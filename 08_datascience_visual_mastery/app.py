from shared.ui import setup
import streamlit as st, numpy as np, pandas as pd
setup("Visual Data Science Mastery","Explore statistical shapes and relationships interactively.")
rng=np.random.default_rng(11); kind=st.selectbox("Visualization",["Distribution","Regression","Correlation","Calibration"]); n=st.slider("Points",100,2000,500)
if kind=="Distribution": st.bar_chart(pd.Series(rng.normal(size=n)).value_counts(bins=30).sort_index())
elif kind=="Regression":
 x=rng.normal(size=n); y=2.4*x+rng.normal(scale=.8,size=n); st.scatter_chart(pd.DataFrame({"x":x,"y":y}),x="x",y="y")
elif kind=="Correlation":
 df=pd.DataFrame(rng.multivariate_normal([0,0,0],[[1,.8,.2],[.8,1,.4],[.2,.4,1]],n),columns=list("ABC")); st.dataframe(df.corr().round(3))
else:
 p=np.linspace(.05,.95,10); observed=np.clip(p+rng.normal(0,.05,10),0,1); st.line_chart(pd.DataFrame({"predicted":p,"observed":observed}).set_index("predicted"))
