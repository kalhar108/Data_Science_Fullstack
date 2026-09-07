from shared.ui import setup
from shared.common import metric_cards, regression_metrics
import streamlit as st, numpy as np, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
setup("NYC Taxi Trip Prediction","Compare regression models on synthetic taxi trips with geospatial and temporal features.")
rng=np.random.default_rng(42); n=2500
dist=rng.gamma(2.2,2.0,n); hour=rng.integers(0,24,n); rain=rng.binomial(1,.18,n); passenger=rng.integers(1,5,n); traffic=1+.5*np.exp(-((hour-8)/2.2)**2)+.6*np.exp(-((hour-17)/2.5)**2); y=4+3.1*dist*traffic+4*rain+rng.normal(0,3,n)
X=pd.DataFrame({"distance_mi":dist,"hour":hour,"rain":rain,"passengers":passenger})
Xt,Xv,yt,yv=train_test_split(X,y,test_size=.25,random_state=42)
models={"Linear":LinearRegression(),"Random Forest":RandomForestRegressor(n_estimators=150,random_state=42),"Gradient Boosting":GradientBoostingRegressor(random_state=42)}
rows=[]
for name,m in models.items(): m.fit(Xt,yt); pred=m.predict(Xv); rows.append({"Model":name,**regression_metrics(yv,pred)})
st.dataframe(pd.DataFrame(rows).sort_values("MAE"),use_container_width=True)
model=models["Gradient Boosting"]
st.subheader("Try a trip")
c1,c2,c3=st.columns(3); d=c1.slider("Distance (mi)",.5,25.,5.); h=c2.slider("Hour",0,23,17); r=c3.checkbox("Rain")
p=float(model.predict(pd.DataFrame([{ "distance_mi":d,"hour":h,"rain":int(r),"passengers":1}]))[0]); st.metric("Predicted trip duration",f"{p:.1f} min")
