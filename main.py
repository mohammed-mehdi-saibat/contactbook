#!/usr/bin/env python3

import os

from contacts import menu, load_contacts, userChoice, add_contact, delete_contact

#----- Main menu

def main():
    while True:

        menu() 
        choice = userChoice()

        match choice:
            case 1:
                load_contacts()
            case 2:
                add_contact()
            case 3:
                delete_contact()
            case 4:
                os.system("clear")
                # quit("\n\033[35m========\nGood Bye!\n========\033[35m\n")
                quit("""\n\033[35m                         
                                                                                                ██
             ██████    ██████    ██████   ██████      ██████   ██    ██  ███████             ██ ██ ██
            ██        ██    ██  ██    ██  ██   ██     ██   ██   ██  ██   ██              ██  ██ ██ ██
            ██   ███  ██    ██  ██    ██  ██   ██     ██████     ████    █████            ██ ██ ██ ██
            ██    ██  ██    ██  ██    ██  ██   ██     ██   ██     ██     ██                ██████████
             ██████    ██████    ██████   ██████      ██████      ██     ███████            ████████
                                                                                             ██████ 
                \033[0m\n""")



if __name__ == "__main__":
    main()


