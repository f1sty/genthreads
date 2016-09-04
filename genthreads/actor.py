from multiprocessing import Process


class InboxFullError(Exception):
    pass


class Actor(Process):
    def __init__(self, inbox_size=48):
        super(Actor, self).__init__()
        self._inbox = list()
        self._inbox_size = inbox_size

    def send(self, value):
        if len(self._inbox) < self._inbox_size:
            self._inbox.append(value)
        else:
            raise InboxFullError('no more space in inbox')

    @property
    def inbox(self):
        return self._inbox
