import sqlite3
import getpass
import psycopg2
import os

conn = psycopg2.connect(user=os.getenv("SPROG_DB_USER"),
                        password=os.getenv("SPROG_DB_PW"),
                        host="toke-sprog.cr0dt7iqlyfp.eu-central-1.rds.amazonaws.com",
                        port="5432",
                        database="sprog_app")
c = conn.cursor()
while True:
    try:
        print("1: Log ind.")
        print("2: Opret dig.")
        sign_in_sign_up = int(input(""))
    except ValueError:
        print("Enten 1 eller 2")
        continue
    if sign_in_sign_up == 2:
        while True:
            try:
                brugernavn_input = input("Brugernavn: ")
                adgangskode_input = getpass.getpass("Adgangskode: ")

                sql = f"""INSERT INTO brugernavn (brugernavn, adgangskode)
                    VALUES ('{brugernavn_input}', '{adgangskode_input}')"""
                c.execute(sql)
                conn.commit()
                c.execute("SELECT * FROM brugernavn")
            except sqlite3.IntegrityError:
                print()
                print("Brugernavn er allerede taget")
                print()
                continue
            break
        continue

    elif sign_in_sign_up == 1:
        while True:
            try:
                brugernavn_input = input("Brugernavn: ")
                adgangskode_input = getpass.getpass("Adgangskode: ")
                c.execute(f"""SELECT * FROM brugernavn
                            WHERE brugernavn='{brugernavn_input}'""")
                conn.commit()
                result = c.fetchall()
                adgangskode_fra_db = result[0][1]
                brugernavn_fra_db = result[0][0]
                if adgangskode_input == adgangskode_fra_db:
                    break
                print()
                print("Forkert kode")
                print()
            except IndexError:
                print()
                print("Ugyldig brugernavn eller adgangskode")
                print()
                continue
        break
    else:
        print("Ugyldig kommando")