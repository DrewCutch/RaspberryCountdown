class NixieDisplay:

    def __init__(self, controllers, initial_value=0):
        self.controllers = controllers
        self._value = initial_value
        self.value = initial_value
        self.on = False

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        temp = new_value
        if new_value > 10 ** len(self.controllers) - 1 or new_value < 0:
            temp = new_value = 0
        for i in range(len(self.controllers)):
            self.controllers[i].value = temp % 10
            temp //= 10
        self._value = new_value

    def turn_on(self):
        for controller in self.controllers:
            controller.turn_on()

    def turn_off(self):
        for controller in self.controllers:
            controller.turn_off()
