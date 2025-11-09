
class Convertisseur:
    # Attribut de classe : taux de conversion euro → dirham
    taux_eur_dh = 10.9

    @staticmethod
    def vers_dh(euros: float) -> float:
        """Convertit un montant en euros vers dirhams selon le taux actuel."""
        return euros * Convertisseur.taux_eur_dh

    @staticmethod
    def vers_eur(dirhams: float) -> float:
        """Convertit un montant en dirhams vers euros selon le taux actuel."""
        return dirhams / Convertisseur.taux_eur_dh

    @classmethod
    def mettre_a_jour_taux(cls, nv_taux: float):
        """Met à jour le taux de conversion pour toutes les instances."""
        cls.taux_eur_dh = nv_taux
