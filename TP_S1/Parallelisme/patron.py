import multiprocessing

class Patron:
    def __init__(self, name):
        self.name = name
        self.process = multiprocessing.Process(target=self.run)
        self.parent_pipe, self.child_pipe = multiprocessing.Pipe()

    def print(self, msg):
        print(self.name + " " + msg)

    def start(self):
        self.process.start()

    def join(self):
        self.process.join()

    def run(self):
        raise NotImplementedError