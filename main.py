'''
    HW-2 Contacts assistant bot module
    Entry point
'''

import controllers.cmd_handler as handler
from models.address_book import AddressBook
from controllers.db_helper import init

def main():
    '''
    Main module
    '''
    book = AddressBook()
    init(book)
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = handler.parse_input(user_input)

        if command in ["close", "exit", "e"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            handler.add_contact(args, book)
        elif command == "change":
            handler.change_contact(args, book)
        elif command == "phone":
            handler.find_contact_by_phone(args, book)
        elif command == "remove":
            handler.remove_phone(args, book)
        elif command == "all":
            handler.show_all_contacts(book)
        elif command  in ["add-birthday", "ab"]:
            handler.add_birthday_by_name(args, book)
        elif command in ["show-birthday", "sb"]:
            handler.show_birthday_by_name(args, book)
        elif command in ["birthdays", "b"]:
            handler.get_birthdays_next_week(book)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
