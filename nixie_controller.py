from gpiozero import OutputDevice


class NixieController:
    def __init__(self, initial_value, pin_1, pin_2, pin_3, pin_4):
        self.pins = [OutputDevice(pin_1), OutputDevice(pin_2), OutputDevice(pin_3), OutputDevice(pin_4)]
        self.pin_states = [False, False, False, False]
        self._value = initial_value
        self.value = initial_value
        self.on = False

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        for n in range(4):
            self.pin_states[n] = new_value & (2 ** n) != 0
        self._value = new_value

    def refresh_pins(self):
        for n in range(4):
            self.pins[n].value = self.pin_states[n]

    def turn_on(self):
        self.refresh_pins()
        self.on = True

    def turn_off(self):
        for pin in self.pins:
            pin.value = True
        self.on = False
