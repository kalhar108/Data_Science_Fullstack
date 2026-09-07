from shared.ui import setup
import streamlit as st, json
setup("CRISP-DM Mastery","Turn a data-science idea into a structured CRISP-DM execution plan.")
phases=["Business Understanding","Data Understanding","Data Preparation","Modeling","Evaluation","Deployment"]
notes={}
for p in phases:
 with st.expander(p,expanded=p==phases[0]): notes[p]=st.text_area(f"Notes for {p}",key=p)
st.download_button("Download project brief",json.dumps(notes,indent=2),"crispdm_project.json")
