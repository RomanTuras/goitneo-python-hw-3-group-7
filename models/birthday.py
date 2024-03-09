'''Birthday class'''

from datetime import datetime
from models.field import Field
from exceptoins_handler import input_error, IncorrectDate


@input_error
class Birthday(Field):
    '''A class for storing a contact birthday. Not required field.'''
    def __init__(self, birthday):
        birthday = str_to_date(birthday)
        super().__init__(birthday)
        print("Birthday added!")    



def str_to_date(string):
    '''Converting string to date'''
    if '.' in string:
        day, month, year = string.split('.')
        return datetime(int(year), int(month), int(day)).date()
    raise IncorrectDate
