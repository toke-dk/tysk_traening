import sqlite3
import psycopg2
import lister
import os
if os.getenv("SPROG_DB_NAME") is not None:
    db_name = "sprog_app_dev"
else:
    db_name = "sprog_app"
conn = psycopg2.connect(user="sprog_app_user",
                        password="tokes_spr0gsp1l",
                        host="toke-sprog.cr0dt7iqlyfp.eu-central-1.rds.amazonaws.com",
                        port="5432",
                        database=db_name)
c = conn.cursor()

assert len(lister.l_da) == len(lister.l_ty)
for i in range(len(lister.l_da)):
    sql = f"""INSERT INTO ord (dansk, tysk)
               VALUES ('{lister.l_da[i]}', '{lister.l_ty[i]}')"""
    c.execute(sql)
conn.commit()
