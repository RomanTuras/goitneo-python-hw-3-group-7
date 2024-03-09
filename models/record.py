'''Record class'''

from models.name import Name
from models.phone import Phone
from models.birthday import Birthday
from exceptoins_handler import PhoneNotFound


class Record:
    '''A class for storing information about a contact, including name and phone list.'''
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = "--"

    def add_phone(self, phone_number):
        '''Adding phone'''
        phone = Phone(phone_number)
        self.phones.append(phone)

    def edit_phone(self, old_phone, new_phone):
        '''Edit phone number'''
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return

    def remove_phone(self, phone):
        '''Removing phone number'''
        if phone in self.phones:
            self.phones.remove(phone)

    # def find_phone(self, phone_number):
    #     '''Finding phone number'''
    #     for phone in self.phones:
    #         if phone.value == phone_number:
    #             return phone_number
    #     raise PhoneNotFound
    
    def add_birthday(self, birthday):
        '''Add birthday to contact'''
        self.birthday = Birthday(birthday)


    def __str__(self):
        return f"Contact: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"
