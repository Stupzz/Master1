from patron import Patron
from message import Message
from mq_sender import MQ_sender
from mq_reiceiver import MQ_receiver

class Plateforme(Patron):
    FULL = "full"
    NOT_FULL = "not_full"


    def __init__(self, context, voies):
        super(Plateforme, self).__init__('Plateforme', context, voies)
        self.etat = Plateforme.NOT_FULL
        self.nb_train = 0
        self.voies = voies
        self.mq_sender = MQ_sender('localhost')

    def run(self):
        def ajout_train():
            self.nb_train += 1
            if self.voies == self.nb_train:
                self.etat = Plateforme.FULL

        def retire_train():
            self.nb_train -= 1
            if self.voies != self.nb_train and self.etat != Plateforme.NOT_FULL:
                self.etat = Plateforme.NOT_FULL

        def gestion_message(message):
            if message == Message.ARRIVAGE_TRAIN:
                if self.etat == Plateforme.NOT_FULL:
                    ajout_train()
                    self.mq_sender.publish(Message.ARRIVAGE_TRAIN, "operateur")
                else:
                    self.mq_sender.publish(self.name + ": " + Message.ATTENTE_TRAIN, "operateur")
            else:
                if self.nb_train != 0:
                    retire_train()
                    self.mq_sender.publish(Message.SORTI_TRAIN, "operateur")
                else:
                    self.mq_sender.publish(Message.GARE_VIDE, "operateur")

            mq_receiver = MQ_receiver('localhost', 'platforme', gestion_message)
            mq_receiver.start_reiceive()
