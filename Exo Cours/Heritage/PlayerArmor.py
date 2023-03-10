# methode sans constructeur
class Player:
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print("Bienvenue au joueur", pseudo, "\nPoints de vie:", health, "\nPoints d'attaque:", attack)

    # getter
    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def damage(self, damage):
        self.health -= damage
        print("Aie... vous venez de subir", damage, "dégâts !")

    def attack_player(self, target_player):
        target_player.damage(self.attack)


class Warrior(Player):
    def __init__(self, pseudo, health, attack):
        super().__init__(pseudo, health, attack)
        self.armor = 3
        print("Bienvenue au guerrier", pseudo, "\nPoints de vie:", health, "\nPoints d'attaque:", attack)

    def damage(self, damage):
        if self.armor > 0:
            self.armor -= 1
            damage = 0
        super().damage(damage)

    def blade(self):
        self.armor = 3
        print("Les points d'armures sont rechargés")

    def get_armor_point(self):
        return self.armor


player = Player("Graven", 10, 3)
player.damage(3)

warrior = Warrior("DarkWarrior", 30, 4)
warrior.damage(4)
print("vie:", warrior.get_health(), "armure:", warrior.get_armor_point())
warrior.damage(4)
print("vie:", warrior.get_health(), "armure:", warrior.get_armor_point())
warrior.damage(4)
print("vie:", warrior.get_health(), "armure:", warrior.get_armor_point())
warrior.damage(4)
print("vie:", warrior.get_health(), "armure:", warrior.get_armor_point())
if issubclass(Warrior, Player):
    print("Bien hérité")
