from shared.ui import setup
from shared.common import regression_metrics
import streamlit as st, numpy as np, pandas as pd
from sklearn.ensemble import RandomForestRegressor
setup("TimePulse Forecasting","Lag-feature forecasting with leakage-safe chronological holdout.")
rng=np.random.default_rng(4); n=500; t=np.arange(n); y=20+.035*t+3*np.sin(2*np.pi*t/30)+rng.normal(0,1,n); df=pd.DataFrame({"y":y});
for lag in range(1,15): df[f"lag{lag}"]=df.y.shift(lag)
df=df.dropna(); split=int(len(df)*.8); X=df.drop(columns="y"); model=RandomForestRegressor(n_estimators=160,random_state=42).fit(X.iloc[:split],df.y.iloc[:split]); pred=model.predict(X.iloc[split:]); st.write(regression_metrics(df.y.iloc[split:],pred)); chart=pd.DataFrame({"actual":df.y.iloc[split:].values,"forecast":pred}); st.line_chart(chart)
