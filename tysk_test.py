#!/usr/bin/env python3
import random

print("1: Fra Tysk til Dansk. ")
print("2: Fra Dansk til Tysk. ")

sprog = input("")

print("Skal de blandes? ja/nej")

bland = input("")

print()

antal = 0
gang = 0
rigtig = 0
forkert = 0


l_ty = [
    "Freunde",
    "Woher",
    "Was",
    "Welche",
    "Lieblingstier",
    "Essen",
    "Freundschaft",
    "Geht",
    "Wo",
    "Herbst",
    "Jahreszeiten",
    "Machen",
    "Spass",
    "Leicht",
    "Schwer",
    "Scheint",
    "Wenn",
    "Besonders",
    "Schlafen",
    "Wetter",
    "Laufen",
    "Tanzen",
    "Antwort",
    "Trinken",
    "Viele",
    "Sehr",
    "Glaube",
    "Entschuldigung",
    "Schon",
    "Einige",
    "Hoffe",
    "Versteht",
    "Gemütlich",
    "Links",
    "Rechts",
    "Weit",
    "geradeaus",
    "Gesund",
    "Wieder",
    "Hier"

]

l_da = [
    "Ven",
    "Hvorfra",
    "Hvad",
    "Hvilke",
    "Yndlingsdyr",
    "Spise",
    "Venskab",
    "Går",
    "Hvor",
    "Efterår",
    "Årstider",
    "Laver",
    "Sjov",
    "Let",
    "Svært",
    "Skinner",
    "Når",
    "Særligt",
    "Sove",
    "Vejr",
    "Løbe",
    "Danse",
    "Svar",
    "Drikke",
    "Mange",
    "Meget",
    "Tror",
    "Undskyld",
    "Allerede",
    "Nogle",
    "Håber",
    "Forstår",
    "Hyggeligt",
    "Venstre",
    "Højre",
    "Langt",
    "Ligeud",
    "Sund",
    "Igen",
    "Her",

]


if sprog == "1" and bland.lower() == "nej":
    for i in range(40):

        if gang == 40:
          break

        else:

          gang = gang + 1

          print(gang)

          #her starter spørgsmålene

          print(l_ty[antal])
          svar = input("")

          if svar.lower() == l_da[antal].lower():
              print("rigtig")
              print()
          else:
              print(f"forkert. '{l_ty[antal]}' på dansk er '{l_da[antal]}'")
              print()

          antal = antal + 1
          continue


if sprog == "2" and bland.lower() == "nej":
    for i in range(40):

        if gang == 40:
          break

        else:

          gang = gang + 1

          print(gang)

          #her starter spørgsmålene

          print(l_da[antal])
          svar = input("")

          if svar.lower() == l_ty[antal].lower():
              print("rigtig")
              print()
          else:
              print(f"forkert. '{l_da[antal]}' på tysk er '{l_ty[antal]}'")
              print()

          antal = antal + 1
          continue


if sprog == "1" and bland == "ja":
    antal_l = []
    for i in range(40):
        antal = random.randint(0, 39)

        while True:
            if antal in antal_l:
                antal = random.randint(0, 39)
                continue
            else:
                break


        antal_l.append(antal)
        gang = gang + 1
        print(gang)

        # her starter spørgsmålene

        print(l_ty[antal])
        svar = input("")

        if svar.lower() == l_da[antal].lower():
            print("rigtig")
            print()
            rigtig = rigtig + 1

        else:
            print(f"forkert. '{l_ty[antal]}' på dansk er '{l_da[antal]}'")
            print()
            forkert = forkert + 1

        if gang == 40:
            break

        else:
            continue



if sprog == "2" and bland == "ja":
    antal_l = []
    for i in range(40):
        antal = random.randint(0, 39)

        while True:
            if antal in antal_l:
                antal = random.randint(0, 39)
                continue
            else:
                break

        antal_l.append(antal)
        gang = gang + 1
        print(gang)

        #her starter spørgsmålene

        print(l_da[antal])
        svar = input("")

        if svar.lower() == l_ty[antal].lower():
            print("rigtig")
            print()
            rigtig = rigtig + 1

        else:
            print(f"forkert. {l_da[antal]} på tysk er {l_ty[antal]}")
            print()
            forkert = forkert + 1

        if gang == 40:
            break

        else:
            continue





print(f"Finnish! Du fik '{rigtig}' rigte, og '{forkert}' forkerte ")
