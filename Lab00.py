'''Authors: Jesse-Jackson Zigi and Bright Okrah'''


'''
    This is just a brief inheritance overview with Python
    To initialize any of the classes, just pass a string 
    as an argument. Each class has an overridden get_specs()
    and display_specs() method. The get_specs() method returns
    a string while the display_specs() method prints out a string.
'''
#Inheritance practice
class Computer:
    _specs = ""

    def __init__(self, specs):
        self._specs = specs

    def get_specs(self):
        return self._specs

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


'''
You can test any of the classes this way.
'''
laptop = Laptop("3GB Ram")
laptop.display_specs()

desktop = Desktop("8GB Ram")
desktop.display_specs()