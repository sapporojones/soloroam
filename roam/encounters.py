# template
# def a(player):
#     encounter_text = print()
#     #player.something
#     return encounter_text

# imports
from roam.ships import SoloSabre

##0
def cit(player):
    encounter_text = print(
        f"\nYour corporation has access to a dockable structure in this system.  "
        + "\n\nYou imaptiently repair your damage there before embarking.  "
        + "\n\nYour score increases by 20."
    )
    player.structure_rep
    player.score_change(20)
    return encounter_text


##1
def wreck(player):
    encounter_text = print(
        f"\nYou notice wrecks from a fight that haven't been looted yet.  "
        + "\nYour score increased by 50."
    )
    player.score_change(50)
    return encounter_text


##2
def sabre(player):
    encounter_text = print(
        f"\nYou observe a single sabre on field with you.  "
        + "\n\nThere are no other hostiles there with you.  "
        + "\n\nNoticing many other hostiles in local you perform a 360 degree directional scan.  You see many other hostiles. "
        + "\n\nYou are outmatched by a destroyer class vessel and the Sabre has friends so you atteempt to run.  "
        + "\n\nWhile successful, you take 20 damage.  "
        + "\n\nYour score has been increased by 40."
    )
    player.take_damage(20)
    player.score_change(40)
    return encounter_text


##4
def sappo(player):
    encounter_text = print(
        f"\nLooking at the local list you notice Sapporo Jones in system.  You make a subaru joke, he notices, laughs at the joke, and wishes you well.  "
        + "\n\nYour score has increased by 50."
    )
    player.score_change(50)
    return encounter_text


##4
def newbro(player):
    encounter_text = print(
        f"\nAs chat loads you notice a newbro asking a newbro question.  "
        + "\n\nYou answer it for him and after verifying he has only played the game for a week toss him 10m ISK.  "
        + "\n\nYour score has increased by 100.  Newbros are excellent.  Always be nice to them."
    )
    player.score_change(100)
    return encounter_text


##5
def bloc(player):
    encounter_text = print(
        f"Out of nowhere a large nullsec alliance fleet begins loading in to this solar system.  "
        + "\n\nAs you watch their movement on your directional scanner you notice they are here to shoot a hostile structure.  "
        + "\n\nYou decide it is best to leave them alone.  Your score increases by 20."
    )
    player.score_change(20)
    return encounter_text


##6
def distracted(player):
    encounter_text = print(
        f"Your attention slips to something happening around your computer.  You hear an alert as your shields take damage.  "
        + "\n\nAs your heart skips several beats in excitement you realize it is just NPC pirates on a gate.  "
        + "\n\nYou warp off but not before taking 30 damage.  "
        + "\n\nYour score increases by 30."
    )
    player.score_change(30)
    player.take_damage(30)
    return encounter_text


##7
def cm(player):
    encounter_text = print(
        f"Your corp pings for you to attend a corp meeting you completely forgot about.  "
        + "\n\nYou warp to the sun and hop on comms and listen to the meeting.  "
        + "\n\nYou gain appreciation for your corp CEO and fellow corp mates.  "
        + "\n\nYour score increases by 50."
    )
    player.score_change(50)
    return encounter_text


##8
def sb(player):
    encounter_text = print(
        f"As you warp around the system you pass close to a stargate with a smartbombing Machariel class battleship.  "
        + "\n\nWhile it does not kill you, you do take damage from it.  "
        + "\n\nYou take 20 damage.  Learning from the mistake increases your score by 30."
    )
    player.score_change(30)
    player.take_damage(20)
    return encounter_text


##9
def tidi(player):
    encounter_text = print(
        f"You notice everything going super slow.  Looking in the upper left of your screen you notice the Time Dilation indicator.  "
        + "\n\nDoing stuff here is going to be lame.  You make plans to leave for an adjacent solar system. "
        + "\n\nYour score goes up by 30 for dealing with soul crashing lag."
    )
    player.score_change(30)
    return encounter_text
