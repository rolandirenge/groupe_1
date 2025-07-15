# Opérations entre deux nombres

# Version corrigée (identique à l'image avec syntaxe fixée)
a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))

somme = a + b
difference = a - b
produit = a * b
quotient = a / b if b != 0 else "Division par zéro"
division_entiere = a // b if b != 0 else "Division par zéro"
reste = a % b if b != 0 else "Division par zéro"

print(f"\nRésultats :")
print(f"Somme : {somme}")
print(f"Différence : {difference}")
print(f"Produit : {produit}")
print(f"Quotient : {quotient}")
print(f"Division entière : {division_entiere}")
print(f"Reste : {reste}")
def calcul_operations():
    try:
        print("\n--- Calculatrice ---")
        x = float(input("Premier nombre : "))
        y = float(input("Deuxième nombre : "))

        operations = {
            "Somme": x + y,
            "Différence": x - y,
            "Produit": x * y,
            "Quotient": x / y if y != 0 else "Impossible",
            "Division entière": x // y if y != 0 else "Impossible",
            "Reste": x % y if y != 0 else "Impossible"
        }

        print("\nRésultats :")
        for operation, resultat in operations.items():
            print(f"{operation} : {resultat}")

    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides")
        calcul_operations()


calcul_operations()