
from carnet import Carnet
from contact import Contact

# Création du carnet
c = Carnet()
c.ajouter(Contact("Amina Saidi", "0612345678", "amina@example.com"))
c.ajouter(Contact("Youssef Belkhou", "0699988877", "youssef@example.com"))
c.ajouter(Contact("Said Toumi", "0677001122", "said@example.com"))

# Recherche de contacts contenant "sa"
resultat = c.recherche("sa")
print("Résultat de la recherche pour 'sa' :")
for contact in resultat:
    print(contact.nom, contact.telephone)

# Affichage de tous les contacts
print("\nTous les contacts :")
c.afficher_tous()

# Nombre de contacts
print("\nNombre total de contacts :", c.nombre_contacts)
