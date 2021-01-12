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
from roam.ships import Rat
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
    rat_array = ['reset']
    current_fight = ''
    while player.hp >= 1:


        system.clear_screen()
        if player.location == route_list[0]:
            pass
        else:
            rat_array.remove(rat_array[0])
            rat_array = system.npc_swarm_spawn()  

        if player.location == current_fight:
            rat_array = ['reset']
        else:
            pass           

        #always spawn rats for exploratory testing.  comment out when released.


        status_array = system.status_message(route_list, player, rat_array)
        print(f"{status_array[0]}\n{status_array[1]}")
        
        movement_options = system.movement_options(route_list, player)
        print("\nAdjacent systems to your current location are:")
        for x in movement_options:
            print(x)
        if len(movement_options) == 1:
            print(
            f"\nWhat is your decision? \n\nAvailable commands are {movement_options[0]}, or type \'rat\' to shoot rats."
            )   
        else:
            print(
            f"\nWhat is your decision? \n\nAvailable commands are {movement_options[0]}, {movement_options[1]} or type \'rat\' to shoot rats."
            )
        try:
            player_action = str(input())
        except ValueError:
            print("You spin your ship.")

        action = system.parse_input(player_action, movement_options, player)
        #print(rat_array)
        if action.lower() == 'rat':
            if rat_array[0] != 'reset':
                #print('fightin')
                system.rat_fight(rat_array, player)
                # system.clear_screen()
                try:
                    for x in rat_array:
                        rat_array[x].remove()
                    rat_array = ['reset']
                    current_fight = player.location
                except:
                    rat_array = ['reset']
                    current_fight = player.location
  

    print(f"\n\nYour ship explodes in to tiny pieces at the stargate in {player.location}.  \nYour capsule containing your body shatters from the force of the explosion.  \nYou are dead.  You wake up in your hangar where your death clone is set to and prepare to voyage out once again.  \no7 capsuleer the cyno is now lit. \n\nYour final score was {str(player.score)}")           




if __name__ == "__main__":
    # origin_system = 'D-PNP9'
    # destination_system = 'C9N-CC'
    # route_list = system.route_control(origin_system, destination_system)
    route_list = unilist
    player = Atron(100, route_list[0])
    system.clear_screen()
    w.starting_text()
    print(player.location)
    # sleep(5)
    main(player)
