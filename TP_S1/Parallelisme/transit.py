from patron import Patron
from message import Message
from time import sleep


class Transit(Patron):

    def __init__(self, context):
        super(Transit, self).__init__('Transit', context)

    def run(self):
        while self.attente_msg():
            pass

    def attente_msg(self):
        msg = self.child.recv()

        if msg.type == Message.START_TRANSIT:
            print(str(msg.train) + ' entre en transit')
            sleep(2)
            #print(str(msg.train) + ' sort du transit')
            self.envoie_message('Operateur', Message(Message.FIN_TRANSIT, None, None))

        elif msg.type == Message.STOP:
            return False

        return True
