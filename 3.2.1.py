def lese_zimmerdaten():
    print("Bitte geben Sie die folgenden Informationen zum Zimmer ein:")

    zimmer = {
        "Zimmernummer": input("Zimmernummer: "),
        "Größe (m²)": float(input("Größe in m²: ")),
        "Anzahl Fenster": int(input("Anzahl Fenster: ")),
        "Stockwerk": int(input("Stockwerk: ")),
        "Wandfarbe": input("Farbe der Wände: "),
        "Bodenbelag": input("Bodenbelag (z.B. Laminat, Teppich): t "),
        "Mietpreis (€)": float(input("Mietpreis in Euro: ")),
        "Verfügbar": input("Verfügbar (ja/nein): ").lower() == "ja",
        "Heizungstyp": input("Heizungstyp (z.B. Zentral, Etagen): "),
        "Balkon": input("Balkon vorhanden (ja/nein): ").lower() == "ja"
    }

    return zimmer


def gib_zimmerdaten_aus(zimmer):
    print("\n📋 Zimmerdaten:")
    for eigenschaft, wert in zimmer.items():
        print(f"{eigenschaft}: {wert}")


# Hauptprogramm
if __name__ == "__main__":
    zimmer = lese_zimmerdaten()
    gib_zimmerdaten_aus(zimmer)