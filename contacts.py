#!/usr/bin/env python3

import os
import platform

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

def load_contacts():

    contacts = []

    try:
        with open(filename, 'r', encoding="UTF-8") as f:
            for line in f:
                print(line) 
    except FileNotFoundError:
        print(f"\nThe list is still empty: {contacts}\n")


