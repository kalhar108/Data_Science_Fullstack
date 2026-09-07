from shared.ui import setup
import streamlit as st
from collections import defaultdict, deque
setup("FlowForge DAG Engine","Define dependencies and run topological sorting with cycle detection.")
raw=st.text_area("Edges (one A,B per line)","ingest,clean\nclean,features\nfeatures,train\ntrain,evaluate\nevaluate,report")
edges=[]
for line in raw.splitlines():
 if "," in line: edges.append(tuple(x.strip() for x in line.split(",",1)))
nodes=set(sum(([a,b] for a,b in edges),[])); indeg={n:0 for n in nodes}; g=defaultdict(list)
for a,b in edges:g[a].append(b);indeg[b]+=1
q=deque(sorted([n for n in nodes if indeg[n]==0])); order=[]
while q:
 n=q.popleft();order.append(n)
 for v in g[n]:
  indeg[v]-=1
  if indeg[v]==0:q.append(v)
if len(order)!=len(nodes): st.error("Cycle detected: DAG is invalid")
else: st.success("Valid DAG"); st.code(" → ".join(order))
