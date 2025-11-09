
from cercle import Cercle
from math import pi

c = Cercle(3)

print("Périmètre :", c.perimetre)  # 2πr
print("Surface   :", c.surface)    # πr²

# Test de la sécurité du setter
try:
    c.rayon = -5
except ValueError as e:
    print("Erreur capturée :", e)

# Test de l’agrandissement
c.agrandir(50)  # +50%
print("\nAprès agrandissement de 50% :")
print("Nouveau rayon   :", c.rayon)
print("Nouveau périmètre :", c.perimetre)
print("Nouvelle surface   :", c.surface)
