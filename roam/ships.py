# library to handle stuff about your ship

##########################
# necessary imports go here
##########################


##################################
# Inaugural frigate class - Atron
##################################

# a ship needs to have certain stats
# it needs a pilot (usually the player) it needs a quantity of ammo as a limited resource,
# it needs nanite as a limited resource, and naturally hp as a limited resource
# the pilot needs to be alterable so that if we need to assign an 'npc' we can reuse the class
class Atron:
    def __init__(self, hp, location):
        self.hp = hp
        self.cargo = []
        self.location = location
        self.score = 0
        self.killmarks = 0

    def structure_rep(self):
        rep_amt = 100 - self.hp
        self.hp += rep_amt

    def add_cargo(self, items):
        self.cargo.append(items)

    def take_damage(self, damage):
        self.hp -= damage

    def change_location(self, location):
        self.location = location

    def score_change(self, points):
        self.score += points

    def getmarks(self, marks):
        self.score += marks


class Rat:
    def __init__(self, hp):
        self.hp = hp

    def deal_damage(self, damage):
        player.hp -= 10

    def take_damage(self, damage):
        self.hp -= damage


class NullBlob:
    def __init__(self, hp):
        self.hp = hp

    def deal_damage(self, damage):
        player.hp -= 30

    def take_damage(self, damage):
        self.hp -= damage


class SoloSabre:
    def __init__(self, hp):
        self.hp = hp

    def take_damage(self, damage):
        self.hp -= damage
