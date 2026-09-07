from shared.ui import setup
import streamlit as st, numpy as np, pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from scipy.sparse import hstack
setup("Multimodal AutoML Suite","Fuse tabular and text features, then compare unimodal vs multimodal models.")
rng=np.random.default_rng(8); n=1000; spend=rng.normal(50,15,n); rating=rng.integers(1,6,n); texts=np.array(["excellent premium product","good value","average item","poor quality","terrible return"])[rating-1]; y=((spend>50)&(rating>=4)).astype(int); idx=np.arange(n); rng.shuffle(idx); tr=idx[:750]; te=idx[750:]; vec=TfidfVectorizer(); Ttr=vec.fit_transform(texts[tr]); Tte=vec.transform(texts[te]); tab=np.c_[spend,rating]; sc=StandardScaler(); Atr=sc.fit_transform(tab[tr]); Ate=sc.transform(tab[te]); rows=[]
for name,Xtr,Xte in [("Tabular",Atr,Ate),("Text",Ttr,Tte),("Fused",hstack([Atr,Ttr]),hstack([Ate,Tte]))]:
 m=LogisticRegression(max_iter=1000).fit(Xtr,y[tr]); rows.append({"Model":name,"ROC-AUC":roc_auc_score(y[te],m.predict_proba(Xte)[:,1])})
st.dataframe(pd.DataFrame(rows).sort_values("ROC-AUC",ascending=False).round(4),use_container_width=True)
