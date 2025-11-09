
class Article:
    def __init__(self, reference: str, designation: str, prix_ht: float, stock: int):
        self.reference = reference
        self.designation = designation
        self.prix_ht = prix_ht
        self.stock = stock

    def valeur_stock(self) -> float:
        """Calcule la valeur du stock de cet article."""
        return self.prix_ht * self.stock

    def __str__(self) -> str:
        """Représentation lisible de l’article."""
        return f"Réf {self.reference} — {self.designation} : {self.stock} unités à {self.prix_ht:.2f} € HT"

    # --- Extension facultative ---
    def approvisionner(self, qte: int):
        """Augmente le stock et écrit l’opération dans un fichier journal."""
        if qte > 0:
            self.stock += qte
            with open("mouvements.log", "a", encoding="utf-8") as f:
                f.write(f"Approvisionnement de {qte} unités pour {self.designation} (Réf {self.reference})\n")
        else:
            print("Quantité invalide (doit être > 0)")
