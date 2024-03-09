'''Exceptions handler'''


class NameExists(Exception):
    '''Name already exists'''

class IncorrectPhoneNumber(Exception):
    '''Incorrect Phone Number'''

class PhoneNotFound(Exception):
    '''Phone not found'''

class IncorrectDate(Exception):
    '''Date error'''


def input_error(func):
    '''
    Error handler decotator
    '''
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("Give me name and phone please!")
        except NameExists:
            print("The same name already exists, add another!")
        except KeyError:
            print("Name not found!")
        except IncorrectPhoneNumber:
            print("Incorrect Phone Number!")
        except PhoneNotFound:
            print("Phone not found!")
        except IncorrectDate:
            print("Date error! Use next format: DD.MM.YYYY")
        except IndexError:
            print("Give me name")

    return inner
