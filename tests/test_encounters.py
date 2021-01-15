# template
# def a(player):
#     encounter_text = print()
#     #player.something
#     return encounter_text

# imports
from roam.ships import SoloSabre
from roam.ships import Atron
import roam.encounters as e
from roam.loot import *

#functions to create data used by functions in system library
def player_create():
    route_list = route_init()
    player = Atron(100, route_list[0])
    return player

def route_init():
    route_list = ["D-PNP9", "G-YZUX", "A1-AUH", "Q0OH-V", "X-7BIX", "C9N-CC"]
    return route_list

##0
def test_cit():
    player = player_create()
    e.cit(player)
    assert player.score > 0


##1
#def test_wreck():
#    player = player_create()
#    e.wreck(player)
#    assert player.score > 0


##2
def test_sabre():
    player = player_create()
    e.sabre(player)
    assert player.hp == 80


##4
def test_sappo():
    player = player_create()
    e.sappo(player)
    assert player.score == 50


##4
def test_newbro():
    player = player_create()
    e.newbro(player)
    assert player.score == 100


##5
def test_bloc():
    player = player_create()
    e.bloc(player)
    assert player.score == 20


##6
def test_distracted():
    player = player_create()
    e.distracted(player)
    assert player.hp == 70


##7
def test_cm():
    player = player_create()
    e.cm(player)
    assert player.score == 50


##8
def test_sb():
    player = player_create()
    e.sb(player)
    assert player.hp == 80


##9
def test_tidi():
    player = player_create()
    e.tidi(player)
    assert player.score == 30
