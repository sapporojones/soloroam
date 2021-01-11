from os import system, name
import sqlite3
import requests
import json
from random import randint


database = r"sqlite-latest.sqlite"
conn = sqlite3.connect(database)
cur = conn.cursor()


def clear_screen():
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def current_status(player):
    for item in player.cargo:
        print(f"Your cargohold contains {item}")
    print(f"Your current location is {player.location}")
    print(f"Your ship has {player.hp} hp remaining")
    print(f"Your ship has {player.ammo} ammo remaining")
    print(f"Your ship has {player.nanite} nanite repair paste remaining")
    return


def find_system_from_id(id):
    cur.execute(
        "SELECT solarSystemName FROM mapSolarSystems WHERE solarSystemID=?", (id,)
    )
    system_name = cur.fetchone()
    return system_name


def find_id_from_system(name):
    cur.execute(
        "SELECT solarSystemID FROM mapSolarSystems WHERE solarSystemName=?", (name,)
    )
    system_id = cur.fetchone()
    return system_id


def route_control():
    route_list = []
    origin = "D-PNP9"
    desti = "C9N-CC"
    ori_id = find_id_from_system(origin)[0]
    dst_id = find_id_from_system(desti)[0]
    formed_route_url = f"https://esi.evetech.net/latest/route/{ori_id}/{dst_id}/?datasource=tranquility&flag=shortest"
    rsp_list = requests.get(formed_route_url)
    rsp_list_json = rsp_list.json()
    for x in rsp_list_json:
        route_list.append(find_system_from_id(x)[0])
    return route_list


def get_position_in_route(route_list, loc):
    list_pos = 0
    i = 0
    for x in route_list:
        if x == loc:
            list_pos = i
        i += 1
    return list_pos


def npc_swarm_spawn():
    n_spawn = randint(1, 4)
    rat_array = []
    for n in range(n_spawn):
        rat_spawn_member = Rat(30)
        rat_array.append(rat_spawn_member)
    return rat_array


def status_message(route_list, pilot, rat_array):
    movement_options = []
    return_listicle = []
    cur_pos = pilot.location
    cur_list_pos = get_position_in_route(route_list, cur_pos)
    if cur_list_pos == 0:
        movement_options.append(route_list[1])
    elif cur_list_pos == route_list[-1]:
        movement_options.append(route_list[(cur_list_pos - 1)])
    else:
        movement_options.append(route_list[(cur_list_pos - 1)])
        movement_options.append(route_list[(cur_list_pos + 1)])

    if rat_array == 0:
        rat_string = "\nThere are 0 rats on field with you"
    else:
        rat_string = f"\nThere are {len(rat_array)} rats on field with you"
    pilot_string = f"\nYou have {pilot.hp} hp, {pilot.ammo} ammo, {pilot.nanite} paste, and are currently in {pilot.location}."

    # compile to list format
    return_listicle.append(rat_string)
    return_listicle.append(pilot_string)
    return return_listicle


def movement_options(route_list, pilot):
    movement_options = []
    cur_pos = pilot.location
    cur_list_pos = get_position_in_route(route_list, cur_pos)
    if cur_list_pos == 0:
        movement_options.append(route_list[1])
    elif cur_list_pos == route_list[-1]:
        movement_options.append(route_list[(cur_list_pos - 1)])
    else:
        movement_options.append(route_list[(cur_list_pos - 1)])
        movement_options.append(route_list[(cur_list_pos + 1)])
    return movement_options


def parse_input(player_action, movement_options, player):
    if player_action.upper() == "RAT":
        choice = "rat"
    else:
        choice = "You spin your ship."
    for x in movement_options:
        if x == player_action.upper():
            player.location = x
            choice = "move"
    return choice
