from time import sleep
from patron import Patron
from message import Message
from train import Train


class Actor(Patron):
    def __init__(self, context):
        super(Actor, self).__init__('Actor', context)

    def run(self):
        while self.command():
            sleep(0.2)

    def command(self):
        print("Commands: ajout, retrait")
        command = input('-> ')

        if command == 'retrait':
            self.envoie_message('Plateforme', Message(Message.PRINT_TRAINS, None, None))
            id_train = input('Quel train souhaitez vous retirer de la gare? Sélectionnez le avec l\'id')
            id_train = int(id_train)
            self.envoie_message('Plateforme', Message(Message.SORTI_TRAIN, Train(id_train), None))

        elif command == 'ajout':
            train = Train(input('Quel id voulez vous pour votre train?'))
            self.envoie_message('Operateur', Message(Message.ENTREE_TRAIN, train, None))

        elif command == 'stop':
            return False

        return True