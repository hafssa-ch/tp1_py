
from datetime import datetime

class JournalTaches:
    def __init__(self, fichier: str = "journal.txt"):
        self.fichier = fichier
        self._f = None  # Fichier ouvert en mode append

    def __enter__(self):
        """Ouverture du fichier en mode append."""
        self._f = open(self.fichier, "a", encoding="utf-8")
        return self

    def enregistrer(self, tache: str):
        """Écrit la tâche avec horodatage ISO."""
        if self._f is None:
            raise RuntimeError("Le fichier n’est pas ouvert.")
        timestamp = datetime.now().isoformat()
        self._f.write(f"{timestamp} — {tache}\n")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Fermeture du fichier."""
        if self._f:
            self._f.close()
            self._f = None

    # --- Extension : lecture inverse ---
    def lire(self):
        """Affiche le journal dans l’ordre inverse (dernière tâche en premier)."""
        try:
            with open(self.fichier, "r", encoding="utf-8") as f:
                lignes = f.readlines()
            for ligne in reversed(lignes):
                print(ligne.strip())
        except FileNotFoundError:
            print("Le fichier de journal est vide ou n’existe pas.")
