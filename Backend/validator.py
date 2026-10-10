FORBIDDEN = ["DROP", "DELETE", "UPDATE"]

def validate_sql(sql):

    upper_sql = sql.upper()

    for word in FORBIDDEN:
        if word in upper_sql:
            return False

    return True