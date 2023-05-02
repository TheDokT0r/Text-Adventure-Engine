import os


def main():
    mainMenu()


def mainMenu():
    print('Welcome to the text adventure engine!')

    option = input(
        "What would you like to do? (Type 'help' for a list of commands)\n").lower()

    os.system('cls')

    if option == 'help':
        print('Commands:')
        print('help - Displays this message')
        print('quit - Quits the program')
        print('play - Starts a game')
        print('init <game name> - Initializes a game')
        print('delete - Deletes a game')
        print('add - Adds a game to the list of games')

    if option == 'quit' or option == 'q' or option == 'exit':
        exit()

    else:
        input('Invalid command')
        os.system('cls')
        mainMenu()


if __name__ == '__main__':
    main()
