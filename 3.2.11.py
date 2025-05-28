zahlen = []
print("Gib Zahlen ein (oder 'stop' zum Beenden):")

# === Eingaben sammeln mit while-Schleife ===
while True:
    eingabe = input("Zahl eingeben: ")

    if eingabe.lower() == "stop":
        break

    if eingabe.lstrip("-").isdigit():  # Erlaubt auch negative Zahlen
        zahlen.append(int(eingabe))
    else:
        print("Ungültige Eingabe! Bitte gib eine ganze Zahl ein oder 'stop'.")

# === Überprüfung: Wurden überhaupt Zahlen eingegeben? ===
if len(zahlen) == 0:
    print("Es wurden keine Zahlen eingegeben.")
else:
    # Mit for-Schleife: Minimum, Maximum, Summe
    kleinste = zahlen[0]
    groesste = zahlen[0]
    summe = 0

    for zahl in zahlen:
        if zahl < kleinste:
            kleinste = zahl
        if zahl > groesste:
            groesste = zahl
        summe += zahl

    durchschnitt = round(summe / len(zahlen), 2)  # Durchschnitt mit 2 Nachkommastellen

    # Liste sortieren
    sortierte_liste = sorted(zahlen)

    # === Ausgabe ===
    print("\n--- Auswertung ---")
    print("Eingegebene Zahlen:", zahlen)
    print("Sortierte Zahlen:  ", sortierte_liste)
    print("Kleinste Zahl:", kleinste)
    print("Größte Zahl:", groesste)
    print("Durchschnitt:", durchschnitt)