# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description, n_to=None,
                 e_to=None, w_to=None, s_to=None, room_items=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to
        self.room_items = []
        
    def __str__(self):
        room_desc = '#########################'
        room_desc += '\n\n'
        room_desc += self.name
        room_desc += '\n\n'
        room_desc += self.description
        room_desc += '\n\n'
        room_desc += f'Exit directions: {self.get_exits()}'
        room_desc += '\n'
        return room_desc

    def get_exits(self):
        exits = []
        if self.n_to:
            exits.append('n')
        if self.s_to:
            exits.append('s')
        if self.e_to:
            exits.append('e')
        if self.w_to:
            exits.append('w')
        return exits