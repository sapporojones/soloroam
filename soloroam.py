"""
Solo Roam Text Adventure Game main python script
by Sapporo Jones
"""

# library mports
from time import sleep
import sqlite3
import requests


# local imports
from roam.ships import Atron
import roam.words as w
import roam.system as system
import json

# sqlite db connect stuff for eve SDE, assume it is in the directory we are running this script
database = r"sqlite-latest.sqlite"
conn = sqlite3.connect(database)
cur = conn.cursor()


unilist = ["D-PNP9", "G-YZUX", "A1-AUH", "Q0OH-V", "X-7BIX", "C9N-CC"]

# eventually we'll do argument based routing or some sort of input but for now I am a living god


def main(player):
    rat_array = 0
    while player.hp >= 1:
        #system.clear_screen()
        status_array = system.status_message(route_list, player, rat_array)
        print(status_array[0])
        print(status_array[1])
        movement_options = system.movement_options(route_list, player)
        print("\nYour movement options are:")
        for x in movement_options:
            print(x)
        print(
            "What is your decision? \n\n Enter a system name from the list to move, or type rat to shoot rats."
        )
        try:
            player_action = str(input())
        except ValueError:
            print("You spin your ship.")

        action = system.parse_input(player_action, movement_options, player)
        #print(action)
        #print(player.location)
        #break



if __name__ == "__main__":
    route_list = system.route_control()
    player = Atron("player", 100, 100, 100, route_list[0])
    w.starting_text()
    print(player.location)
    #sleep(5)
    main(player)
