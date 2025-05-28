zahlen_liste = []

# Schleife zur Sammlung der Benutzereingaben
while True:
    eingabe = input("Bitte geben Sie eine Zahl ein oder 'stop' zum Beenden: ")

    if eingabe.lower() == 'stop':
        break  # Beendet die Schleife, wenn 'stop' eingegeben wird
    else:
        try:
            zahl = int(eingabe)  # Versucht, die Eingabe in einen Integer umzuwandeln
            zahlen_liste.append(zahl)  # Fügt die Zahl zur Liste hinzu
        except ValueError:
            print("Ungültige Eingabe! Bitte geben Sie eine ganze Zahl oder 'stop' ein.")

# Überprüfen, ob Zahlen eingegeben wurden, bevor Berechnungen durchgeführt werden
if not zahlen_liste:
    print("Es wurden keine Zahlen eingegeben.")
else:
    # Initialisierung für die Suche nach Minimum und Maximum
    # Wir nehmen an, die erste Zahl ist zunächst das Minimum und Maximum
    kleinste_zahl = zahlen_liste[0]
    groesste_zahl = zahlen_liste[0]
    summe_der_zahlen = 0

    # For-Schleife zur Berechnung von Minimum, Maximum und Summe
    for zahl in zahlen_liste:
        if zahl < kleinste_zahl:
            kleinste_zahl = zahl
        if zahl > groesste_zahl:
            groesste_zahl = zahl
        summe_der_zahlen += zahl

    # Durchschnitt berechnen
    durchschnitt = summe_der_zahlen / len(zahlen_liste)

    # Ergebnisse ausgeben
    print(f"\nDie größte Zahl ist: {groesste_zahl}")
    print(f"Die kleinste Zahl ist: {kleinste_zahl}")
    print(f"Der Durchschnitt der Zahlen ist: {durchschnitt:.2f}") # Rundet auf zwei Nachkommastellen

    # Liste sortieren und ausgeben
    zahlen_liste.sort() # Sortiert die Liste aufsteigend
    print(f"Die sortierte Liste ist: {zahlen_liste}")