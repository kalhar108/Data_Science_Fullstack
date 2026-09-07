from shared.ui import setup
import streamlit as st, pandas as pd, numpy as np
setup("Enterprise Data Science Audit","Upload a CSV or inspect a generated dataset for common quality risks.")
up=st.file_uploader("CSV",type="csv")
if up: df=pd.read_csv(up)
else:
 rng=np.random.default_rng(1); df=pd.DataFrame({"age":rng.integers(18,80,500),"income":rng.normal(70000,18000,500),"target":rng.integers(0,2,500)}); df.loc[:15,"income"]=np.nan; df=pd.concat([df,df.iloc[:5]],ignore_index=True)
report=pd.DataFrame({"dtype":df.dtypes.astype(str),"missing_pct":df.isna().mean(),"unique":df.nunique()}); st.dataframe(report,use_container_width=True); c1,c2,c3=st.columns(3); c1.metric("Rows",len(df)); c2.metric("Duplicate rows",int(df.duplicated().sum())); c3.metric("Columns >30% missing",int((df.isna().mean()>.3).sum())); st.write("Leakage heuristic: inspect columns with near-perfect correlation to target and post-outcome timestamps before modeling.")
