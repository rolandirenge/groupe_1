montant_ht = float(input("Montant HT (€) : "))
taux_tva = float(input("Taux de TVA (%) : "))

taux_coef = taux_tva / 100
montant_ttc = montant_ht * (1 + taux_coef)

print(f"Montant TTC : {montant_ttc:.2f} €")