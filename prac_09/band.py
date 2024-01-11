"""Band example with list of musicians."""


class Band:
    def __init__(self, name):
       self.name = name
       self.musicians = []

    def __str__(self):
        return f"{self.name}({self.musicians})"

    def __repr__(self):
        return str(self)

    def play(self):
        message = ''
        for musician in self.musicians:
            message += musician.play() + '\n'
        return message

    def add(self, musician):
        self.musicians.append(musician)