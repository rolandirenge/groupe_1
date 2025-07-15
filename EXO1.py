"""Énoncé.1. :
Créer un programme qui demande le prénom, l’âge, la ville et le métier d’un utilisateur, puis
affiche un mini profil structuré.
Ensuite, ajouter une conversion d'âge en nombre de jours vécus (approximation). """
prenom = input("Entrez votre prénom : ")
age = int(input("Entrez votre âge : "))
ville = input("Entrez votre ville : ")
metier = input("Entrez votre métier : ")

jours_vecus = age * 365
print("\n== PROFIL UTILISATEUR ==")
print(f"Prénom : {prenom}")
print(f"Âge : {age} ans ({jours_vecus} jours vécus environ)")
print(f"Ville : {ville}")
print(f"Métier : {metier}")

