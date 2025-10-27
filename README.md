# COMP 163 - Project 1: Character Creator & Saving/Loading

**Name:** Ajani Davis  
**Date:** October 27, 2025

**AI Usage:** Used to write README.md and for debugging

## Overview

This project is a character creation and management system for a role-playing game (RPG). It allows users to create characters with different classes, save them to files, load them back, and level them up with dynamically calculated stats.

## Features

- **Character Creation**: Create characters with four different classes
- **Stat Calculation**: Automatic stat generation based on class and level
- **Save/Load System**: Save characters to text files and load them back
- **Level Up System**: Increase character levels with automatic stat updates
- **Character Display**: View formatted character information

## Character Classes

The system supports four character classes, each with unique stats and equipment:

1. **Warrior**
   - High strength and health
   - Starting equipment: Iron Sword
   - Backstory: "A fearless fighter who seeks glory on the battlefield."

2. **Mage**
   - High magic power
   - Starting equipment: Wooden Staff
   - Backstory: "A scholar of the arcane, mastering the mysteries of magic."

3. **Rogue**
   - Balanced strength and magic
   - Starting equipment: Dagger
   - Backstory: "A quick and clever trickster who trusts no one but themselves."

4. **Cleric**
   - High health and magic
   - Starting equipment: Healing Staff
   - Backstory: "A devoted healer who travels to bring peace and balance."

## Functions

### `create_character(name, character_class)`
Creates a new character with the specified name and class.

**Parameters:**
- `name` (str): Character's name (defaults to "Anonymous Hero" if empty)
- `character_class` (str): Must be one of: "Warrior", "Mage", "Rogue", "Cleric"

**Returns:**
- Dictionary containing character data, or `None` if invalid class

**Example:**
```python
char = create_character("TestHero", "Warrior")
```

### `calculate_stats(character_class, level)`
Calculates strength, magic, and health based on class and level.

**Parameters:**
- `character_class` (str): The character's class
- `level` (int): The character's current level

**Returns:**
- Tuple of (strength, magic, health)

### `save_character(character, filename)`
Saves a character to a text file.

**Parameters:**
- `character` (dict): Character dictionary to save
- `filename` (str): Path to save file

**Returns:**
- `True` if successful, `False` if failed

**Example:**
```python
save_character(char, "my_character.txt")
```

### `load_character(filename)`
Loads a character from a text file.

**Parameters:**
- `filename` (str): Path to character file

**Returns:**
- Character dictionary, or `None` if file not found

**Example:**
```python
char = load_character("my_character.txt")
```

### `display_character(character)`
Prints formatted character information to the console.

**Parameters:**
- `character` (dict): Character dictionary to display

**Example:**
```python
display_character(char)
```

### `level_up(character)`
Increases character level by 1 and recalculates stats.

**Parameters:**
- `character` (dict): Character dictionary to level up (modified in place)

**Example:**
```python
level_up(char)
```

## Character Data Structure

Characters are stored as dictionaries with the following keys:
```python
{
    "name": str,          # Character's name
    "class": str,         # Character's class
    "strength": int,      # Strength stat
    "magic": int,         # Magic stat
    "health": int,        # Health points
    "level": int,         # Current level
    "gold": int,          # Gold amount (starts at 100)
    "equipment": str,     # Equipped item
    "backstory": str      # Character's backstory
}
```

## File Format

Characters are saved in a human-readable text format:
```
Character Name: TestHero
Class: Warrior
Level: 1
Strength: 13
Magic: 3
Health: 105
Gold: 100
Equipment: Iron Sword
Backstory: A fearless fighter who seeks glory on the battlefield.
```

## Usage Example
```python
# Create a new character
hero = create_character("Aragorn", "Warrior")

# Display the character
display_character(hero)

# Level up the character
level_up(hero)

# Save the character
save_character(hero, "aragorn.txt")

# Load the character later
loaded_hero = load_character("aragorn.txt")
display_character(loaded_hero)
```

## Running the Program

Run the main program to test character creation:
```bash
python project1_starter.py
```

## Running Tests

The project includes comprehensive tests. Run them with pytest:
```bash
pytest tests/test_comprehensive.py
```

## Requirements

- Python 3.x
- `os` module (standard library)

## Error Handling

The system handles several error cases:
- Empty or `None` character names (defaults to "Anonymous Hero")
- Invalid character classes (returns `None`)
- Invalid or empty filenames (returns `False`)
- Non-existent directories when saving (returns `False`)
- Missing files when loading (returns `None`)

## Project Structure
```
project-1-andavis24/
│
├── project1_starter.py      # Main project file
├── tests/
│   └── test_comprehensive.py  # Test suite
└── README.md                 # This file
```

## Author Notes

This project demonstrates fundamental programming concepts including:
- Function design and implementation
- File I/O operations
- Data structures (dictionaries)
- Error handling
- Code organization and documentation
