class Train:

    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return f"Train d'id: {self.id}"

    def __str__(self):
        return f"Train d'id: {self.id}"

    def __eq__(self, other):
        return other.id == self.id
