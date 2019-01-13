from time import sleep

from threading import Thread
from patron import Patron
from message import Message


class Operateur(Patron):

    def __init__(self, context):
        super(Operateur, self).__init__('Operateur', context)
        self.trains_en_sortie = []
        self.trains_en_entree = []
        self.en_transit = False

    def run(self):
        while self.attente_msg():
            pass

    def attente_msg(self):
        msg = self.child.recv()

        if msg.type == Message.DEMANDE_SORTI:
            if not self.en_transit:
                self.make_transit(msg.train)
            else:
                self.trains_en_sortie.append(msg.train)

        elif msg.type == Message.REPONSE_ENTREE:
            if msg.accept:
                self.make_transit(self.trains_en_entree.pop(0))
            else:
                if len(self.trains_en_sortie) > 0:
                    train = self.trains_en_sortie.pop(0)
                    self.make_transit(train)

        elif msg.type == Message.ENTREE_TRAIN:
            self.trains_en_entree.append(msg.train)
            if not self.en_transit:
                if len(self.trains_en_entree) == 1:
                    self.envoie_message('Plateforme', Message(Message.DEMANDE_ENTREE, self.trains_en_entree[0], None))

        elif msg.type == Message.FIN_TRANSIT:
            self.en_transit = False
            if len(self.trains_en_entree) > 0:
                self.envoie_message('Plateforme', Message(Message.DEMANDE_ENTREE, self.trains_en_entree[0], None))
            elif len(self.trains_en_sortie) > 0:
                train = self.trains_en_sortie.pop(0)
                self.make_transit(train)


        elif msg.type == Message.STOP:
            return False

        return True

    def make_transit(self, train):
        self.en_transit = True
        self.envoie_message('Transit', Message(Message.START_TRANSIT, train, None))

