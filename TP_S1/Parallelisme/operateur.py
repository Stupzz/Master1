from time import sleep

from patron import Patron
from message import Message



class Operateur(Patron):

    def __init__(self, context):
        super(Operateur, self).__init__('Operateur', context)
        self.trains_en_sorti = []
        self.trains_en_entree = []
        self.en_transit = False

    def run(self):
        while self.attente_msg():
            pass

    def attente_msg(self):
        msg = self.child.recv()

        if msg.type == Message.INFO:
            print("Je suis dans l'operator")
            self.envoie_message('plateforme', Message(Message.INFO, None, None))

        elif msg.type == Message.STOP:
            return False

        return True
