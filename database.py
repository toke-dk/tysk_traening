import sqlite3
import lister

conn = sqlite3.connect('ord.db')

c = conn.cursor()

assert len(lister.l_da) == len(lister.l_ty)
for i in range(len(lister.l_da) - 1):
    sql = f"""INSERT INTO ord (dansk, tysk)
                VALUES ('{lister.l_da[i]}', '{lister.l_ty[i]}')"""
    print(sql)
    c.execute(sql)
conn.commit()

print(c.fetchall())
