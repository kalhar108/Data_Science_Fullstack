
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, accuracy_score, f1_score

def seed_everything(seed=42):
    np.random.seed(seed)

def regression_metrics(y_true,y_pred):
    return {"MAE":float(mean_absolute_error(y_true,y_pred)),"RMSE":float(mean_squared_error(y_true,y_pred)**0.5),"R2":float(r2_score(y_true,y_pred))}

def classification_metrics(y_true,y_pred):
    return {"Accuracy":float(accuracy_score(y_true,y_pred)),"F1":float(f1_score(y_true,y_pred,average='weighted'))}

def metric_cards(st, metrics):
    cols=st.columns(len(metrics))
    for c,(k,v) in zip(cols,metrics.items()): c.metric(k,f"{v:.3f}")
