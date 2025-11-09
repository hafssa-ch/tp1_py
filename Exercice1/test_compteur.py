
from compteur_page import CompteurPage

# Création de trois pages différentes
p1 = CompteurPage("https://example.com/")
p2 = CompteurPage("https://example.com/blog")
p3 = CompteurPage("https://example.com/contact")

# Vérification du compteur global
for p in (p1, p2, p3):
    print(p.afficher_stats())

# total_visites devrait être 3
print("Total global :", CompteurPage.total_visites)

# --- Extension : enregistrement de lectures individuelles ---
p1.enregistrer_lecture()
p1.enregistrer_lecture()
p2.enregistrer_lecture()

print(p1.afficher_lectures())  # 2 lectures
print(p2.afficher_lectures())  # 1 lecture
print(p3.afficher_lectures())  # 0 lecture
