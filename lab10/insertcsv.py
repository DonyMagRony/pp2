import psycopg2

    
conn = psycopg2.connect("host=localhost dbname=Phones user=postgres password=1111")
cur = conn.cursor()
with open('something.csv', 'r', encoding="utf-8") as f:
    next(f)
    cur.copy_from(f, 'users', sep=',')
conn.commit()