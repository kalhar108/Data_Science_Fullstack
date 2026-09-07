from shared.ui import setup
import streamlit as st, numpy as np, pandas as pd
setup("Data Science Skills Lab","Five compact interactive labs for core data-science intuition.")
lab=st.selectbox("Lab",["Sampling","Distributions","Feature scaling","Classification metrics","Bias-variance"]); rng=np.random.default_rng(42)
if lab=="Sampling":
 n=st.slider("Sample size",10,1000,100); vals=rng.normal(100,15,n); st.metric("Sample mean",f"{vals.mean():.2f}"); st.line_chart(pd.DataFrame({"running_mean":np.cumsum(vals)/np.arange(1,n+1)}))
elif lab=="Distributions": st.bar_chart(pd.Series(rng.normal(size=2000)).value_counts(bins=30).sort_index())
elif lab=="Feature scaling": st.write(pd.DataFrame({"raw":[1,10,100],"minmax":[0,.09,1],"zscore":[-0.81,-0.59,1.41]}))
elif lab=="Classification metrics": st.write({"Precision":"TP/(TP+FP)","Recall":"TP/(TP+FN)","F1":"harmonic mean of precision and recall"})
else: st.write("High bias → underfit. High variance → overfit. Validation curves help find the useful complexity region.")
