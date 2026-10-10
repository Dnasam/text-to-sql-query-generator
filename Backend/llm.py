def generate_sql(question):

    question = question.lower()

    mappings = {
        "show all customers": "SELECT * FROM customers;",
        "list all customers": "SELECT * FROM customers;",
        "show all orders": "SELECT * FROM orders;",
        "list all orders": "SELECT * FROM orders;",
        "customers from delhi": "SELECT * FROM customers WHERE city='Delhi';",
        "customers from mumbai": "SELECT * FROM customers WHERE city='Mumbai';",
        "total orders": "SELECT COUNT(*) FROM orders;",
        "highest order": "SELECT MAX(amount) FROM orders;",
    }

    for key in mappings:
        if key in question:
            return mappings[key]

    return "SELECT * FROM customers;"