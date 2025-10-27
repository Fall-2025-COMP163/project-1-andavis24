"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Ajani Davis
Date: [10-27-25]
AI: Used AI to create the readme.md and help with debugging
"""

import os  


def create_character(name, character_class):
    # if the name is empty, give a default name
    if name == "" or name is None:
        name = "Anonymous Hero"

    # list of valid classes
    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]
    if character_class not in valid_classes:
        return None

    # starting level
    level = 1

    # get stats based on class and level
    strength, magic, health = calculate_stats(character_class, level)

    # all new characters start with the same amount of gold
    gold = 100

    # set starting equipment based on class
    if character_class == "Warrior":
        equipment = "Iron Sword"
    elif character_class == "Mage":
        equipment = "Wooden Staff"
    elif character_class == "Rogue":
        equipment = "Dagger"
    else:
        equipment = "Healing Staff"

    # create a dictionary to hold character info
    character = {
        "name": name,
        "class": character_class,
        "strength": strength,
        "magic": magic,
        "health": health,
        "level": level,
        "gold": gold,
        "equipment": equipment
    }

    # give each class an automatic backstory
    if character_class == "Warrior":
        backstory = "A fearless fighter who seeks glory on the battlefield."
    elif character_class == "Mage":
        backstory = "A scholar of the arcane, mastering the mysteries of magic."
    elif character_class == "Rogue":
        backstory = "A quick and clever trickster who trusts no one but themselves."
    else:  # cleric
        backstory = "A devoted healer who travels to bring peace and balance."

    character["backstory"] = backstory

    return character


def calculate_stats(character_class, level):
    # adjust stats depending on the class
    if character_class == "Warrior":
        strength = 10 + (level * 3)
        magic = 2 + (level)
        health = 100 + (level * 5)
    elif character_class == "Mage":
        strength = 3 + (level)
        magic = 12 + (level * 4)
        health = 70 + (level * 3)
    elif character_class == "Rogue":
        strength = 7 + (level * 2)
        magic = 6 + (level * 2)
        health = 80 + (level * 3)
    elif character_class == "Cleric":
        strength = 6 + (level * 2)
        magic = 10 + (level * 3)
        health = 90 + (level * 4)

    return strength, magic, health


def save_character(character, filename):
    # check if the file path seems valid before writing
    if filename == "" or filename is None:
        print("Invalid file name.")
        return False
    
    # check if the directory exist
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        print("Error: Directory does not exist.")
        return False

    # write all character info to the file
    with open(filename, "w") as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")
        file.write(f"Equipment: {character['equipment']}\n")
        file.write(f"Backstory: {character['backstory']}\n")

    return True


def load_character(filename):
    # check if the file exists before opening
    if not os.path.exists(filename):
        print("File not found.")
        return None

    # open the file and read all the data
    with open(filename, "r") as file:
        lines = file.readlines()

        # empty dictionary to rebuild the character
        character = {}

        # go through each line and pull out the data
        for line in lines:
            line = line.strip()
            parts = line.split(": ")

            # only run if the line has two parts
            if len(parts) == 2:
                key = parts[0]
                value = parts[1]

                # match file keys to dictionary keys
                if key == "Character Name":
                    character["name"] = value
                elif key == "Class":
                    character["class"] = value
                elif key == "Level":
                    character["level"] = int(value)
                elif key == "Strength":
                    character["strength"] = int(value)
                elif key == "Magic":
                    character["magic"] = int(value)
                elif key == "Health":
                    character["health"] = int(value)
                elif key == "Gold":
                    character["gold"] = int(value)
                elif key == "Equipment":
                    character["equipment"] = value
                elif key == "Backstory":
                    character["backstory"] = value

    return character


def display_character(character):
    # print out everything nicely for the player
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print(f"Equipment: {character['equipment']}")
    print(f"Backstory: {character['backstory']}")


def level_up(character):
    # add one to the level
    character["level"] = character["level"] + 1

    # get new stats for this higher level
    strength, magic, health = calculate_stats(character["class"], character["level"])

    # update dictionary values
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health

    print(f"{character['name']} leveled up to Level {character['level']}!")


# Main program for testing
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")

    char = create_character("TestHero", "Warrior")
    display_character(char)

