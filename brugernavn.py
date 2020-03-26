import sqlite3
import getpass
import psycopg2
import os

def login():
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
                    print()
                    print("ADVARSEL: Adgangskoden bliver ikke krypteret! Brug en ny ligegyldig adgangskode.")
                    adgangskode_input = getpass.getpass("Adgangskode: ")

                    print("Gentag din adgangskode")
                    adgangskodeto = getpass.getpass("Adgangskode")
                    if adgangskode_input == adgangskodeto:
                        sql = f"""INSERT INTO brugernavn (brugernavn, adgangskode)
                            VALUES ('{brugernavn_input}', '{adgangskode_input}')"""
                        c.execute(sql)
                        conn.commit()
                        c.execute("SELECT * FROM brugernavn")
                    else:
                        print("Forkert adgangskode")
                        print()
                        continue
                except psycopg2.IntegrityError:
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
    return brugernavn_fra_db