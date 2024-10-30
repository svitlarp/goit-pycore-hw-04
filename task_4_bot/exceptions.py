class NameAlreadyExists(ValueError):
    print('''Can not add because this contact has already exists in phone book. 
                            Try change_contact to change it.''')

class NameDoestNotExists(ValueError):
    print('No such name in phone_book')                            