#library to handle stuff about your ship

##########################
#necessary imports go here
##########################



##################################
#Inaugural frigate class - Atron
##################################

#a ship needs to have certain stats
#it needs a pilot (usually the player) it needs a quantity of ammo as a limited resource,
#it needs nanite as a limited resource, and naturally hp as a limited resource
#the pilot needs to be alterable so that if we need to assign an 'npc' we can reuse the class
class Atron:
    def __init__(self, pilot, ammo, nanite, hp, location):
        self.pilot = pilot
        self.ammo = ammo
        self.nanite = nanite
        self.hp = hp
        self.cargo = []
        self.location = location

    def add_cargo(self, items):
        self.cargo.append(items)

    def fire_guns(self):
        self.ammo -= 1

    def use_nanite(self):
        self.nanite -= 1

    def take_damage(self, damage):
        self.hp -= damage

    def change_location(self, location):
        self.location = location
