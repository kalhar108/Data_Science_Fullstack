from shared.ui import setup
import streamlit as st, numpy as np, pandas as pd
setup("Nano Transformer Lab","Inspect tokenization and a simplified self-attention computation.")
text=st.text_input("Prompt","data science with transformers")
tokens=text.lower().split(); vocab={t:i for i,t in enumerate(sorted(set(tokens)))}
st.write("Tokens",tokens); st.write("Vocabulary",vocab)
if tokens:
 rng=np.random.default_rng(7); d=8; E=rng.normal(size=(len(vocab),d)); X=np.vstack([E[vocab[t]] for t in tokens]); Q=X; K=X; scores=Q@K.T/np.sqrt(d); A=np.exp(scores-scores.max(axis=1,keepdims=True)); A=A/A.sum(axis=1,keepdims=True); st.subheader("Self-attention matrix"); st.dataframe(pd.DataFrame(A,index=tokens,columns=tokens).round(3),use_container_width=True); st.caption("Educational simplification: Q=K=embedding matrix, shown to make attention mechanics inspectable.")
