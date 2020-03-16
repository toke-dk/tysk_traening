#!/usr/bin/env python3
import random
import time
import lister
import brugernavn
import sqlite3


def start():
    print("1: Fra Tysk til Dansk. ")
    print("2: Fra Dansk til Tysk. ")


def clear_screen():
    print("\033c", end="")


clear_screen()
input(f"Velkommen {brugernavn.brugernavn_fra_db}. Tryk enter for at starte")
brugernavn.c.execute(f"""SELECT tid_sekunder 
                        FROM brugernavn
                        WHERE brugernavn='{brugernavn.brugernavn_fra_db}'""")
brugernavn.conn.commit()
print(brugernavn.brugernavn_fra_db)
bruger_tid = brugernavn.c.fetchall()
print(f"Din sidste tid er {bruger_tid[0][0]} sekunder")
start()
sprog = input("")
print()

while True:
    if sprog == "1" or sprog == "2":
        break
    else:
        print("Ugyldig kommando")
        start()
        sprog = input("")
        print()
forsøg = 0


def ordene(index_liste):
    gang = 0
    rigtig = 0
    forkert = 0

    random.shuffle(index_liste)

    for v in range(len(index_liste)):
        print(v + 1)
        # her starter spørgsmålene
        if sprog.lower() == "1":
            word_ty = lister.l_ty[index_liste[gang]]
            word_da = lister.l_da[index_liste[gang]]
            print(word_ty)
            svar = input("")

            if svar.lower() == word_da.lower():
                print("Rigtig")
                print()
                rigtig = rigtig + 1
                index_liste.remove(index_liste[gang])
            else:
                print(f"Forkert. '{word_ty}' på dansk er '{word_da}'")
                print()
                forkert = forkert + 1
                gang = gang + 1
        # her starter det andede
        elif sprog.lower() == "2":
            word_ty = lister.l_ty[index_liste[gang]]
            word_da = lister.l_da[index_liste[gang]]
            print(word_da)
            svar = input("")

            if svar.lower() == word_ty.lower():
                print("Rigtig")
                print()
                rigtig = rigtig + 1
                index_liste.remove(index_liste[gang])
            else:
                print(f"Forkert. '{word_da}' på tysk er '{word_ty}'")
                print()
                forkert = forkert + 1
                gang = gang + 1
    return (rigtig, forkert, index_liste)


antal_l = [
]
forkert_l = [
]

rand_num = random.randint(0, (len(lister.glade_komentare) - 1))
øve_liste = []
for i in range(40):
    øve_liste.append(i)
start_tid = time.time()
(rigtig, forkert, rest_liste) = ordene(øve_liste)
forsøg = forsøg + 1
procent = int((rigtig / 40) * 100)
# efter 1. forsøg
time.sleep(1.4)
clear_screen()
print(f"Du fik '{rigtig}' rigtige, og '{forkert}' forkerte ")
print(f'Du fik {procent}% rigtige')
print("")
print(f"{lister.glade_komentare[rand_num]}")
input("Nu kommer de forkerte (tryk enter)")
print("")
# her 
gang = 0

while len(rest_liste) > 0:
    (rigtig, forkert, rest_liste) = ordene(rest_liste)
    procent = int((rigtig / 40) * 100)
    time.sleep(1.4)
    clear_screen()
    print(f"Der er kun {len(rest_liste)} ord tilbage")
    print("")
    forsøg = forsøg + 1
slut_tid_sekunder = time.time()
sekunder = (slut_tid_sekunder - start_tid) % 60
minutter = (slut_tid_sekunder - start_tid) // 60

brugernavn.c.execute(f"""UPDATE brugernavn
                        SET tid_sekunder=({int(slut_tid_sekunder-start_tid)})
                        WHERE brugernavn='{brugernavn.brugernavn_fra_db}'""")
brugernavn.conn.commit()
# helt slutning
print("Tillykke. Du gjorde det")
print(f"Det tog dig {forsøg} forsøg at lave 100% rigtige")
print(f"{lister.glade_komentare[rand_num]}")
input("Her kommer din tid: (tryk enter)")
print(f"Minutter: {int(minutter)}")
print(f"Sekunder: {int(sekunder)}")
