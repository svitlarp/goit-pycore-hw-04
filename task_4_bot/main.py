from task_4_bot.input_parser import parse_input
 

def main():
    '''
    The main function which controls the main command processing loop.
    '''
    phone_book = {}
    print(MENU)

    print('hello')
    print('"How can I help you?"')
    
    # Ask user which action he wants to do with a phone_book
    user_input = input('Enter what you wonna do with your phone_book')

    # Call parse_input() function to extract desired action from input string using python unpacking
    response_action, *given_args = parse_input(user_input)

    while True:

        # Building a simple match-case statement
        match response_action:
            case 'add':
                name, phone = given_args
                add_contact(name, phone)
            case 'change':
                name, phone = given_args
                change_contact(name, phone)
            case 'phone':
                name = given_args
                show_phone(name)
            case 'all':
                show_all()
            case 'exit' | 'close':
                print('Good bye!')
                break            
    

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


if __name__ == "main":
    main()