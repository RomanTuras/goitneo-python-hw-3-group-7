'''Phone class'''

from models.field import Field
from exceptoins_handler import IncorrectPhoneNumber

class Phone(Field):
    '''A class for storing a phone number. Has format validation (10 digits).'''
    def __init__(self, phone_number):
        if phone_number.isdigit() and len(phone_number)==10:
            super().__init__(phone_number)
        else:
            raise IncorrectPhoneNumber
