import random

# Eine zufällige Zahl zwischen 1 und 100 wählen
geheime_zahl = random.randint(1, 100)

# Zähler für die Anzahl der Versuche
versuche = 0

print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht.")
print("Kannst du sie erraten?")

# Solange der Benutzer falsch rät, wird die Schleife wiederholt
while True:
    tipp = input("Dein Tipp: ")

    # Eingabe prüfen und in eine Zahl umwandeln
    if not tipp.isdigit():
        print("Bitte gib eine gültige Zahl ein.")
        continue

    tipp = int(tipp)
    versuche += 1

    if tipp < geheime_zahl:
        print("Zu niedrig!")
    elif tipp > geheime_zahl:
        print("Zu hoch!")
    else:
        print(f"Richtig! Du hast die Zahl nach {versuche} Versuchen erraten.")
        break