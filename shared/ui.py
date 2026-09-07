
import streamlit as st

def setup(title, subtitle):
    st.set_page_config(page_title=title,page_icon='🧪',layout='wide')
    st.title(title)
    st.caption(subtitle)
    with st.sidebar:
        st.markdown('### AI-Assisted DS Portfolio')
        st.caption('Built as an original replication/extension of the reference experiment catalog.')
