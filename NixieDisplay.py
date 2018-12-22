import NixieController


class NixieDisplay:

    def __init__(self, num_controllers, initial_value=0):
        self.controllers = [NixieController() for n in range(num_controllers)]
        self._value = initial_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        digits = map(int, new_value)
        if len(digits) != len(self.controllers):
            raise ValueError("Value has too many digits to be displayed by controllers")
        for i in range(len(digits)):
            self.controllers[i].value = digits[i]
        self._value = new_value
