from os import system, name



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