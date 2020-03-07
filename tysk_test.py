#!/usr/bin/env python3
import random

print("1: Fra Tysk til Dansk. ")
print("2: Fra Dansk til Tysk. ")

sprog = input("")

print("Skal de blandes? ja/nej")

bland = input("")

print()

def tyskTilDansk():
  antal = 0
  gang = 0
  rigtig = 0
  forkert = 0
  for i in range(len(l_da)):
    gang = gang + 1
    print(gang)
    # her starter spørgsmålene
    word = l_ty[antal]
    print(word)
    svar = input("")

    if svar.lower() == l_da[antal].lower():
        print("rigtig")
        print()
        rigtig = rigtig + 1
        forkert_l.remove(word)
        l_da.remove(l_da[antal])
        l_ty.remove(l_ty[antal])
        #if antal == 0:
        #  antal = 0
        #else:
        #  antal = antal - 1
    else:
        print(f"forkert. '{word}' på dansk er '{l_da[antal]}'")
        print()
        forkert = forkert + 1
        antal = antal + 1
    continue
  return (rigtig, forkert)
  

antal_l = [
]

forkert_l = [
]

glade_komentare = [
    "Godt gået",
    "Super flot",
    "Fantastisk gjort",
    "Sådan dér",
    "Det kører med klatten fister",
    "Du styrer få vildt",
    "Virkelig flot"
]

rand_num = random.randint(0, len(glade_komentare))

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

if sprog == "1" and bland.lower() == "nej" or bland.lower() == "n":
  forkert_l = l_ty.copy()
  (rigtig, forkert) = tyskTilDansk()
  print(rigtig)
  print(forkert)
  procent = int((rigtig / 40) * 100)


if sprog == "2" and bland.lower() == "nej":
    for i in range(40):
        gang = gang + 1
        print(gang)
        # her starter spørgsmålene
        word = l_da[antal]
        print(word)
        svar = input("")

        if svar.lower() == l_ty[antal].lower():
            print("rigtig")
            print()
            rigtig = rigtig + 1
        else:
            print(f"forkert. '{word}' på tysk er '{l_ty[antal]}'")
            print()
            forkert_l.append(word)
            forkert = forkert + 1
        antal = antal + 1
        continue

if sprog == "1" and bland == "ja":
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
        word = l_ty[antal]
        print(word)
        svar = input("")

        if svar.lower() == l_da[antal].lower():
            print("rigtig")
            print()
            rigtig = rigtig + 1
        else:
            print(f"forkert. '{word}' på dansk er '{l_da[antal]}'")
            print()
            forkert_l.append(word)
            forkert = forkert + 1

        if gang == 40:
            break
        else:
            continue

if sprog == "2" and bland == "ja":

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
        word = l_da[antal]
        print(word)
        svar = input("")

        if svar.lower() == l_ty[antal].lower():
            print("rigtig")
            print()
            rigtig = rigtig + 1
        else:
            print(f"forkert. {word} på tysk er {l_ty[antal]}")
            print()
            forkert_l.append(word)
            forkert = forkert + 1

        if gang == 40:
            break
        else:
            continue

procent = int((rigtig / 40) * 100)

# efter 1. forsøg
print(f"Finnish! Du fik '{rigtig}' rigte, og '{forkert}' forkerte ")
print(f'Du fik {procent}% rigtige')
print("")
print(f"{glade_komentare[rand_num]}")
input("Nu kommer de forkerte (tryk enter)")

# her kommer 2. forsøg


gang = 0

antal_l = [
]
if sprog == "1":
  tyskTilDansk()

if sprog == "2":
    print("Her kommer de ord du fik forkerte")
    print("")

    for i in range(forkert):
        gang = gang + 1
        print(gang)
        forkertToList = forkert - 1
        antal = random.randint(0, forkertToList)

        while True:
            if antal in antal_l:
                random.randint(0, forkertToList)
                continue
            else:
                break
        print(forkert_l[antal])
        svar2 = input("")

        if svar2.lower() == l_da[antal].lower():
            print("Rigtigt")
            print()
            rigtig = rigtig + 1
        else:
            print("forkert")
            print("")
            # print(f"Forkert. '{forkert_l[antal]}' er '{}' ")
            forkert2 = forkert + 1
            continue
# helt slutning
print(f"Finnish! På 1. og 2. forsøg fik du {rigtig} rigtige og {forkert} forkerte")
print(f"Du fik så {procent}% rigtige.")
print(f"{glade_komentare[rand_num]}")

