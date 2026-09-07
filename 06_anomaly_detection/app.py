from shared.ui import setup
import streamlit as st, numpy as np, pandas as pd
from sklearn.ensemble import IsolationForest
setup("Anomaly Detection","Score synthetic telemetry with Isolation Forest and robust z-scores.")
rng=np.random.default_rng(5); n=1000; x=rng.normal(0,1,n); x[rng.choice(n,25,replace=False)]+=rng.normal(7,1,25); contam=st.slider("Expected anomaly fraction",.01,.15,.03,.01); iso=IsolationForest(contamination=contam,random_state=42); pred=iso.fit_predict(x.reshape(-1,1)); med=np.median(x); mad=np.median(abs(x-med))+1e-9; rz=.6745*(x-med)/mad; df=pd.DataFrame({"value":x,"isolation_anomaly":pred==-1,"robust_z":rz}); st.metric("Detected anomalies",int((pred==-1).sum())); st.line_chart(df[["value"]]); st.dataframe(df[df.isolation_anomaly].sort_values("robust_z",key=abs,ascending=False).head(30),use_container_width=True)
