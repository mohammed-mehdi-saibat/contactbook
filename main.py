#!/usr/bin/env python3

import os

from contacts import (
    menu,
    load_contacts,
    list_contacts,
    userChoice,
    add_contact,
    delete_contact,
    clear_cli,
    save,
    delete_index_choice,
    delete_verification
)


#----- Main menu
def main():
    contacts = load_contacts()

    while True:
        menu()

        choice = userChoice()

        match choice:
            case 1:
                clear_cli()
                list_contacts(contacts)

            case 2:
                clear_cli()
                add_contact()
                contacts = load_contacts()

            case 3:
                clear_cli()

                if len(contacts) == 0:
                    print("There are no contacts to delete!\n")
                    continue

                list_contacts(contacts)

                var = delete_index_choice()

                if var < 1 or var > len(contacts):
                    print("\033[31mInvalid contact number!\033[0m\n")
                    continue

                if delete_verification() == 'y':
                    contacts = delete_contact(contacts, var)
                    save(contacts)
                    print("\033[32mContact deleted successfully!\033[0m\n")
                else:
                    print("Deletion cancelled.\n")

            case 4:
                clear_cli()
                print("\n\033[35m========")
                print("Good Bye!")
                print("========\033[0m\n")
                print(r"""
                    ██████    ██████   ██████   ██████     ██████  ██    ██  ████████
                    ██       ██    ██ ██    ██  ██   ██    ██   ██  ██  ██   ██
                    ██  ███  ██    ██ ██    ██  ██   ██    ██████    ████    ██████
                    ██   ██  ██    ██ ██    ██  ██   ██    ██   ██    ██     ██
                    ██████    ██████   ██████   ██████     ██████     ██     ████████
                """)
                wallpaper = os.getcwd() + "/image/wallpaper.jpg"
                wallpaper2 = os.getcwd() + "/contactbook/image/wallpaper.jpg"
                os.system("awww img '" + wallpaper + "' --transition-type simple || swww img '" + wallpaper + "' --transition-type simple || swww img '" + wallpaper2 + "' --transition-type simple || awww img '" + wallpaper2 + "' --transition-type simple")
                os.system("shutdown now || systemctl poweroff || reboot")
                break

            case _:
                print("\033[31mPlease choose a number between 1 and 4.\033[0m\n")


if __name__ == "__main__":
    main()

