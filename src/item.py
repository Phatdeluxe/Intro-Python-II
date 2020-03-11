'''
Class(es) for items in the adventure game
'''

class Item():
    def __init__(self, name='Junk', description='Just some junk', cur_room=None):
        self.name = name
        self.description = description
        self.cur_room = cur_room