import streamlit as st
import requests

st.title("🧠 Job Memory Agent")

st.header("Save Job Application")
company = st.text_input("Company")
role = st.text_input("Role")
notes = st.text_area("Notes")

if st.button("Save to Memory"):
    r = requests.post("http://127.0.0.1:8000/remember",
                      json={"company":company, "role":role, "notes":notes})
    st.success(f"Saved! {r.json()}")

st.header("Ask Your Memory")
question = st.text_input("Ask Anything")

if st.button("Get Answer"):
    r = requests.post("http://127.0.0.1:8000/recall",
                      json ={"question":question})
    st.write(r.json()["answer"])