# from player import Player, Player1 sans fichier model
from Classe.model.player import Player, Player1
from Classe.model.weapon import Weapon

knife = Weapon("Couteau", 3)
player1 = Player1()
print("Bienvenue au joueur", player1.pseudo)
player2 = Player1()
print("Bienvenue au joueur", player2.pseudo)


player3 = Player("Bob", 11, 5)
player3.set_weapon(knife)
# print(player3.get_pseudo())
# player3.damage(2)
# print("Vous avez", player3.get_health(), "points de vie")
player4 = Player("Graven", 10, 3)
player3.attack_player(player4)
print("Bienvenue au joueur", player4.pseudo, "\nPoints de vie:", player4.health, "\nPoints d'attaque:", player4.attack)
