# Exercice 2 - Fiche produit
nom_produit = "casque Bluetooth"
prix = 100.0
stock = 35
remise = 0.15
prix_final = prix * (1 - remise)
print("\n=== FICHE PRODUIT ===")
print(f"Produit : {nom_produit}")
print(f"Prix initial : {prix} €")
print(f"Remise : {remise * 100}%")
print(f"Prix final : {prix_final:.2f} €")
print(f"Stock disponible : {stock} unités")
if stock < 10:
    print("\nATTENTION : Stock faible !")
elif stock == 0:
    print("\nRUPTURE DE STOCK")