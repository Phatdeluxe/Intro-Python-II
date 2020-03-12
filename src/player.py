# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, cur_room):
        self.name = name
        self.cur_room = cur_room
        self.items = []

    def move(self, direction):
        if getattr(self.cur_room, f'{direction}_to'):
            self.cur_room = getattr(self.cur_room, f'{direction}_to')
            print(self.cur_room)          
        else:
            print(f'{self.name} cannot move in that direction.')

    def get_item(self, target):
        if target in self.cur_room.room_items:
            self.items.append(target)
            self.cur_room.room_items.remove(target)
            print(f'{self.name} picked up the {target.name}.\n')
        else:
            print(f'{self.name} coudld not find {target.name} in the {self.cur_room.name}.\n')

    def drop_item(self, target):            
        if target in self.items:
            self.items.remove(target)
            self.cur_room.room_items.append(target)
            print(f'{self.name} dropped the {target.name}.\n')
        else:
            print(f'{self.name} could not find {target.name} in their inventory.\n')

    def check_inv(self):
        print('Inventory:')
        for item in self.items:
            print(f'-{item.name}')
        print('')