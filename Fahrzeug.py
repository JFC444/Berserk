# Fahrzeug-Eigenschaften als Variablen
farbe = "blau"
größe = "groß"
anzahl_tueren = "3 Türen"
kraftstoff = "Diesel"
fahrzeugtyp = "Lkw"

# Weitere eigene Eigenschaften
baujahr = 2022
marke = "Mercedes"
kennzeichen = "B-AB1234"
gewicht = "3.5 Tonnen"
zustand = "gebraucht"

# Ausgabe aller Variablen
print("Fahrzeugdaten:")
print("Farbe:", farbe)
print("Größe:", größe)
print("Anzahl Türen:", anzahl_tueren)
print("Kraftstoff:", kraftstoff)
print("Fahrzeugtyp:", fahrzeugtyp)
print("Baujahr:", baujahr)
print("Marke:", marke)
print("Kennzeichen:", kennzeichen)
print("Gewicht:", gewicht)
print("Zustand:", zustand)

# Beispiel: Werte zwischen zwei Variablen tauschen
print("\nTausche Farbe und Zustand...")

temp = farbe
farbe = zustand
zustand = temp

# Ausgabe nach dem Tausch
print("Neue Farbe:", farbe)
print("Neuer Zustand:", zustand)