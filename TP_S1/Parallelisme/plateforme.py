from patron import Patron
from message import Message
from time import sleep


class Plateforme(Patron):

    def __init__(self, context, nb_trains):
        super(Plateforme, self).__init__('Plateforme', context)
        self.nb_max_trains = int(nb_trains)
        self.trains = []

    def run(self):
        while self.attente_msg():
            pass

    def attente_msg(self):
        msg = self.child.recv()

        if msg.type == Message.SORTI_TRAIN:
            for train in self.trains:
                if str(train.id) == str(msg.train.id):
                    self.envoie_message('Operateur', Message(Message.DEMANDE_SORTI, msg.train, None))
                    break

        elif msg.type == Message.SORT_TRAIN:
            for train in self.trains:
                if str(train.id) == str(msg.train.id):
                    self.trains.remove(train)
                    break

        elif msg.type == Message.DEMANDE_ENTREE:
            if len(self.trains) < self.nb_max_trains:
                self.envoie_message('Operateur', Message(Message.REPONSE_ENTREE, None, True))
                self.trains.append(msg.train)
                print(str(msg.train) + ' Le train est accepter en gare')
            else:
                self.envoie_message('Operateur', Message(Message.REPONSE_ENTREE, None, False))

        elif msg.type == Message.PRINT_TRAINS:
            for train in self.trains:
                print(train)

        elif msg.type == Message.VIDE_GARE:
            for train in self.trains:
                self.envoie_message('Operateur', Message(Message.DEMANDE_SORTI, train, None))

        elif msg.type == Message.STOP:
            return False

        return True
