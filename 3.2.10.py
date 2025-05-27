summe = 0

for zahl in range(1, 101):  # 101, weil die Obergrenze ausgeschlossen ist
    if zahl % 2 == 0:       # Wenn die Zahl gerade ist
        summe += zahl

print("Die Summe aller geraden Zahlen von 1 bis 100 ist:", summe)