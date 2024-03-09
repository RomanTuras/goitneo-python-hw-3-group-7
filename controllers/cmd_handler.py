'''Commands handler module'''

from datetime import datetime, timedelta
from exceptoins_handler import input_error, NameExists
from models.address_book import AddressBook
from models.record import Record
from models.birthday import str_to_date
from constants import IS_DEBUG


def parse_input(user_input):
    '''
    Parsing user input
    '''
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book:AddressBook):
    '''
    Add a new contact
    '''
    name, phone = args
    record = Record(name)
    if book.is_has_record(record):
        raise NameExists
    record.add_phone(phone)
    book.add_record(record)
    print("Contact added!")


@input_error
def remove_phone(args, book:AddressBook):
    '''
    Removing phone from contact
    '''
    name, phone = args
    record = Record(name)
    if book.is_has_record(record):
        record.remove_phone(phone)
        book.update_record(record)
        print("Phone removed!")


@input_error
def change_contact(args, book:AddressBook):
    '''
    Change contact number by name
    '''
    name, old_phone = args
    record = book.find_by_name(name)
    if record:
        new_phone = input("Enter a new phone: ")
        record.edit_phone(old_phone, new_phone)
        print("Contact updated!")


@input_error
def find_contact_by_phone(args, book:AddressBook):
    '''
    Getting contact by phone number
    '''
    phone = args[0]
    for record in book.values():
        if record.find_phone(phone):
            print(record)
        else:
            raise KeyError


def show_all_contacts(book:AddressBook):
    '''
    Showing all contacts
    '''
    for name, record in book.data.items():
        print(record)


def add_birthday_by_name(args, book:AddressBook):
    '''
    Adding a birthday to contact by name
    '''
    name, birthday = args
    record = book.find_by_name(name)
    if record:
        record.add_birthday(birthday)


@input_error
def show_birthday_by_name(args, book:AddressBook):
    '''Showing contact birthday'''
    name = args[0]
    record = book.find_by_name(name)
    if record:
        print(f"Birthday is: {record.birthday}")


def get_birthdays_next_week(book:AddressBook):
    '''Getting users, having birthdays on next working week'''
    if IS_DEBUG:
        today = datetime(2023, 12, 30).date()
    else:
        today = datetime.today().date()

    next_seven_days = today + timedelta(days=7)
    # Create a dictionary to store users by weekday
    users_by_weekday = {day: [] for day in [
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}
    
    # Organize users by weekday if their birthday falls within the next 7 days
    for name, record in book.data.items():
        birthday = record.birthday.value
        # print(birthday)
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        if today <= birthday_this_year <= next_seven_days:
            weekday = birthday_this_year.strftime('%A')
            # If the birthday falls on Saturday or Sunday, move it to the next Monday
            if weekday=='Saturday' and birthday_this_year + timedelta(days=2) <= next_seven_days:
                users_by_weekday['Monday'].append(record.name.value)
            elif weekday=='Sunday' and birthday_this_year + timedelta(days=1) <= next_seven_days:
                users_by_weekday['Monday'].append(record.name.value)
            else:
                users_by_weekday[weekday].append(record.name.value)

    # Print the result
    for day, user_list in users_by_weekday.items():
        if user_list:
            formatted_users = ', '.join(user_list)
            print(f"{day}: {formatted_users}")
