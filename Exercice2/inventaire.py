
from article import Article

# Création de quelques articles
a1 = Article("A001", "Clavier mécanique", 79.90, 10)
a2 = Article("A002", "Souris sans fil", 39.50, 25)
a3 = Article("A003", "Écran 24 pouces", 149.00, 8)

# Liste d’articles
articles = [a1, a2, a3]

# Affichage individuel
for a in articles:
    print(a)

# Calcul de la valeur totale de l’inventaire
total = sum(a.valeur_stock() for a in articles)
print(f"\nValeur d’inventaire : {total:.2f} €")

# --- Extension : test d’approvisionnement ---
a1.approvisionner(5)
a3.approvisionner(2)

print("\nAprès approvisionnement :")
for a in articles:
    print(a)
