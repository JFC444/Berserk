import tkinter as tk  # language=css
from tkinter import messagebox

# BankAccount-Klasse
class BankAccount:
    def __init__(self, kontoinhaber):
        self.kontoinhaber = kontoinhaber
        self.kontostand = 0.0

    def einzahlen(self, betrag):
        if betrag > 0:
            self.kontostand += betrag
            return True
        return False

    def abheben(self, betrag):
        if betrag > self.kontostand or betrag <= 0:
            return False
        self.kontostand -= betrag
        return True

    def get_kontostand(self):
        return self.kontostand

# GUI-Klasse
class BankGUI:
    def __init__(self, master):
        self.konto = BankAccount("Max Mustermann")
        self.master = master
        master.title("🏦 Mein Bankkonto")
        master.geometry("400x300")
        master.configure(bg= "#e51955")   # heller Hintergrund

        # Kontoüberschrift
        self.label_name = tk.Label(master, text=f"Konto: {self.konto.kontoinhaber}",
                                   font=("Arial", 16, "bold"), bg="#f0f4f7")
        self.label_name.pack(pady=10)

        self.label_kontostand = tk.Label(master, text="Kontostand: 0.00 €",
                                         font=("Arial", 14), bg="#f0f4f7")
        self.label_kontostand.pack(pady=5)

        self.entry_betrag = tk.Entry(master, font=("Arial", 12), width=20)
        self.entry_betrag.pack(pady=10)

        # Button-Styles
        button_style = {
            "font": ("Arial", 12, "bold"),
            "width": 15,
            "padx": 5,
            "pady": 5
        }

        self.button_einzahlen = tk.Button(master, text="Einzahlen", bg="#8ecae6", fg="white",
                                          command=self.einzahlen, **button_style)
        self.button_einzahlen.pack(pady=3)

        self.button_abheben = tk.Button(master, text="Abheben", bg="#f4a261", fg="white",
                                        command=self.abheben, **button_style)
        self.button_abheben.pack(pady=3)

        self.button_aktualisieren = tk.Button(master, text="Kontostand anzeigen", bg="#2a9d8f", fg="white",
                                              command=self.aktualisieren, **button_style)
        self.button_aktualisieren.pack(pady=10)

    def einzahlen(self):
        try:
            betrag = float(self.entry_betrag.get())
            if self.konto.einzahlen(betrag):
                self.aktualisieren()
            else:
                messagebox.showwarning("Fehler", "Einzahlungsbetrag muss positiv sein.")
        except ValueError:
            messagebox.showerror("Fehler", "Bitte eine gültige Zahl eingeben.")

    def abheben(self):
        try:
            betrag = float(self.entry_betrag.get())
            if self.konto.abheben(betrag):
                self.aktualisieren()
            else:
                messagebox.showwarning("Fehler", "Nicht genügend Guthaben oder ungültiger Betrag.")
        except ValueError:
            messagebox.showerror("Fehler", "Bitte eine gültige Zahl eingeben.")

    def aktualisieren(self):
        kontostand = self.konto.get_kontostand()
        self.label_kontostand.config(text=f"Kontostand: {kontostand:.2f} €")

# Start
if __name__ == "__main__":
    root = tk.Tk()
    app = BankGUI(root)
    root.mainloop() 
