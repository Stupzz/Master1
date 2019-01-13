from time import sleep
from patron import Patron
from message import Message
from threading import Thread
from plateforme import Plateforme
from multiprocessing import Pipe
from train import Train
from operateur import Operateur
from actor import Actor


if __name__ == '__main__':
    context = dict()

    parts = [Operateur, Plateforme]
    objs_parts = []
    actor = Actor(context)

    for p in parts:
        objs_parts += [p(context)]

    for p in objs_parts:
        p.launch()

    actor.run()

    for p in objs_parts:
        p.join()