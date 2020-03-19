import sqlite3
import psycopg2
import lister
import os

conn = psycopg2.connect(user=os.getenv("SPROG_DB_USER"),
                        password=os.getenv("SPROG_DB_PW"),
                        host="toke-sprog.cr0dt7iqlyfp.eu-central-1.rds.amazonaws.com",
                        port="5432",
                        database="sprog_app")
c = conn.cursor()

assert len(lister.l_da) == len(lister.l_ty)
for i in range(len(lister.l_da)):
    sql = f"""INSERT INTO ord (dansk, tysk)
               VALUES ('{lister.l_da[i]}', '{lister.l_ty[i]}')"""
    c.execute(sql)
conn.commit()
