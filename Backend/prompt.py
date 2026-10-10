PROMPT = """
You are a PostgreSQL expert.

Database Schema:

Table customers:
- customer_id
- name
- city

Table orders:
- order_id
- customer_id
- amount
- order_date

Generate ONLY SQL query.
"""