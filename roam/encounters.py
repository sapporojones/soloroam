# template
# def a(player):
#     encounter_text = print()
#     #player.something
#     return encounter_text

# imports
from time import sleep
from roam.loot import randomloot, valueofLoot


##0
def cit(player):
    print(
        f"\nYour corporation has access to a dockable structure in this system.  "
        + "\n\nYou imaptiently repair your damage there before embarking.  "
        + "\n\nYour score increases by 20.")
    player.structure_rep
    player.score_change(20)
    return


##1
def wreck(player):
    loot_found = randomloot()
    value = valueofLoot(loot_found)
    print(
        f"\nYou notice wrecks from a fight that haven't been looted yet.  "
        + f"\nYou have looted {loot_found} and your score has increased by {value}"
    )
    player.score_change(value)
    return


##2
def sabre(player):
    print(
        f"\nYou observe a single sabre on field with you.  "
        + "\n\nThere are no other hostiles there with you.  "
        + "\n\nSeeing many hostiles in local you perform a 360 degree directional scan and see a hostile fleet."
        + "\n\nYou are outmatched by a destroyer class vessel and the Sabre has friends so you atteempt to run.  "
        + "\n\nWhile successful, you take 20 damage.  "
        + "\n\nYour score has been increased by 40."
    )
    player.take_damage(20)
    player.score_change(40)
    return


##4
def sappo(player):
    print(
        f"\nLooking at the local list you notice Sapporo Jones in system.  "
        + "You make a subaru joke, he notices, laughs at the joke, and wishes you well.  "
        + "\n\nYour score has increased by 50."
    )
    player.score_change(50)
    return


##4
def newbro(player):
    print(
        f"\nAs chat loads you notice a newbro asking a newbro question.  "
        + "\n\nYou answer it for him and after verifying he has only played the game for a week toss him 10m ISK.  "
        + "\n\nYour score has increased by 100.  Newbros are excellent.  Always be nice to them."
    )
    player.score_change(100)
    return


##5
def bloc(player):
    print(
        f"Out of nowhere a large nullsec alliance fleet begins loading in to this solar system.  "
        + "\n\nAs you watch their movement on your directional scanner you notice they are here to shoot a structure.  "
        + "\n\nYou decide it is best to leave them alone.  Your score increases by 20."
    )
    player.score_change(20)
    return


##6
def distracted(player):
    print(
        f"Your attention slips to something happening around your computer.  "
        + "You hear an alert as your shields take damage.  "
        + "\n\nAs your heart skips several beats in excitement you realize it is just NPC pirates on a gate.  "
        + "\n\nYou warp off but not before taking 30 damage.  "
        + "\n\nYour score increases by 30."
    )
    player.score_change(30)
    player.take_damage(30)
    return


##7
def cm(player):
    print(
        f"Your corp pings for you to attend a corp meeting you completely forgot about.  "
        + "\n\nYou warp to the sun and hop on comms and listen to the meeting.  "
        + "\n\nYou gain appreciation for your corp CEO and fellow corp mates.  "
        + "\n\nYour score increases by 50."
    )
    player.score_change(50)
    return


##8
def sb(player):
    print(
        f"As you warp around the system you pass close to a stargate with a smartbombing Machariel class battleship.  "
        + "\n\nWhile it does not kill you, you do take damage from it.  "
        + "\n\nYou take 20 damage.  Learning from the mistake increases your score by 30."
    )
    player.score_change(30)
    player.take_damage(20)
    return


##9
def tidi(player):
    print(
        f"You notice everything going super slow.  "
        + "In the upper left of your screen you notice the Time Dilation indicator.  "
        + "\n\nDoing stuff here is going to be lame.  You make plans to leave for an adjacent solar system. "
        + "\n\nYour score goes up by 30 for dealing with soul crashing lag."
    )
    player.score_change(30)
    return


##10
def rookie_ships(player):
    print(
        f"Your overview expands rapidly with hostiles.  You sort by ship class and realize what's happening..  "
        + f"\n\nIt's a newbro rookie ship roam.  Roughly 20 new players in their free corvettes swarm the gate grid.  "
        + "\n\nAs soon as you break cloak they are upon you.  You exchange shots, they do damage, most die."
        + "\n\nAs their numbers dwindle they extract.  You have no way to prevent this and the fight is basically over."
        + "\n\nYou say good fight in local and toss the fleet commander some money for his effort helping newbros."
        + "\n\nBecause rookie ships do not do that much damage you will now sit for 5 seconds while you experience "
        + "\ntaking damage from rookie ships.  Also you take 10 damage.  Thrill to the immersion.  You loot the field."
    )
    loot_found = randomloot()
    value = valueofLoot(loot_found)
    sleep(5)
    player.take_damage(10)
    player.score_change(value)
    return


#11
def burst_jam(player):
    print(
        "You encounter an errant command destroyer using an entosis module on a Territorial Claim Unit. You feel cheeky"
        + "\nso you warp over to engage the hostile. As you engage an Ares class Interceptor lands next to you and hits"
        + "\nthe ECM Burst.  You lose your lock on the hostile and begin taking damage without dealing any.  You notice"
        + "\nyou aren't warp scrambled so you decide to bail.  You take 20 damage and your score increases by 50."
    )
    player.take_damage(20)
    player.score_change(50)
    return


#12
def dread_rat(player):
    print(
        "You warp to an asteroid anomaly believing a player to be there.  When you land there, there is no player."
        + "\nThere is, however, an NPC Dreadnought.  You decide to engage it.  "
        + "\n\nAs it is a capital vessel and you are piloting a frigate, time passes with little damage done.  Soon"
        + "\nothers land and engage the Dreadnought with you.  Shortly thereafter the Dreadnought explodes.  You loot"
        + "\nquickly and then leave.  "
    )
    loot_found = randomloot()
    value = valueofLoot(loot_found)
    sleep(5)
    player.take_damage(10)
    player.score_change(value)
    return


#13
def spooky(player):
    print(
        "Your map indicates activity in this system.  When you jump in you see warp disruption bubbles everywhere.  "
        + "\nYou see wrecks, abandoned drones, but no signs of players.  You check your directional scanner but see no")
    sleep(3)
    print(
        "\nresults.  After 45 seconds the interdiction bubbles despawn.  "
        + "\n\nYour score increases by 30."
    )
    player.score_change(30)
    return


#14
def cyno(player):
    print(
        "You see a lit cynosural field on your overview 19AU from your current position.  Unable to see what is"
        + "\nhappening or on field that far away you decide to investigate.  You warp to the cyno, it's a long warp..."
    )
    sleep(3)
    print(
        "You land next to a Venture class industrial frigate.  There are no other ships present.  You quickly destroy"
        + "\nthe helpless frigate.  You loot the field and gon on about your business.  "
    )
    loot_found = randomloot()
    value = valueofLoot(loot_found)
    player.score_change(value)
    return


#15
def argument(player):
    print(
        "As you jump in to system you notice two people arguing in local chat."
    )
    choice = input("Would you like to say something to them?\n")
    if choice == 'yes':
        print(
            "As the argument between the two players reaches a dramatic crescendo you decide to contribute to their "
            + "\ndiscussion.  "
            + "\n\nYou patiently wait for a break in the argument and as soon as it arrives you drop your wisdom."
            + "\n\n\"ur gay pwnd\""

        )

    else:
        print(
            "\n\nYou continue on about your business."
        )

    return
