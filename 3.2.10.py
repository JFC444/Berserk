summe = 0

for zahl in range(1, 101):  # 101, weil die Obergrenze ausgeschlossen ist
    if zahl % 2 == 0:       # Wenn die Zahl gerade ist
        summe += zahl

print("Die Summe aller geraden Zahlen von 1 bis 100 ist:", summe)
grenze = input("Bis zu welcher Zahl sollen die geraden Zahlen summiert werden? ")

# Prüfen, ob die Eingabe gültig ist (nur Ziffern)
if not grenze.isdigit():
    print("Bitte gib eine gültige positive Zahl ein.")
else:
    grenze = int(grenze)
    summe = 0

    for zahl in range(1, grenze + 1):
        if zahl % 2 == 0:
            summe += zahl

    print(f"Die Summe aller geraden Zahlen von 1 bis {grenze} ist: {summe}")