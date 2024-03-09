'''Name class'''

from models.field import Field

class Name(Field):
    '''A class for storing a contact name. Required field.'''
    def __init__(self, name):
        super().__init__(name)
