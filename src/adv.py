from item import Item
from room import Room
from player import Player


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

item = {
    'key': Item('Key to nowhere', '''This key does not seem to open anything in particular'''),

    'junk': Item(),

    'hat': Item('Hat', '''A nifty looking hat, maybe you should give it someone special'''),

}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Link rooms to items

item['junk'].cur_room = room['outside']
item['key'].cur_room = room['foyer']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input('Please choose a name:\n->')
player = Player(name=name, cur_room=room['outside'])
print('')
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def use_input(cmd):
    if cmd == 'north':
        if player.cur_room.n_to == None:
            print("You can't go that direction\n")
        else:
            player.cur_room = player.cur_room.n_to
    elif cmd == 'south':
        if player.cur_room.s_to == None:
            print("You can't go that direction\n")
        else:
            player.cur_room = player.cur_room.s_to
    elif cmd == 'east':
        if player.cur_room.e_to == None:
            print("You can't go that direction\n")
        else:
            player.cur_room = player.cur_room.e_to
    elif cmd == 'west':
        if player.cur_room.w_to == None:
            print("You can't go that direction\n")
        else:
            player.cur_room = player.cur_room.w_to

    elif cmd == 'help':
        print("Type in commands such as 'North' to move north.")
        print("Type 'q' to quit.\n")

    elif cmd[:3] == 'get':
        if cmd[4:] in item and item[cmd[4:]].cur_room == player.cur_room:
            player.player_items.append(item[cmd[4:]])
            print(f'{player.name} picked up the {cmd[4:]}!\n')
        else:
            print(f'{player.name} can not find {cmd[4:]} in the room.\n')

    elif cmd[:4] == 'drop':
        # if item[cmd[5:]] in player.player_items:
        if cmd[5:] in item and item[cmd[5:]] in player.player_items:
            player.player_items.remove(item[cmd[5:]])
            print(f'{player.name} dropped the {cmd[5:]}.\n')
        else:
            print(f"{player.name} does not have {cmd[5:]} in their inventory.\n")

    elif cmd == 'inv':
        print('Inventory:')
        for i in player.player_items:
            print(f'-{i.name}')
        print('')


    else:
        print(f'{player.name} did not understand that command.')
        print("Type 'help' for instructions.\n")


print(f'Welcome, {player.name}, to The Adventure Game.')
print("For instructions type 'help'\n")



while True:
    print(f'Current room: {player.cur_room.name}.\n{player.cur_room.description}\n')
    cmd = input("->")
    print('')
    cmd = cmd.lower()

    if cmd == 'q':
        break
    else:
        use_input(cmd)



