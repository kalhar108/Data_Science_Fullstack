from shared.ui import setup
import streamlit as st, numpy as np, pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
setup("Customer Segmentation","Segment customers and inspect cluster quality/personas.")
rng=np.random.default_rng(3); n=700; df=pd.DataFrame({"annual_spend":rng.lognormal(8.3,.55,n),"visits":rng.poisson(8,n)+1,"discount_ratio":rng.beta(2,5,n),"tenure_months":rng.integers(1,84,n)})
k=st.slider("Clusters",2,7,4); Z=StandardScaler().fit_transform(df); labels=KMeans(k,random_state=42,n_init=20).fit_predict(Z); st.metric("Silhouette",f"{silhouette_score(Z,labels):.3f}"); p=PCA(2).fit_transform(Z); plot=pd.DataFrame({"PC1":p[:,0],"PC2":p[:,1],"cluster":labels.astype(str)}); st.scatter_chart(plot,x="PC1",y="PC2",color="cluster"); out=df.assign(cluster=labels).groupby("cluster").mean().round(2); st.dataframe(out,use_container_width=True)
