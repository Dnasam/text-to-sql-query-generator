from fastapi import FastAPI
from llm import generate_sql
from database import run_query

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Text-to-SQL API Running"}

@app.get("/query")
def query_database(question: str):

    sql = generate_sql(question)

    results = run_query(sql)

    return {
        "question": question,
        "sql": sql,
        "results": results
    }