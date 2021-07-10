from random import seed
from random import randint

loot = ["explo loot", "rat poop", "faction mods", "deadspace mods", "officer mods"]


def randomloot():
    npc_loot = "nothing"
    randvalue = randint(1, 999)
    if randvalue <= 200:
        npc_loot = loot[0]
    elif randvalue <= 550:
        npc_loot = loot[1]
    elif randvalue <= 850:
        npc_loot = loot[2]
    elif randvalue <= 950:
        npc_loot = loot[3]
    elif randvalue <= 990:
        npc_loot = loot[4]

    return npc_loot


def valueofLoot(myloot):
    score = 0
    if myloot == loot[0] or myloot == loot[1]:
        score = 50
    elif myloot == loot[2]:
        score = 100
    elif myloot == loot[3]:
        score = 500
    elif myloot == loot[4]:
        score = 1000
    return score
