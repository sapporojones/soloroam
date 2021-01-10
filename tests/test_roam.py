from roam import __version__
from roam.ships import Atron
import roam.system as system
import sqlite3
import requests
import json


unilist = ['D-PNP9', 'G-YZUX','A1-AUH', 'Q0OH-V', 'X-7BIX', 'C9N-CC']

def test_version():
    assert __version__ == '0.1.0'

#player ship attribute testing
def test_atron_init():
    player = Atron("player", 100, 100, 100, unilist[0])
    assert player.pilot == "player"

def test_add_cargo():
    player = Atron("player", 100, 100, 100, unilist[0])
    player.add_cargo("mobile depot")
    assert player.cargo[0] == "mobile depot"

def test_take_damage():
    player = Atron("player", 100, 100, 100, unilist[0])
    player.take_damage(10)
    assert player.hp == 90

def test_player_location_change():
    player = Atron("player", 100, 100, 100, unilist[0])
    player.change_location(unilist[1])
    assert player.location == 'G-YZUX'

#db system name lookups testing
def test_id_by_name():
    DP = system.find_id_from_system('D-PNP9')
    assert DP[0] == 30003135

def test_name_by_id():
    DP = system.find_system_from_id(30003135)
    assert DP[0] == 'D-PNP9'

def test_route_list_creation():
    route_list = []
    origin = 'D-PNP9'
    desti = 'C9N-CC'
    ori_id = system.find_id_from_system(origin)[0]
    dst_id = system.find_id_from_system(desti)[0]
    formed_route_url = f"https://esi.evetech.net/latest/route/{ori_id}/{dst_id}/?datasource=tranquility&flag=shortest"
    rsp_list = requests.get(formed_route_url)
    rsp_list_json = rsp_list.json()
    for x in rsp_list_json:
        route_list.append(system.find_system_from_id(x)[0])
    assert route_list[0] == 'D-PNP9'