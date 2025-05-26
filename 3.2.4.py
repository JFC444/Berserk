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