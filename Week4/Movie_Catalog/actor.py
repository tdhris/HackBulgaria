class Actor:
    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return self._name

    def get_name(self):
        return self._name
