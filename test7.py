import psycopg2

conn = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='wizard32',
    host='127.0.0.1',
    port=5432)
cur = conn.cursor()

cur.execute("INSERT INTO users (login, password) VALUES (%s, %s)", ("Maison", "123"))
cur.execute("INSERT INTO users (login, password) VALUES (%s, %s)", ("eax", "456"))
conn.commit()

cur.execute("SELECT * FROM users")
print(cur.fetchall())
