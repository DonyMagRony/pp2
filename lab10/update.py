import psycopg2
from config import config


def updaten(data,adress):
    
    sql = """UPDATE users
             SET name=%s
             WHERE adress=%s
             RETURNING user_id"""
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
        cur.execute(sql, (data,adress))
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

def updatep(data,adress):
   
    sql = """UPDATE users
             SET phone = %s
             WHERE adress=%s
             RETURNING user_id"""
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
        cur.execute(sql, (data,adress))
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

choose=input("update name-1 or phone-2: ")

if choose=="1":
    name=input("name: ")
    adress=input("adress: ")
    updaten(name,adress)
if choose=="2":
    phone=input("phone: ")
    adress=input("adress: ")
    updatep(phone,adress)    


