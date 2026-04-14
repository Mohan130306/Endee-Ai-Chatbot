import streamlit as st
from embedder import get_embedding
from vector_store import store_vector
from rag_pipeline import get_answer

st.title("AskMyDocs AI 🤖")

# Upload text manually
doc = st.text_area("Enter document text:")

if st.button("Store Document"):
    emb = get_embedding(doc)
    store_vector(doc, emb)
    st.success("Stored in Endee!")

query = st.text_input("Ask a question:")

if query:
    answer = get_answer(query)
    st.write("Answer:", answer)