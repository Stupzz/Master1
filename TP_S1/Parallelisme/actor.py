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
        print("Commands: ajout, retrait, ajout_multiple, clear_gare, print_gare, stop?")
        command = input()

        if command == 'retrait':
            self.envoie_message('Plateforme', Message(Message.PRINT_TRAINS, None, None))
            print('Quel train souhaitez vous retirer de la gare? Sélectionnez le avec l\'id')
            id_train = int(input())
            self.envoie_message('Plateforme', Message(Message.SORTI_TRAIN, Train(id_train), None))

        elif command == 'ajout':
            train = Train(input('Quel id voulez vous pour votre train?'))
            self.envoie_message('Operateur', Message(Message.ENTREE_TRAIN, train, None))

        elif command == 'ajout_multiple':
            nb_train = int(input('Combien de train voulez vous ajoutez?'))
            ind_mini = int(input('A quel indice voulez vous commencer?'))
            for i in range (ind_mini, ind_mini+nb_train):
                train = Train(i)
                self.envoie_message('Operateur', Message(Message.ENTREE_TRAIN, train, None))

        elif command == 'clear_gare':
            self.envoie_message('Plateforme', Message(Message.VIDE_GARE, None, None))

        elif command == 'print_gare':
            self.envoie_message('Plateforme', Message(Message.PRINT_TRAINS, None, None))

        elif command == 'stop':
            message = Message(Message.STOP, None, None)
            self.envoie_message('Operateur', message)
            self.envoie_message('Plateforme', message)
            self.envoie_message('Transit', message)
            return False

        return True
