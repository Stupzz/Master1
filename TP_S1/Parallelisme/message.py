class Message:
    INFO = "info"
    STOP = "stop"

    def __init__(self, type, train, accept):
        self.type = type
        self.train = train
        self.accept = accept

    def __str__(self):
        return "Message: " + self.type + ". Contient le train: " + self.train + ". La réponse est: " + self.accept + "."

