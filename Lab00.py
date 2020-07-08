#Inheritance practice
class Computer:
    _specs = ""

    def __init__(self, specs):
        self._specs = specs

    def get_specs(self):
        return _specs

    def display_specs(self):
        print("Specs:{0}".format(self._specs))



class Laptop(Computer):
    def get_specs(self):
        return self._specs

    def display_specs(self):
        print("Laptop specs: {0}".format(self._specs))


class Desktop(Computer):
    def get_specs(self):
        return self._specs

    def display_specs(self):
        print("Desktop specs: {0}".format(self._specs))


laptop = Laptop("3GB Ram")
laptop.display_specs()

desktop = Desktop("8GB Ram")
desktop.display_specs()