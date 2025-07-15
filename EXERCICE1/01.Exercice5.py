# Calcul de vitesse moyenne
distance_km = float(input("Distance (km) : "))
temps_h = float(input("Temps (heures) : "))

vitesse_kmh = distance_km / temps_h
vitesse_ms = (distance_km * 1000) / (temps_h * 3600)

print(f"\nVitesse moyenne : {vitesse_kmh:.2f} km/h")
print(f"Vitesse moyenne : {vitesse_ms:.2f} m/s")
while True:
    try:
        print("\n--- Calcul de vitesse ---")
        distance = float(input("Distance parcourue (km) : "))
        temps = float(input("Temps écoulé (heures) : "))

        if distance <= 0 or temps <= 0:
            print("Erreur : Les valeurs doivent être positives")
            continue

        kmh = distance / temps
        ms = (distance * 1000) / (temps * 3600)

        print(f"\nRésultats :")
        print(f"- {kmh:.2f} km/h")
        print(f"- {ms:.2f} m/s")
        break

    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides")