class Message:
    ARRIVAGE_TRAIN = "arrivage train"
    SORTI_TRAIN = "sorti train"
    GARE_VIDE = "gare vide"
    ENTREE_TRAIN = "entree train"

    ATTENTE_TRAIN = "attente train"

    def __init__(self, type, train):
        self.type = type
        self.train = train


