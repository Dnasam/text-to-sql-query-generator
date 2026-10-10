import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="texttosql",
    user="postgres",
    password="postgres"
)

cursor = conn.cursor()

def run_query(query):

    cursor.execute(query)

    try:
        rows = cursor.fetchall()

        columns = [desc[0] for desc in cursor.description]

        results = []

        for row in rows:
            results.append(dict(zip(columns, row)))

        return results

    except:
        return []