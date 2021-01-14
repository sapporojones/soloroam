from roam import __version__
from roam.ships import Atron
from roam.ships import Rat
import roam.system as system
import sqlite3
import requests
import json
from random import randint

unilist = ["D-PNP9", "G-YZUX", "A1-AUH", "Q0OH-V", "X-7BIX", "C9N-CC"]


def test_version():
    assert __version__ == "0.2.1"


# player ship attribute testing
def test_atron_init():
    player = Atron(100, unilist[0])
    assert player.hp == 100


def test_add_cargo():
    player = Atron(100, unilist[0])
    player.add_cargo("mobile depot")
    assert player.cargo[0] == "mobile depot"


def test_take_damage():
    player = Atron(100, unilist[0])
    player.take_damage(10)
    assert player.hp == 90


def test_player_location_change():
    player = Atron(100, unilist[0])
    player.change_location(unilist[1])
    assert player.location == "G-YZUX"


# db system name lookups testing
def test_id_by_name():
    DP = system.find_id_from_system("D-PNP9")
    assert DP[0] == 30003135


def test_name_by_id():
    DP = system.find_system_from_id(30003135)
    assert DP[0] == "D-PNP9"


# def test_route_list_creation():
#     route_list = []
#     origin = "D-PNP9"
#     desti = "C9N-CC"
#     ori_id = system.find_id_from_system(origin)[0]
#     dst_id = system.find_id_from_system(desti)[0]
#     formed_route_url = f"https://esi.evetech.net/latest/route/{ori_id}/{dst_id}/?datasource=tranquility&flag=shortest"
#     rsp_list = requests.get(formed_route_url)
#     rsp_list_json = rsp_list.json()
#     for x in rsp_list_json:
#         route_list.append(system.find_system_from_id(x)[0])
#     assert route_list[0] == "D-PNP9"


def test_get_position_in_route():
    unilist = ["D-PNP9", "G-YZUX", "A1-AUH", "Q0OH-V", "X-7BIX", "C9N-CC"]
    player_location = "A1-AUH"
    list_pos = 0
    i = 0
    for x in unilist:

        if x == player_location:
            list_pos = i
        i += 1
    assert list_pos == 2


def test_npc_swarm_spawn():
    n_spawn = randint(1, 4)
    rat_array = []
    for n in range(n_spawn):
        rat_spawn_member = Rat(30)
        rat_array.append(rat_spawn_member)
    assert rat_array[0].hp == 30


def test_status_message():
    ###test vars
    route_list = ["D-PNP9", "G-YZUX", "A1-AUH", "Q0OH-V", "X-7BIX", "C9N-CC"]
    pilot = Atron(100, route_list[0])

    n_spawn = randint(1, 4)
    rat_swarm = []
    for n in range(n_spawn):
        rat_spawn_member = Rat(30)
        rat_swarm.append(rat_spawn_member)

    ###end test vars
    movement_options = []
    return_listicle = []
    cur_pos = pilot.location
    cur_list_pos = system.get_position_in_route(route_list, cur_pos)
    if cur_list_pos == 0:
        movement_options.append(route_list[1])
    elif cur_list_pos == route_list[-1]:
        movement_options.append(route_list[(cur_list_pos - 1)])
    else:
        movement_options.append(route_list[(cur_list_pos - 1)])
        movement_options.append(route_list[(cur_list_pos + 1)])

    rat_string = f"There are {len(rat_swarm)} rats on field with you"
    pilot_string = f"You have {pilot.hp} hp, and are currently in {pilot.location}."

    # compile to list format
    return_listicle.append(rat_string)
    return_listicle.append(pilot_string)
    return_listicle.append(movement_options)
    assert len(return_listicle) == 3


def test_movement_options():
    ###test vars
    route_list = ["D-PNP9", "G-YZUX", "A1-AUH", "Q0OH-V", "X-7BIX", "C9N-CC"]
    pilot = Atron(100, route_list[2])

    n_spawn = randint(1, 4)
    rat_swarm = []
    for n in range(n_spawn):
        rat_spawn_member = Rat(30)
        rat_swarm.append(rat_spawn_member)

    ###end test vars
    movement_options = []
    cur_pos = pilot.location
    cur_list_pos = system.get_position_in_route(route_list, cur_pos)
    if cur_list_pos == 0:
        movement_options.append(route_list[1])
    elif cur_list_pos == route_list[-1]:
        movement_options.append(route_list[(cur_list_pos - 1)])
    else:
        movement_options.append(route_list[(cur_list_pos - 1)])
        movement_options.append(route_list[(cur_list_pos + 1)])
    assert len(movement_options) == 2


def test_parse_input_else():
    ###test vars
    route_list = ["D-PNP9", "G-YZUX", "A1-AUH", "Q0OH-V", "X-7BIX", "C9N-CC"]
    pilot = Atron(100, route_list[2])

    n_spawn = randint(1, 4)
    rat_swarm = []
    for n in range(n_spawn):
        rat_spawn_member = Rat(30)
        rat_swarm.append(rat_spawn_member)

    ###end test vars
    player_action = "x"
    movement_options = system.movement_options(route_list, pilot)
    if player_action.lower() == "rat":
        choice = "rat"
    elif player_action.lower() in movement_options:
        for x in movement_options:
            if player_action.lower() == x:
                choice = x
    else:
        choice = "You spin your ship."
    assert choice == "You spin your ship."


def test_parse_input_move():

    ###test vars
    route_list = ["D-PNP9", "G-YZUX", "A1-AUH", "Q0OH-V", "X-7BIX", "C9N-CC"]
    pilot = Atron(100, route_list[2])

    n_spawn = randint(1, 4)
    rat_swarm = []
    for n in range(n_spawn):
        rat_spawn_member = Rat(30)
        rat_swarm.append(rat_spawn_member)

    ###end test vars

    player_action = "G-YZUX"
    movement_options = ["G-YZUX", "A1-AUH", "Q0OH-V"]
    if player_action.upper() == "RAT":
        choice = "rat"
    else:
        choice = "You spin your ship."
    for x in movement_options:
        if x == player_action.upper():
            pilot.location = x
            choice = player_action.upper()

    assert choice == pilot.location


def test_array_of_events():
    # list of events for testing
    possible_events = ["buffer", "NullBlob", "Rat"]
    # when this goes live we'll do it programitically maybe
    random_event = randint(1, (len(possible_events) - 1))
    selected_event = possible_events[random_event]
    assert random_event != 0


def test_rat_fight():
    player = Atron(100, "D-PNP9")
    n_spawn = randint(2, 6)
    rat_array = []
    for n in range(n_spawn):
        rat_spawn_member = Rat(30)
        rat_array.append(rat_spawn_member)
    while len(rat_array) > 0:
        rat_array[-1].take_damage(10)
        player.take_damage(5)
        if rat_array[-1].hp <= 0:
            rat_array.remove(rat_array[-1])
        else:
            pass

    assert player.hp < 100
