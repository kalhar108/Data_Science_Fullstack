from shared.ui import setup
import streamlit as st, pandas as pd, json
setup("Dynamic Experiment Workspace","Track experiments, priorities and completion telemetry.")
if "tasks" not in st.session_state: st.session_state.tasks=[{"Task":"EDA","Priority":"High","Done":True},{"Task":"Baseline model","Priority":"High","Done":False},{"Task":"Error analysis","Priority":"Medium","Done":False}]
with st.form("add"):
 t=st.text_input("New task"); p=st.selectbox("Priority",["High","Medium","Low"]); submitted=st.form_submit_button("Add")
 if submitted and t: st.session_state.tasks.append({"Task":t,"Priority":p,"Done":False})
df=pd.DataFrame(st.session_state.tasks); st.dataframe(df,use_container_width=True); st.progress(float(df.Done.mean()) if len(df) else 0); st.download_button("Export JSON",json.dumps(st.session_state.tasks,indent=2),"workspace.json")
