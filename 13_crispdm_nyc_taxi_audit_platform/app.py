from shared.ui import setup
import streamlit as st, numpy as np, pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
setup("NYC Taxi Audit Platform","Audit → model → explain in one compact CRISP-DM workflow.")
rng=np.random.default_rng(21); n=1800; d=rng.gamma(2,2,n); h=rng.integers(0,24,n); airport=rng.binomial(1,.12,n); y=5+2.9*d+7*airport+5*((h>=16)&(h<=19))+rng.normal(0,3,n); df=pd.DataFrame({"distance":d,"hour":h,"airport":airport,"duration":y}); st.subheader("Data audit"); st.write({"rows":len(df),"missing_cells":int(df.isna().sum().sum()),"duplicates":int(df.duplicated().sum())}); X=df.drop(columns="duration"); Xt,Xv,yt,yv=train_test_split(X,y,test_size=.25,random_state=42); m=GradientBoostingRegressor(random_state=42).fit(Xt,yt); p=m.predict(Xv); st.metric("Validation MAE",f"{mean_absolute_error(yv,p):.2f} min"); st.subheader("Feature importance"); st.bar_chart(pd.Series(m.feature_importances_,index=X.columns).sort_values(ascending=False))
