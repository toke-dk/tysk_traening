import sqlite3
import lister
import random

conn = sqlite3.connect('ord.db')

c = conn.cursor()

#assert len(lister.l_da) == len(lister.l_ty)
#for i in range(len(lister.l_da)):
#    sql = f"""INSERT INTO ord (dansk, tysk)
#                VALUES ('{lister.l_da[i]}', '{lister.l_ty[i]}')"""
#    c.execute(sql)
#conn.commit()

c.execute("""SELECT dansk
            FROM ord""")

resultat = c.fetchall()
tysk_resultat = resultat[random.randint(0, len(lister.l_ty))][0]

print(tysk_resultat)
