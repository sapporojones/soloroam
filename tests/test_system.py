#System library tests

from os import system, name
import sqlite3
# import json
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from random import randint
import requests
import roam.system as s
from roam.ships import Atron
from roam.ships import Rat
import roam.encounters as e


#functions to create data used by functions in system library
def player_create():
    player = Atron(100, route_list[0])
    return player

def route_init():
    route_list = ["D-PNP9", "G-YZUX", "A1-AUH", "Q0OH-V", "X-7BIX", "C9N-CC"]
    return route_list




#current_status function is used for status text 
#this appears to be an unused funciton in system
#adding test coverage for it anyways

def test_current_status():
    player = player_create()
    route_list = route_init()
    status_text = s.current_status(player)
    assert len(status_text) >= 0



#test function to determine system name from id
#to test this function requires an active internet connection
def test_find_system_from_id_online():
    id = 30003135
    system_name = s.find_system_from_id_online(id)
    assert system_name == 'D-PNP9'

#to test this function requires an active internet connection
def test_find_id_from_system():
    name = 'd-pnp9'
    system_id = s.find_id_from_system(name)
    assert system_id = 30003135


#to test this function requires an active internet connection
def test_route_control():
    origin_system = 'D-PNP9'
    destination_system = 'C9N-CC'
    route_list = s.route_control(origin_system, destination_system)
    assert route_list[2] == 'A1-AUH'

#to test this function requires an active internet connection
def test_get_position_in_route():
    route_list = route_init()
    player = player_create()
    player.location = 'A1-AUH'
    loc = player.location
    route_index = s.get_position_in_route(route_list, loc)

    assert route_index == 2


def test_npc_swarm_spawn():
    rat_array = s.npc_swarm_spawn()
    assert rat_array >= 2



def test_movement_options(route_list, player):
    route_list = route_init()
    player = player_create()
    player.location = route_list[2]

    movement_options = []
    movement_options = s.movement_options(route_list, player)
    assert len(movement_options) == 2



def test_rat_fight():
    rat_array = s.npc_swarm_spawn()
    player = player_create()

    s.rat_fight(rat_array, player)
    assert player.hp < 100



