from shared.ui import setup
import streamlit as st, pandas as pd, itertools
setup("Market Basket Mining","Mine frequent itemsets and association rules from sample baskets.")
baskets=[{"milk","bread","eggs"},{"bread","butter"},{"milk","bread","butter"},{"beer","chips"},{"milk","eggs"},{"bread","eggs"},{"milk","bread","eggs","butter"},{"beer","chips","salsa"},{"bread","butter","jam"},{"milk","bread"}]*12
items=sorted(set().union(*baskets)); min_support=st.slider("Minimum support",.05,.8,.2,.05); rows=[]
for a,b in itertools.permutations(items,2):
 sup_ab=sum({a,b}<=x for x in baskets)/len(baskets); sup_a=sum(a in x for x in baskets)/len(baskets); sup_b=sum(b in x for x in baskets)/len(baskets)
 if sup_ab>=min_support: rows.append({"Rule":f"{a} → {b}","support":sup_ab,"confidence":sup_ab/sup_a,"lift":(sup_ab/sup_a)/sup_b})
st.dataframe(pd.DataFrame(rows).sort_values("lift",ascending=False).round(3),use_container_width=True)
