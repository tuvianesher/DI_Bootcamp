class Temperature:
    def __init__(self, value):
        self.value = value

    def to_celsius(self):
        pass

    def to_kelvin(self):
        pass

    def to_fahrenheit(self):
        pass


class Celsius(Temperature):
    def to_celsius(self):
        return self.value

    def to_kelvin(self):
        return self.value + 273.15

    def to_fahrenheit(self):
        return (self.value * 9/5) + 32


class Kelvin(Temperature):
    def to_celsius(self):
        return self.value - 273.15

    def to_kelvin(self):
        return self.value

    def to_fahrenheit(self):
        return (self.value - 273.15) * 9/5 + 32


class Fahrenheit(Temperature):
    def to_celsius(self):
        return (self.value - 32) * 5/9

    def to_kelvin(self):
        return (self.value - 32) * 5/9 + 273.15

    def to_fahrenheit(self):
        return self.value
