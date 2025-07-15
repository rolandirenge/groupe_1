# Conversion durée en secondes
heures = int(input("Nombre d'heures : "))
minutes = int(input("Nombre de minutes : "))
secondes = int(input("Nombre de secondes : "))
total_secondes = heures * 3600 + minutes * 60 + secondes
print(f"\nDurée totale : {total_secondes} secondes")
try:
    heures = max(0, int(input("\nNombre d'heures : ")))
    minutes = max(0, min(59, int(input("Nombre de minutes : "))))
    secondes = max(0, min(59, int(input("Nombre de secondes : "))))

    total = heures * 3600 + minutes * 60 + secondes
    print(f"\nConversion : {heures}h {minutes}m {secondes}s = {total} secondes")

except ValueError:
    print("Erreur : Veuillez entrer des nombres entiers valides")