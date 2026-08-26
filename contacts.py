#!/usr/bin/env python3

import os
import platform

# Load contacts 
def load_contacts(filename="contacts.txt"):
    keys = ['Name', 'Phone', 'Email']
    contacts = []

    with open(filename, 'a+', encoding="UTF-8") as f:
        f.seek(0)

        for line in f.readlines():
            data = line.strip().split(",")

            if len(data) == 3:
                contacts.append(dict(zip(keys, data)))

    return contacts


# Clear terminal 
def clear_cli():
    os.system("cls" if platform.system() == "Windows" else "clear")



def menu():
    print("\033[36m========================================\033[0m")
    print("---------Contacts Manager Menu--------")
    print("\033[36m========================================\033[0m\n")
    print("1. View contacts list")
    print("2. Add a contact")
    print("3. Delete contact")
    print("4. Quit\n")

def userChoice():
    try:
        choice = int(input("You choose: "))
        return choice
    except ValueError:
        print("\n\033[36mthe choice must me a number!\033[0m\n")

def add_contact():
    print(f"\n\033[32mSystem answer\033[0m: Adding contact function!")

def delete_contact():
    print("\n\033[31mSystem answer\033[0m: Deleting contact function!")


