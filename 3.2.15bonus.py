class BankAccount:
    def __init__(self, kontoinhaber, ueberziehungsrahmen=-100.0):
        self.kontoinhaber = kontoinhaber 
        self.kontostand = 0.0
        self.ueberziehungsrahmen = ueberziehungsrahmen

    def einzahlen(self, betrag):
        if betrag > 0:
            self.kontostand += betrag
            print(f"{betrag:.2f} € wurden eingezahlt.")
        else:
            print("Einzahlungbetrag muss höher sein.")
    
    def abheben(self, betrag): 
        if betrag <= 0:
            print("Abhebungsbetrag muss kleiner sein.")
        elif self.kontostand - betrag < self.ueberziehungsrahmen:
            print("Abhebung abgelehnt: Überziehungsrahmen überschritten.")
        else:
            self.kontostand -= betrag 
            print(f"{betrag:.2f} € wurden abgehoben.")

    def zeige_kontostand(self):
        print(f"Aktueller Kontostand von {self.kontoinhaber}: {self.kontostand:.2f} €")

    def zinsen_berechnen(self, zinssatz):
        if self.kontostand > 0:
            zinsen = self.kontostand * (zinssatz / 100)
            self.kontostand += zinsen
            print(f"Zinsen von {zinsen:.2f} € wurden dem Konto hinzugefügt.")
        else: 
            print("Keine Zinsen, da der Kontostand nicht gedeckt ist.")

    def __str__(self):
        return f"Konto von {self.kontoinhaber} - Kontostand: {self.kontostand:.2f} €" 
    
konto = BankAccount("Ryou Hikari")
print(konto)
konto.einzahlen(1000)
konto.abheben(500)
konto.abheben(50)
konto.zinsen_berechnen(5)
print(konto) 
