class BankAccount:
    def __init__(self, kontoinhaber):
        self.kontoinhaber = kontoinhaber
        self.kontostand = 0.0

    def einzahlen(self, betrag):
        if betrag > 0:
            self.kontostand += betrag 
            print(f"{betrag:.2f} € wurden eingezahlt.")
        else:     
            print("Einzahlung muss höher sein.")
    
    def abheben(self, betrag):
        if betrag > self.kontostand:
            print("Das Konto ist nicht genügend gedeckt.")
        elif betrag <= 0:
            print("Abhebungsbetrag darf nicht minus sein.")
        else:
            self.kontostand -= betrag
            print(f"{betrag:.2f} € wurden abgehoben.")

    def zeige_kontostand(self):
        print(f"Aktueller Kontostand von {self.kontoinhaber}: {self.kontostand:.2f} €")   

konto = BankAccount("Guts Berserker")
konto.einzahlen(500)
konto.abheben(200)
konto.abheben(50) 
