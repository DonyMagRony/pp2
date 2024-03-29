import psycopg2
from config import config


def insert(name,phone,adress):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO users(name,adress,phone)
             VALUES(%s,%s,%s) RETURNING user_id;"""
    conn = None
    vendor_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (name,phone,adress,))
        # get the generated id back
        vendor_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return vendor_id

name=(input("name:"))
phone=(input("phone:"))
adress=(input("adress:"))
insert(name,adress,phone)