"""
Solo Roam Text Adventure Game main python script
by Sapporo Jones
"""

#library mports
from time import sleep

#local imports
from roam.ships import Atron
import roam.words as w
import roam.system as system

#TODO: Get SDE and create connection strings to use it here






unilist = ['D-PNP9', 'G-YZUX','A1-AUH', 'Q0OH-V', 'X-7BIX', 'C9N-CC']

def main(player):
    w.starting_text()
    print(player.location)
    sleep(5)
    system.clear_screen()
    system.current_status(player)

if __name__ == "__main__":
    player = Atron("player", 100, 100, 100, unilist[0])

    main(player)