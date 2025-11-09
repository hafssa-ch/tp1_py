
from convertisseur import Convertisseur

montant = 100

print("Avant mise à jour :", Convertisseur.vers_dh(montant))  # 100 * 10.9 = 1090.0

# Mise à jour du taux
Convertisseur.mettre_a_jour_taux(11.2)
print("Après mise à jour  :", Convertisseur.vers_dh(montant))  # 100 * 11.2 = 1120.0

# Test de l’extension vers_eur
montant_dh = 1120
print("Conversion dirhams → euros :", Convertisseur.vers_eur(montant_dh))  # 1120 / 11.2 = 100
