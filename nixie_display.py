class NixieDisplay:

    def __init__(self, controllers, initial_value=0):
        self.controllers = controllers
        self._value = initial_value
        self.value = initial_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        temp = new_value
        if new_value > 10 ** len(self.controllers) - 1:
            raise ValueError("Value has too many digits to be displayed by controllers")
        for i in range(len(self.controllers)):
            self.controllers[i].value = temp % 10
            temp //= 10
        self._value = new_value
