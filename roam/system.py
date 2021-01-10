from os import system, name
import sqlite3
import requests
import json

database = r"sqlite-latest.sqlite"
conn = sqlite3.connect(database)
cur = conn.cursor()


def clear_screen():
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def current_status(player):
    for item in player.cargo:
        print(f"Your cargohold contains {item}")
    print(f"Your current location is {player.location}")
    print(f"Your ship has {player.hp} hp remaining")
    print(f"Your ship has {player.ammo} ammo remaining")
    print(f"Your ship has {player.nanite} nanite repair paste remaining")
    return

def find_system_from_id(id):
    cur.execute("SELECT solarSystemName FROM mapSolarSystems WHERE solarSystemID=?", (id,))
    system_name = cur.fetchone()
    return system_name

def find_id_from_system(name):
    cur.execute("SELECT solarSystemID FROM mapSolarSystems WHERE solarSystemName=?", (name,))
    system_id = cur.fetchone()
    return system_id

def route_control():
    route_list = []
    origin = 'D-PNP9'
    desti = 'C9N-CC'
    ori_id = find_id_from_system(origin)[0]
    dst_id = find_id_from_system(desti)[0]
    formed_route_url = f"https://esi.evetech.net/latest/route/{ori_id}/{dst_id}/?datasource=tranquility&flag=shortest"
    rsp_list = requests.get(formed_route_url)
    rsp_list_json = rsp_list.json()
    for x in rsp_list_json:
        route_list.append(find_system_from_id(x)[0])
    return route_list
