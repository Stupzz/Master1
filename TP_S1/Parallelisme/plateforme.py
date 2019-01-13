from patron import Patron
from message import Message


class Plateforme(Patron):

    def __init__(self, context):
        super(Plateforme, self).__init__('Plateforme', context)
        self.nb_max_train = 0
        self.trains = []

    def run(self):
        while self.attente_msg():
            pass

    def attente_msg(self):
        msg = self.child.recv()

        if msg.type == Message.INFO:
            print("Je suis ici")
            print(msg)

        elif msg.type == Message.STOP:
            return False

        return True
