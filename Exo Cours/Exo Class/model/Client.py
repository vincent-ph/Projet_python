
class Client:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return "Nom: {}\nAdresse: {}".format(self.name, self.address)

    # getter
    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    # setter
    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    # methode
    def contacter(self):
        print(self.name, self.address)