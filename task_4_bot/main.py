# На першому етапі наш бот-асистент повинен вміти зберігати ім'я та номер телефону, знаходити номер телефону за ім'ям, 
# змінювати записаний номер телефону, виводити в консоль всі записи, які зберіг. 
import parse_input
 
def main():
    '''
    The main function which controls the main command processing loop.
    '''
    phone_book = {}
    print(MENU)

    print('hello')
    print('"How can I help you?"')
    
    # Ask user which action he wants to do with a phone_book
    input_action = input('Enter what you wonna do with your phone_book')

    # Call parse_input() function to extract desired action from input string 
    response_action = parse_input(input_action['action'])

    while True:
    # while input != "exit" and input != "close" :

        # Building a simple match-case statement
        match response_action:
            case 'add':
                add_contact(name, phone)
            case 'change':
                change_contact(name, phone)
            case 'phone':
                show_phone(name)
            case 'all':
                show_all()
            case 'exit' | 'close':
                print('Good bye!')
                breake            
    

def add_contact(name: str, phone: str) -> str:
    if name not in phone_book:
        phone_book[name] = phone
        return "Contact added."
    else:
        raise NameAlreadyExists()


def change_contact(name, phone_to_update):
    if name in phone_book:
        phone_book[name] = phone_to_update
        return "Contact updated."
    else:
        raise NameDoestNotExists()
    

def show_phone(name):
    if name in phone_book:
        return phone_book[name]
    else:
        raise NameDoestNotExists()


def show_all():
    return phone_book











