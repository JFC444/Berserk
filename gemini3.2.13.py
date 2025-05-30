import sys # Wird für sys.exit() verwendet, um das Programm ordentlich zu beenden

def celsius_zu_fahrenheit(celsius):
    """
    Wandelt eine Temperatur von Celsius in Fahrenheit um.
    Formel: F = C * 9/5 + 32
    """
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def fahrenheit_zu_celsius(fahrenheit):
    """
    Wandelt eine Temperatur von Fahrenheit in Celsius um.
    Formel: C = (F - 32) * 5/9
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def drucke_trennlinie(zeichen='=', laenge=50):
    """Gibt eine dekorative Trennlinie aus."""
    print(zeichen * laenge)

def main():
    """Hauptfunktion des Temperaturumrechners."""

    drucke_trennlinie('-')
    print("✨ Herzlich willkommen zum Temperaturumrechner! ✨".center(50))
    drucke_trennlinie('-')

    while True:
        print("\nBitte wählen Sie eine Umwandlungsrichtung:")
        print("1. Celsius nach Fahrenheit")
        print("2. Fahrenheit nach Celsius")
        print("3. Programm beenden")
        drucke_trennlinie()

        wahl = input("Ihre Wahl (1, 2 oder 3): ").strip() # .strip() entfernt Leerzeichen am Anfang/Ende

        if wahl == '3':
            print("\nVielen Dank für die Nutzung des Temperaturumrechners! Auf Wiedersehen! 👋")
            drucke_trennlinie('-')
            sys.exit() # Beendet das Programm sauber

        elif wahl in ('1', '2'):
            try:
                temperatur_eingabe = input("Bitte geben Sie die Temperatur ein: ")
                temperatur_wert = float(temperatur_eingabe.replace(',', '.')) # Ersetzt Komma durch Punkt für float Umwandlung

                if wahl == '1':
                    ergebnis = celsius_zu_fahrenheit(temperatur_wert)
                    print(f"\nDas Ergebnis ist: {temperatur_wert}°C = {ergebnis:.2f}°F")
                else: # wahl == '2'
                    ergebnis = fahrenheit_zu_celsius(temperatur_wert)
                    print(f"\nDas Ergebnis ist: {temperatur_wert}°F = {ergebnis:.2f}°C")

                drucke_trennlinie('=')

            except ValueError:
                print("\n❗ Ungültige Eingabe! Bitte geben Sie eine gültige Zahl für die Temperatur ein.")
                drucke_trennlinie('x', 30)
            except Exception as e:
                print(f"\nEin unerwarteter Fehler ist aufgetreten: {e}")
                drucke_trennlinie('!', 30)

        else:
            print("\n❌ Ungültige Auswahl! Bitte geben Sie '1', '2' oder '3' ein.")
            drucke_trennlinie('x', 30)

# Stellt sicher, dass die main-Funktion nur aufgerufen wird,
# wenn das Skript direkt ausgeführt wird.
if __name__ == "__main__":
    main()
