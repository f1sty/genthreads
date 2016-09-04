from multiprocessing import Process


class Actor(Process):
    def __init__(self):
        super(Actor, self).__init__()
        self._inbox = list()

    def send(self, value):
        self._inbox.append(value)

    @property
    def inbox(self):
        return self._inbox
