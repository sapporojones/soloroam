from os import system, name
import sqlite3
# import json
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from random import randint
import requests

from roam.ships import Rat
import roam.encounters as e


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


# def find_system_from_id(id):
#     cur.execute(
#         "SELECT solarSystemName FROM mapSolarSystems WHERE solarSystemID=?", (id,)
#     )
#     system_name = cur.fetchone()
#     return system_name


def find_id_from_system(name):
    url_string = f'https://esi.evetech.net/latest/search/?categories=solar_system&datasource=tranquility&language=en-us&search={name}&strict=true'
    id_request = requests.get(url_string)
    id_request_json = id_request.json()
    system_id = id_request_json["solar_system"]
    return system_id


def find_system_from_id_online(id):
    url_string = f'https://esi.evetech.net/latest/universe/systems/{id}/?datasource=tranquility&language=en-us'
    id_request = requests.get(url_string)
    id_request_json = id_request.json()
    system_name = id_request_json["name"]
    return system_name


def route_control(origin_system, destination_system):
    route_list = []
    ori_id = find_id_from_system(origin_system)[0]
    dst_id = find_id_from_system(destination_system)[0]
    formed_route_url = f"https://esi.evetech.net/latest/route/{ori_id}/{dst_id}/?datasource=tranquility&flag=shortest"
    rsp_list = requests.get(formed_route_url)
    rsp_list_json = rsp_list.json()
    with ThreadPoolExecutor(max_workers = 10) as executor:
        future_result = executor.map(find_system_from_id_online, rsp_list_json)
        for future in future_result:
            route_list.append(future)
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
    n_spawn = randint(2, 4)
    rat_array = []
    for n in range(n_spawn):
        rat_array.append(Rat(30))
    return rat_array


def status_message(route_list, pilot, rat_array):
    movement_options = []
    return_listicle = []
    if len(rat_array) == 1:
        rat_string = "\nThere are 0 rats on field with you"
    else:
        rat_string = f"\nThere are {len(rat_array)} rats on field with you"
    pilot_string = f"\nYou have {pilot.hp} hp, and are currently in {pilot.location}.  Current score is {pilot.score}."

    # compile to list format
    return_listicle.append(rat_string)
    return_listicle.append(pilot_string)
    return return_listicle


def movement_options(route_list, player):
    movement_options = []
    cur_pos = player.location
    cur_list_pos = get_position_in_route(route_list, cur_pos)
    last_system = route_list[-1]
    if cur_list_pos == 0:
        movement_options.append(route_list[1])
    elif cur_pos == last_system:
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


def rat_fight(rat_array, player):
    while len(rat_array) > 0:
        rat_array[-1].take_damage(10)
        player.take_damage(5)
        if rat_array[-1].hp <= 0:
            rat_array.remove(rat_array[-1])
            player.score_change(20)
        else:
            pass
    return


def encounter_chance(player):
    encounter_chance = randint(1, 100)
    if encounter_chance >= 50:
        event_generator(player)
    else:
        pass
    return


def event_generator(player):
    # list of encounters, for now must be manually updated.  When you add to encounters.py add function name here.
    # don't forget to increase the max number in randint or additions won't be called
    encounter_list = [
        e.cit,
        e.sabre,
        e.sappo,
        e.newbro,
        e.wreck,
        e.bloc,
        e.distracted,
        e.sb,
        e.cm,
        e.tidi,
    ]
    selection = randint(0, 9)
    encounter_list[selection](player)
    return
