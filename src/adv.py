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

# items 
key = Item('Key to nowhere', '''This key does not seem to open anything in particular''')
junk = Item()
hat = Item('Hat', '''A nifty looking hat, maybe you should give it someone special''')

item_lookup = {'junk':junk, 'key':key, 'hat':hat}

room['outside'].room_items.append(junk)

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

# item['junk'].cur_room = room['outside']
# item['key'].cur_room = room['foyer']

# room['foyer'].room_items.append(item['key'])
# room['outside'].room_items.append(item['junk'])

#
# Main
#

def print_help():
    print("To move type in commands such as 'n' to move north.")
    print("To pick up items type 'get [item name]'")
    print("To drop an item type 'drop [item name]'")
    print("Type 'q' to quit.\n")

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



print(f'Welcome, {player.name}, to The Adventure Game.')
print("For instructions type 'help'\n")

print(player.cur_room)

while True:
    cmd = input("->")
    print('')
    cmd = cmd.lower()

    if cmd == 'q':
        break
    elif cmd == 'help':
        print_help()
    elif cmd in ('n', 's', 'e', 'w'):
        player.move(cmd)
    elif cmd[:3] == 'get':
        player.get_item(item_lookup[cmd[4:]])
    elif cmd[:4] == 'drop':
        player.drop_item(item_lookup[cmd[5:]])
    elif cmd == 'i':
        player.check_inv()
    else:
        print(f"I did not understand the command '{cmd}'\n")
    