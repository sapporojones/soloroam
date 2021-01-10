"""
Solo Roam Text Adventure Game main python script
by Sapporo Jones
"""

#library mports
from time import sleep
import sqlite3
import requests


#local imports
from roam.ships import Atron
import roam.words as w
import roam.system as system
import json
#TODO: Get SDE and create connection strings to use it here
database = r"sqlite-latest.sqlite"
conn = sqlite3.connect(database)
cur = conn.cursor()





unilist = ['D-PNP9', 'G-YZUX','A1-AUH', 'Q0OH-V', 'X-7BIX', 'C9N-CC']

#eventually we'll do argument based routing or some sort of input but for now I am a living god





def main(player):
    w.starting_text()
    print(player.location)
    sleep(5)
    system.clear_screen()
    system.current_status(player)
    
if __name__ == "__main__":
    route_list = system.route_control()
    player = Atron("player", 100, 100, 100, route_list[0])

    main(player)