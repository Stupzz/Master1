import time

from patron import Patron
from message import Message
from plateforme import Plateforme
from multiprocessing import Pipe
from train import Train


class Operateur(Patron):
    ATTENTE = "attente"
    EN_TRANSIT = "en_transit"

    def __init__(self, context):
        super(Operateur, self).__init__(self)
        self.tains_en_attente = []
        self.etat =

    def run(self):
        while self.attente_msg():
            pass

    def attente_msg(self):
        msg = self.child.recv()

        if msg.type == Message.ARRIVAGE_TRAIN:
            if self.etat == Operateur.EN_TRANSIT:
                self.tains_en_attente.append(msg.train)
                self.print(f"{msg.train} est ajouté à la liste d'attente des trains car il y a déjà un train en transit")
            elif self.context['Plateforme'].etat != Plateforme.FULL:
                self.envoie_train(msg.train)

        if msg.type == Message.SORTI_TRAIN:
            self.print(f"{msg.train} sort de la gare")
            if len(self.tains_en_attente) > 1:
                train = self.tains_en_attente[0]
                del self.tains_en_attente[0]
                self.envoie_train(train)

    def envoie_train(self, train):
        self.print(f"{train} rentre en gare, il est actuellement en transit")
        self.transit(train)
        message = Message(Message.ENTREE_TRAIN, train)
        self.envoie_message('Plateforme', message)

    def transit(self, train):
        self.etat = Operateur.EN_TRANSIT
        time.sleep(2)
        self.etat = Operateur.ATTENTE

    def attente_transit(self):
        while self.etat == Operateur.EN_TRANSIT:
            pass

    def change_etat_transit(self):
        if self.etat == Operateur.EN_TRANSIT:
            self.etat = Operateur.ATTENTE
        else:
            self.etat = Operateur.EN_TRANSIT