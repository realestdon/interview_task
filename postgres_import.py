import psycopg2
import csv
conn = psycopg2.connect("host=localhost dbname=hashmicro user=odoo10 password=admin")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE users(
    name text,
    login text,
    email text,
    active boolean
)
""")
with open('users.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        print(row)
        cur.execute(
        "INSERT INTO users VALUES (%s, %s, %s, %s)",
    )
conn.commit()
