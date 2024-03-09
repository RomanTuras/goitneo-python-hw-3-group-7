'''AddressBook class'''

from collections import UserDict
from models.record import Record
from exceptoins_handler import NameExists, input_error

class AddressBook(UserDict):
    '''A class for storing and managing records.'''

    def is_has_record(self, record:Record):
        '''Check is record exists'''
        return record.name.value in self.data.keys()

    @input_error
    def add_record(self, record:Record):
        '''Storing record'''
        if self.is_has_record(record):
            raise NameExists
        else:
            self.data.update({record.name.value:record})

    @input_error
    def update_record(self, record:Record):
        '''Updating record'''
        if self.is_has_record(record):
            self.data.update({record.name.value:record})

    @input_error
    def delete(self, record:Record):
        '''Deleting record'''
        self.data.pop(record)

    @input_error
    def find_by_name(self, name):
        '''Finding record by user name'''
        record = self.data.get(name)
        if record:
            return record
        raise KeyError
