from model.Commande import Commande
from model.Client import Client

commande = Commande("10/01/23", 123, 100)
commande2 = Commande("11/01/23", 124, 1)
print(commande)
commande.set_date("01/01/23")
commande.set_number(1)
commande.set_price(10)
print("Date:", commande.get_date(), "Numero:", commande.get_number(), "Prix:", commande.get_price())

client = Client("Vincent", "15 rue de Paris")
print(client)
client.set_name("Paul")
client.set_address("1 avenue de Paris")
print("Nom:", client.get_name(), "Adresse:", client.get_address())
print("Prix avec TVA:", commande.calcultva())
client.contacter()

commande3 = commande + commande2
print(commande3)
commande3acquittee = commande3.acquitter()
print(commande3acquittee)