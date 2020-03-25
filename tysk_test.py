#!/usr/bin/env python3
# psql -h toke-sprog.cr0dt7iqlyfp.eu-central-1.rds.amazonaws.com sprog_app sprog_reader
import random
import time
import lister
import brugernavn
import psycopg2
import os


def highscore():
    conn = psycopg2.connect(user="sprog_app_user",
                            password="tokes_spr0gsp1l",
                            host="toke-sprog.cr0dt7iqlyfp.eu-central-1.rds.amazonaws.com",
                            port="5432",
                            database="sprog_app")

    c = conn.cursor()

    c.execute("""SELECT * FROM brugernavn
                ORDER BY tid_sekunder ASC;""")
    conn.commit()
    c.execute("SELECT brugernavn, tid_sekunder FROM brugernavn LIMIT 5")
    conn.commit()
    topfem_liste = c.fetchall()
    print("Dette er top 5 listen for personerne med bedst tid:")
    for i in range(len(topfem_liste)):
        if topfem_liste[i][1] != None:

            print(f"{i + 1}: {topfem_liste[i][0]}, {topfem_liste[i][1]} Minutter {topfem_liste[i][1]} Sekunder")
        else:
            print(f"{i + 1}: {topfem_liste[i][0]}, 0 Minutter 0 Sekunder")


def start():
    print("1: Fra Tysk til Dansk. ")
    print("2: Fra Dansk til Tysk. ")


def clear_screen():
    print("\033c", end="")


highscore()
print()
brugernavn.login()

en_gang_til = True

clear_screen()


print()
print(f"Velkommen {brugernavn.brugernavn_fra_db}")
brugernavn.c.execute(f"""SELECT tid_sekunder 
                        FROM brugernavn
                        WHERE brugernavn='{brugernavn.brugernavn_fra_db}'""")
brugernavn.conn.commit()
bruger_tid = brugernavn.c.fetchall()
input(f"Din sidste tid er {bruger_tid[0][0]} sekunder (Tryk enter for at starte)")
print()

while en_gang_til:
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
        rigtig = 0
        forkert = 0
        naturlig_tal = 0
        global oversat_sprog, svaret, screen_printet_word, land
        random.shuffle(index_liste)
        c.execute("SElECT * FROM ord")
        conn.commit()
        result = c.fetchall()
        for v in range(len(index_liste)):
            print(v + 1)
            random_word = result[index_liste[naturlig_tal]]
            random_word_tysk = random_word[0]
            random_word_dansk = random_word[1]
            # her starter spørgsmålene
            if sprog == '1':
                oversat_sprog = 1
                screen_printet_word = 0
                land = 'Dansk'
                print(random_word_tysk)
                svaret = input("")
            if sprog == '2':
                land = 'Tysk'
                oversat_sprog = 0
                screen_printet_word = 1
                print(random_word_dansk)
                svaret = input("")
            c.execute(f"SELECT * FROM ord WHERE tysk='{random_word_tysk}'")
            conn.commit()
            resultat = c.fetchall()
            rigtige_svar = resultat[0][oversat_sprog]
            if svaret.lower() == rigtige_svar.lower():
                print(f"Rigtigt")
                rigtig = rigtig + 1
                index_liste.remove(index_liste[naturlig_tal])
            else:
                print(f"Ikke helt. '{resultat[0][screen_printet_word]}' på {land} er '{rigtige_svar}'")
                forkert = forkert + 1
                naturlig_tal = naturlig_tal + 1
            print()
        return rigtig, forkert, index_liste


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
                            SET tid_sekunder=({int(slut_tid_sekunder - start_tid)})
                            WHERE brugernavn='{brugernavn.brugernavn_fra_db}'""")
    brugernavn.conn.commit()
    # helt slutning
    print("Tillykke. Du gjorde det")
    print(f"Det tog dig {forsøg} forsøg at lave 100% rigtige")
    print(f"{lister.glade_komentare[rand_num]}")
    input("Her kommer din tid: (tryk enter)")
    print(f"Minutter: {int(minutter)}")
    print(f"Sekunder: {int(sekunder)}")
    highscore()
    # Vil man gerne blive ved
    print()
    print("Vil du prøve igen? J/N")
    en_gang_til = input()
    if en_gang_til.lower() == "j":
        clear_screen()
        continue
    elif en_gang_til.lower() == "n":
        en_gang_til = False
    else:
        while True:
            print("Ugyldig kommando")
            print()
            print("Vil du prøve igen? J/N")
            en_gang_til = input()
            if en_gang_til.lower() == 'j' or en_gang_til.lower() == "n":
                break
        if en_gang_til.lower() == "j":
            clear_screen()
            continue
        else:
            en_gang_til = False
