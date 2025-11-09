
class CompteurPage:
    # Attribut de classe : partagé entre toutes les instances
    total_visites = 0

    def __init__(self, url: str):
        # Attribut d’instance : propre à chaque objet
        self.url = url
        self.visites_par_page = 0  # extension
        # À chaque création d’objet, on incrémente le compteur global
        CompteurPage.total_visites += 1

    def afficher_stats(self) -> str:
        """Retourne une phrase avec l'URL et le total des visites globales."""
        return f"Page {self.url} — visites globales : {CompteurPage.total_visites}"

    def enregistrer_lecture(self):
        """Incrémente le nombre de visites pour cette page spécifique."""
        self.visites_par_page += 1

    def afficher_lectures(self) -> str:
        """Affiche le nombre de lectures pour cette page uniquement."""
        return f"Page {self.url} — lectures individuelles : {self.visites_par_page}"
