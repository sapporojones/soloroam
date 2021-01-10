from roam import __version__
from roam.ships import Atron

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

