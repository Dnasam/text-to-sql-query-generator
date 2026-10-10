# Text-to-SQL Query Generator

A rule-based application that converts natural language questions into SQL queries and displays the corresponding database results through an interactive web interface.

## Features

- Natural language input for supported query patterns
- Rule-based SQL query generation without an LLM
- FastAPI backend for query processing
- Streamlit frontend for interactive use
- SQL query display and tabular result visualization
- Relational database integration

## Tech Stack

Python, FastAPI, Streamlit, Pandas, SQLAlchemy

## Architecture

Streamlit Frontend → FastAPI Backend → SQL Generation and Validation → Database Execution → Results

## Run Locally

1. Create and activate a Python virtual environment.
2. Install dependencies:

   `pip install -r requirements.txt`

3. Start the FastAPI backend using the correct module path:

   `uvicorn Backend.main:app --reload`

4. In a second terminal, start the Streamlit frontend:

   `streamlit run Frontend/app.py`

5. Open the Streamlit URL shown in the terminal.

FastAPI documentation is available at `/docs` on the local backend.

## Note

SQL generation is implemented using rule-based logic, not a Large Language Model (LLM). Supported questions depend on the rules implemented in the application.