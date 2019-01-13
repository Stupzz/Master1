from time import sleep
from patron import Patron
from message import Message


class Actor(Patron):
    def __init__(self, context):
        super(Actor, self).__init__('Actor', context)

    def run(self):
        while self.command():
            sleep(0.2)

    def command(self):
        print("Commands: send, badge, enter, leave, laser, authorize, stop, fire")
        command = input('-> ')

        if command == 'send':
            msg = Message(Message.INFO, None, None)
            self.msg(input('Message target -> '), msg)

        if command == 'stop':
            return False

        return True