from multiprocessing import process


class Actor(process.BaseProcess):
    def __init__(self):
        super(Actor, self).__init__()
        self._inbox = list()

    def send(self, value):
        self._inbox.append(value)

    @property
    def inbox(self):
        return self._inbox
