class NixieController:
    def __init__(self, initial_value):
        self._value = initial_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
