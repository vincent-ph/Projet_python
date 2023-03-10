import datetime

class Commande:
    def __init__(self, date, number, price):
        self.date = date
        self.number = number
        self.price = price

    def __str__(self):
        return "Date: {}\nNuméro: {}\nPrix: {}".format(self.date, self.number, self.price)

    # getter
    def get_date(self):
        return self.date

    def get_number(self):
        return self.number

    def get_price(self):
        return self.price

    # setter
    def set_date(self, date):
        self.date = date

    def set_number(self, number):
        self.number = number

    def set_price(self, price):
        self.date = price

    # methode
    def calcultva(self):
        return self.price + self.price * (19.6/100)

    def __add__(self, commande):
        if self.number > commande.number:
            new_number = self.number + 1
            new_date = self.date
            new_price = self.price + commande.price
        else:
            new_number = commande.number + 1
            new_date = commande.date
            new_price = self.price + commande.price
        return Commande(new_date, new_number, new_price)

    def acquitter(self):
        return CommandeAcquittee(self.date, self.number, self.price, datetime.date.today())


class CommandeAcquittee(Commande):
    def __init__(self, date, number, price, payment_date):
        super().__init__(date, number, price)
        self.payment_date = payment_date

    def __str__(self):
        return "Date: {}\nNuméro: {}\nPrix: {}\nDate Acquittée: {}".format(self.date, self.number, self.price, self.payment_date)




    def hauteur(self):
        if self.estVide():
            return -1
        else:
            if self.left is not None:
                hauteur_left = self.left.hauteur()
            else:
                return 0
            if self.right is not None:
                hauteur_right = self.right.hauteur()
            else:
                return 0
            return 1 + max(hauteur_left, hauteur_right)