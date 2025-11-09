
from journal import JournalTaches
from time import sleep

with JournalTaches() as journal:
    journal.enregistrer("Préparer la réunion du projet X")
    sleep(1)
    journal.enregistrer("Faire la revue de code")
    sleep(1)
    journal.enregistrer("Envoyer le rapport hebdomadaire")

# Lecture inversée
print("\nHistorique du journal (dernière tâche en premier) :")
JournalTaches().lire()
