class Train:
    EN_TRANSIT = "en_transit"
    EN_ATTENTE = "en_attente"
    SUR_RESEAU = "sur_reseau"
    EN_GARE = "en_gare"

    def __init__(self, id):
        self.id = id

    def demande_entrer(self):
        pass

    def demande_sorti(self):
        pass


    def __repr__(self):
        return f"Train: {self.name}. D'id: {self.id}"
