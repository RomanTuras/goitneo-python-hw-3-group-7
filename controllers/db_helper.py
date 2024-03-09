'''Initial module'''

from models.address_book import AddressBook
from models.record import Record
from models.phone import Phone
from models.birthday import Birthday
from constants import IS_DEBUG


def init(book:AddressBook):
    '''Initial boot data from db'''
    if IS_DEBUG:
        phone = Phone("4445556667")
        record = Record("Chubaka")
        record.phones.append(phone)
        record.birthday = Birthday("31.12.1955")
        book.add_record(record)

        phone = Phone("5555666777")
        record = Record("Han,Solo")
        record.phones.append(phone)
        record.birthday = Birthday("3.1.1995")
        book.add_record(record)

        phone = Phone("7777888999")
        record = Record("Luke,Skywalker")
        record.phones.append(phone)
        record.birthday = Birthday("25.2.2005")
        book.add_record(record)

        phone = Phone("8888777666")
        record = Record("Dart,Waider")
        record.phones.append(phone)
        record.birthday = Birthday("5.1.1991")
        book.add_record(record)

        phone = Phone("9999666555")
        record = Record("Princess,Lea")
        record.phones.append(phone)
        record.birthday = Birthday("24.2.2010")
        book.add_record(record)
