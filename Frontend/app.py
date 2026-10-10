import streamlit as st
import requests
import pandas as pd

st.title("Text-to-SQL System")

question = st.text_input("Ask a question")

if st.button("Generate SQL"):

    url = f"http://127.0.0.1:8000/query?question={question}"

    response = requests.get(url)

    data = response.json()

    st.subheader("Generated SQL")
    st.code(data["sql"], language="sql")

    st.subheader("Results")

    df = pd.DataFrame(data["results"])

    st.dataframe(df)