# === Funktionen ===

def celsius_zu_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_zu_celsius(f):
    return (f - 32) * 5/9

# === Begrüßung ===
print("🌡️ Willkommen beim Temperatur-Umrechner 🌡️")
print("------------------------------------------")

# === Hauptschleife ===
while True:
    print("\nWas möchtest du tun?")
    print("1 - Celsius in Fahrenheit umrechnen")
    print("2 - Fahrenheit in Celsius umrechnen")
    print("0 - Programm beenden")

    auswahl = input("Deine Auswahl: ")

    if auswahl == "0":
        print("👋 Programm beendet. Auf Wiedersehen!")
        break

    elif auswahl == "1":
        eingabe = input("Gib die Temperatur in °C ein: ")
        try:
            celsius = float(eingabe)
            fahrenheit = celsius_zu_fahrenheit(celsius)
            print(f"{celsius} °C sind {round(fahrenheit, 2)} °F")
        except ValueError:
            print("❌ Ungültige Eingabe! Bitte gib eine Zahl ein.")

    elif auswahl == "2":
        eingabe = input("Gib die Temperatur in °F ein: ")
        try:
            fahrenheit = float(eingabe)
            celsius = fahrenheit_zu_celsius(fahrenheit)
            print(f"{fahrenheit} °F sind {round(celsius, 2)} °C")
        except ValueError:
            print("❌ Ungültige Eingabe! Bitte gib eine Zahl ein.")

    else:
        print("⚠️ Ungültige Auswahl! Bitte wähle 1, 2 oder 0.")
