# Classe avec valeur en dur
class Player1:
    pseudo = "Vincent"
    health = 20
    attack = 3


class Player:
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
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
        damage = self.attack
        if self.has_weapon():
            damage += self.weapon.get_damage_amount()

        target_player.damage(damage)

    def set_weapon(self, weapon):
        self.weapon = weapon

    def has_weapon(self):
        return self.weapon is not None
