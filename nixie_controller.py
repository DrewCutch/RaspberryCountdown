from gpiozero import OutputDevice


class NixieController:
    def __init__(self, initial_value, pin_1, pin_2, pin_3, pin_4):
        self._value = initial_value
        self.pins = [OutputDevice(pin_1), OutputDevice(pin_2), OutputDevice(pin_3), OutputDevice(pin_4)]
        #self.pins = [False, False, False, False]

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        for n in range(4):
            self.pins[n].value = new_value & (2 ** n) != 0
            #self.pins[n] = new_value & (2 ** n) != 0
        self._value = new_value
