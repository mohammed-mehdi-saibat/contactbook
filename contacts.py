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


# Get all contacts
def list_contacts(contacts):
    index = 1

    for contact in contacts:
        print(f"\033[32m======== User N{index} ========\033[0m")
        print(f"Name: {contact['Name']}")
        print(f"Phone Number: {contact['Phone']}")
        print(f"Email: {contact['Email']}")
        print()
        index += 1

    if len(contacts) == 0:
        print("There are no contacts yet!\n")



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

# Add a contact
def add_contact():
    contact_name = input("Contact name: ")
    contact_phone = input("Contact phone: ")
    contact_email = input("Contact email: ")

    user_data = contact_name + "," + contact_phone + "," + contact_email + "\n"

    with open('contacts.txt', 'a', encoding="UTF-8") as f:
        f.write(user_data)


# Save contacts 
def save(contacts):
    with open("contacts.txt", 'w', encoding="UTF-8") as file:
        for contact in contacts:
            user_data = (
                contact["Name"] + ","
                + contact["Phone"] + ","
                + contact["Email"] + "\n"
            )
            file.write(user_data)


def delete_contact():
    print("\n\033[31mSystem answer\033[0m: Deleting contact function!")


