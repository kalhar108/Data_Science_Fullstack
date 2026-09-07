from shared.ui import setup
import streamlit as st, numpy as np, pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
setup("AutoML Benchmark","Lightweight AutoML leaderboard with reproducible cross-validation.")
X,y=make_classification(n_samples=1200,n_features=16,n_informative=10,random_state=42); models={"Logistic Regression":LogisticRegression(max_iter=1000),"Random Forest":RandomForestClassifier(n_estimators=120,random_state=42),"Gradient Boosting":GradientBoostingClassifier(random_state=42),"KNN":KNeighborsClassifier()}
rows=[]
for name,m in models.items(): s=cross_val_score(m,X,y,cv=5,scoring="roc_auc"); rows.append({"Model":name,"ROC-AUC mean":s.mean(),"std":s.std()})
st.dataframe(pd.DataFrame(rows).sort_values("ROC-AUC mean",ascending=False).round(4),use_container_width=True)
