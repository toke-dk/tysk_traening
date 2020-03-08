#!/usr/bin/env python3
import random

print("1: Fra Tysk til Dansk. ")
print("2: Fra Dansk til Tysk. ")
sprog = input("")
print()

def ikke_blandede(index_liste):
  gang = 0
  rigtig = 0
  forkert = 0

  random.shuffle(index_liste)

  for v in range(len(index_liste)):
    print(v + 1)
    # her starter spørgsmålene
    if sprog.lower() == "1":
      word_ty = l_ty[index_liste[gang]]
      word_da = l_da[index_liste[gang]]
      print(word_ty)
      svar = input("")

      if svar.lower() == word_da.lower():
        print("Rigtig")
        print()
        rigtig = rigtig + 1
        index_liste.remove(index_liste[gang])
      else:
        print(f"forkert. '{word_ty}' på dansk er '{word_da}'")
        print()
        forkert = forkert + 1
        gang = gang + 1
# anden del
    elif sprog.lower() == "2":
      word_ty = l_ty[index_liste[gang]]
      word_da = l_da[index_liste[gang]]
      print(word_da)
      svar = input("")

      if svar.lower() == word_ty.lower():
        print("Rigtig")
        print()
        rigtig = rigtig + 1
        index_liste.remove(index_liste[gang])
      else:
        print(f"forkert. '{word_da}' på tysk er '{word_ty}'")
        print()
        forkert = forkert + 1
        gang = gang + 1
  return (rigtig, forkert, index_liste)

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

rand_num = random.randint(0, (len(glade_komentare) - 1))
øve_liste = []
for i in range(40):
  øve_liste.append(i)
(rigtig, forkert, rest_liste) = ikke_blandede(øve_liste)
procent = int((rigtig / 40) * 100)  
# efter 1. forsøg
print(f"Finnish! Du fik '{rigtig}' rigte, og '{forkert}' forkerte ")
print(f'Du fik {procent}% rigtige')
print("")
print(f"{glade_komentare[rand_num]}")
input("Nu kommer de forkerte (tryk enter)")
print("")
# her 
gang = 0
forsøg = 0

while len(rest_liste) > 0:
  (rigtig, forkert, rest_liste) = ikke_blandede(rest_liste)
  procent = int((rigtig / 40) * 100)
  print(f"Der er kun {rest_liste} ord tilbage")
  print("")
  forsøg = forsøg + 1

# helt slutning
print("Tillykke")
print(f"Det tog dig {forsøg} forsøg at lave 100% rigtige")
print(f"{glade_komentare[rand_num]}")

#39 38 37 36 35