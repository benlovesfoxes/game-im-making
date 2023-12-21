# game.py

import random

def print_location(location):
    print(location["name"])
    print(location["description"])

def print_menu(options):
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

def get_choice(options):
    while True:
        choice = input("Enter your choice: ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        else:
            print("Invalid choice. Try again.")

def explore_island():
    locations = [
        {
            "name": "Beach",
            "description": "You are standing on a sandy beach with waves crashing against the shore.",
            "items": ["seashell", "coconut"],
            "secrets": ["buried treasure"]
        },
        {
            "name": "Jungle",
            "description": "You find yourself in a dense jungle with tall trees and exotic plants.",
            "items": ["banana", "rope"],
            "secrets": []
        },
        {
            "name": "Cave",
            "description": "You enter a dark cave with mysterious echoes.",
            "items": ["torch"],
            "secrets": ["hidden passage"]
        }
    ]

    current_location = random.choice(locations)
    print_location(current_location)

    while True:
        print("\nWhat do you want to do?")
        print_menu(["Explore", "Search for items", "Quit"])

        choice = get_choice(["Explore", "Search", "Quit"])

        if choice == 1:
            print_location(current_location)
        elif choice == 2:
            search_items(current_location)
        elif choice == 3:
            print("Thanks for playing!")
            break

def search_items(location):
    if "items" in location and location["items"]:
        print("You search the area and find the following items:")
        for item in location["items"]:
            print("- " + item)
    else:
        print("You search the area but find nothing.")

def main():
    print("Welcome to Mysterious Island!")
    print("You find yourself stranded on a deserted island.")

    while True:
        print("\nWhat do you want to do?")
        print_menu(["Explore the island", "Quit"])

        choice = get_choice(["Explore", "Quit"])

        if choice == 1:
            explore_island()
        elif choice == 2:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
