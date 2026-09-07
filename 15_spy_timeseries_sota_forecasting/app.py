from shared.ui import setup
import streamlit as st, numpy as np, pandas as pd
from sklearn.linear_model import Ridge
setup("SPY Forecasting Research Lab","Leakage-safe walk-forward return prediction and strategy diagnostics on synthetic market data.")
rng=np.random.default_rng(15); n=1200; ret=rng.normal(.0003,.012,n); ret[2:]+=0.08*ret[:-2]; px=100*np.exp(np.cumsum(ret)); df=pd.DataFrame({"return":ret,"price":px});
for l in range(1,11): df[f"lag{l}"]=df['return'].shift(l)
df=df.dropna(); X=df[[f"lag{i}" for i in range(1,11)]].values; y=df['return'].values; start=300; preds=np.full(len(y),np.nan)
for i in range(start,len(y),20):
 end=min(i+20,len(y)); m=Ridge(alpha=10).fit(X[:i],y[:i]); preds[i:end]=m.predict(X[i:end])
mask=~np.isnan(preds); strat=np.sign(preds[mask])*y[mask]; sharpe=np.sqrt(252)*strat.mean()/(strat.std()+1e-9); bh=np.sqrt(252)*y[mask].mean()/(y[mask].std()+1e-9); c1,c2=st.columns(2); c1.metric("Strategy Sharpe",f"{sharpe:.2f}"); c2.metric("Buy & Hold Sharpe",f"{bh:.2f}"); st.line_chart(pd.DataFrame({"strategy":np.cumprod(1+strat),"buy_hold":np.cumprod(1+y[mask])}))
