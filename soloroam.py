"""
Solo Roam Text Adventure Game main python script
by Sapporo Jones
"""

# library imports - stdlib
from time import sleep
from random import randint

# library imports - external
# import requests


# local imports
from roam.ships import Atron
# from roam.ships import Rat
import roam.words as w
import roam.system as system

origin_system = "Innia"
destination_system = "Kedama"

unilist = ["D-PNP9", "G-YZUX", "A1-AUH", "Q0OH-V", "X-7BIX", "C9N-CC"]


# eventually we'll do argument based routing or some sort of input but for now I am a living god


def main(player):
    """This is the main event loop for the game.
    As long as the player is alive (player.hp >= 0)
    the game is running this loop.

    Args:
        player ([class]): [this represents the player's ship]
    """
    saved_score = 0
    rat_array = ["reset"]
    current_fight = ""
    while player.hp >= 1:

        system.clear_screen()
        if player.location == route_list[0]:
            pass
        else:
            rat_array = []
            rat_chance = randint(1, 100)
            if rat_chance >= 50:
                rat_array = system.npc_swarm_spawn()
            else:
                # must reset here, or a sub 50 roll crashes with no rat_array found
                rat_array = ["reset"]
                pass
        if player.location == current_fight:
            rat_array = ["reset"]
        else:
            pass

        # encounter spawn gotta go somewhere how bout here
        system.encounter_chance(player)

        status_array = system.status_message(route_list, player, rat_array)
        print(f"{status_array[0]}\n{status_array[1]}")

        movement_options = system.movement_options(route_list, player)
        print("\nAdjacent systems to your current location are:")
        for movement_option in movement_options:
            print(movement_option)
        if len(movement_options) == 1:
            print(
                f"\nWhat is your decision? \n\nAvailable commands are {movement_options[0]}, "
                + "or type 'rat' to shoot rats."
            )
        else:
            print(
                f"\nWhat is your decision? \n\nAvailable commands are {movement_options[0]}, "
                + f"{movement_options[1]} or type 'rat' to shoot rats."
            )
        try:
            player_action = str(input())
        except ValueError:
            print("You spin your ship.")

        action = system.parse_input(player_action, movement_options, player)
        # print(rat_array)
        if action.lower() == "rat":
            if rat_array[0] != "reset":
                # print('fightin')
                system.rat_fight(rat_array, player)
                # system.clear_screen()
                try:
                    for rat_item in rat_array:
                        rat_array[rat_item].remove()
                    rat_array = ["reset"]
                    current_fight = player.location
                except:
                    rat_array = ["reset"]
                    current_fight = player.location

        if player.location == destination_system:
            print(
                f"\n\nCongratulations, you have arrived at {player.location}.  "
                + "\nYou may now set a new destination, or dock up and use your points you've gained to reship.  "
                + "\nOr you may choose to either hold onto your points, in which case they might be lost on death "
                + "or save them to buy bigger and better ships"
                + "\no7 capsuleer the system is clear. "
                + f"\n\nYour final score from this trip was {player.score}")
            saved_score += player.score

    if (player.hp < 1):
        print(
            f"\n\nYour ship explodes in to tiny pieces at the stargate in {player.location}.  "
            + "\nYour capsule containing your body shatters from the force of the explosion.  "
            + "\nYou are dead.  You wake up in your hangar where your death clone is set to and "
            + "prepare to voyage out once again.  "
            + "\no7 capsuleer the cyno is now lit. "
            + f"\n\nYour final score was {player.score}"
        )


if __name__ == "__main__":
    print("Building route and setting up game...")
    route_list = system.route_control(origin_system, destination_system)
    # route_list = unilist
    player = Atron(100, route_list[0])
    system.clear_screen()
    w.starting_text()
    print(player.location)
    sleep(5)
    main(player)
