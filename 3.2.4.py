# BMI Rechner 
gewicht = float(input("Gib dein Gewicht in kg ein: "))
groesse = float(input("Gib deine Größe in Metern ein (z. B. 1.75): "))

bmi = gewicht / (groesse ** 2)
print(f"Dein BMI ist: {bmi:.2f}")

if bmi < 18.5:
    print("Untergewicht")
elif 18.5 <= bmi < 25:
    print("Normalgewicht")
elif 25 <= bmi < 30:
    print("Übergewicht")
else:
    print("Starkes Übergewicht")
    

# Ampel 
 farbe = input("Gib die Ampelfarbe ein (rot, gelb, grün): ").lower()

if farbe == "rot":
    print("🚫 Stehen bleiben!")
elif farbe == "gelb":
    print("⚠️ Bereit machen.")
elif farbe == "grün":
    print("✅ Gehen!")
else:
    print("Ungültige Eingabe. Bitte rot, gelb oder grün eingeben.")  


# Rabattrechner 
einkaufswert = float(input("Gib den Einkaufswert in Euro ein: "))

if einkaufswert > 100:
    rabatt = einkaufswert * 0.10
    endpreis = einkaufswert - rabatt
    print(f"Du bekommst 10 % Rabatt. Endpreis: {endpreis:.2f} €")
else:
    print(f"Kein Rabatt. Endpreis: {einkaufswert:.2f} €")


# Zahl zwischen zwei anderen 
a = float(input("Erste Zahl: "))
b = float(input("Zweite Zahl: "))
c = float(input("Dritte Zahl: "))

if (a < b < c) or (c < b < a):
    print("Die zweite Zahl liegt zwischen der ersten und der dritten.")
else:
    print("Die zweite Zahl liegt NICHT zwischen der ersten und der dritten.")#


# Schaltjahr 
jahr = int(input("Gib ein Jahr ein: "))

if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
    print(f"{jahr} ist ein Schaltjahr.")
else:
    print(f"{jahr} ist kein Schaltjahr.")


# Größte Zahl finden 
a = float(input("Gib die erste Zahl ein: "))
b = float(input("Gib die zweite Zahl ein: "))
c = float(input("Gib die dritte Zahl ein: "))

groesste = a

if b > groesste:
    groesste = b
if c > groesste:
    groesste = c

print(f"Die größte Zahl ist: {groesste}")


# Schulnoten 
note = int(input("Gib eine Schulnote von 1 bis 6 ein: "))

if note == 1:
    print("Sehr gut")
elif note == 2:
    print("Gut")
elif note == 3:
    print("Befriedigend")
elif note == 4:
    print("Ausreichend")
elif note == 5:
    print("Mangelhaft")
elif note == 6:
    print("Ungenügend")
else:
    print("Ungültige Eingabe. Bitte Zahl von 1 bis 6 eingeben.")


# Passwortabfrage
passwort = input("Bitte Passwort eingeben: ")

if passwort == "geheim":
    print("Zugriff erlaubt.")
else:
    print("Falsches Passwort!")

# Positiv oder negativ
zahl = float(input("Gib eine Zahl ein: "))

if zahl > 0:
    print("Die Zahl ist positiv.")
elif zahl < 0:
    print("Die Zahl ist negativ.")
else:
    print("Die Zahl ist null.")

# Gerade oder ungerade Zahl
zahl = int(input("Gib eine ganze Zahl ein: "))

if zahl % 2 == 0:
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")