
from math import pi

class Cercle:
    def __init__(self, rayon: float):
        self._rayon = None  # on initialise l’attribut privé
        self.rayon = rayon  # utilise la propriété pour valider la valeur

    @property
    def rayon(self) -> float:
        """Retourne le rayon du cercle."""
        return self._rayon

    @rayon.setter
    def rayon(self, valeur: float):
        """Contrôle que le rayon est positif."""
        if valeur <= 0:
            raise ValueError("Le rayon doit être supérieur à zéro.")
        self._rayon = valeur

    @property
    def perimetre(self) -> float:
        """Calcule le périmètre à la demande."""
        return 2 * pi * self._rayon

    @property
    def surface(self) -> float:
        """Calcule la surface à la demande."""
        return pi * self._rayon ** 2

    def agrandir(self, pourcentage: float):
        """Augmente le rayon de pourcentage %."""
        if pourcentage < 0:
            raise ValueError("Le pourcentage doit être positif.")
        self._rayon *= (1 + pourcentage / 100)
