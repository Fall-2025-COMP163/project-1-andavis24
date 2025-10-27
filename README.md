# COMP 163: Project 1 – Character Creator & Chronicles

**Name:** Ajani Davis  
**Date:** October 27, 2025  
**AI Usage:** Used AI to create this README.md and assist with debugging  
**Development Workflow:** Build → Test → Interview  
**Critical Constraint:** Only concepts covered through the Files chapter were used.  
(No classes, try/except, or advanced modules beyond `os`.)

---

## 🧩 Game Concept

The **Character Creator & Chronicles** project simulates the foundation of a role-playing game (RPG) where players can design unique heroes, save and load their progress, and experience progression through stat growth.  

Each hero begins their journey as one of four iconic classes — **Warrior, Mage, Rogue, or Cleric** — each equipped with unique stats, equipment, and a personalized backstory that sets the tone for their adventure.

---

## ⚙️ Core Features (Base Requirements)

### 1. Character Creation
- Builds a new character with class, stats, level, gold, and equipment.
- Automatically assigns a default name `"Anonymous Hero"` if no name is given.
- Validates character classes before creation.

### 2. Stat Calculation
- Uses class-based formulas to calculate strength, magic, and health.
- Each class has its own growth rate and specialization.

### 3. Save Character
- Saves all character data to a formatted text file for reloading later.
- Validates directory paths before saving and prevents invalid writes.

### 4. Load Character
- Loads data from a text file and rebuilds the character dictionary.
- Handles missing files gracefully.

### 5. Level-Up System
- Increases character level by 1.
- Recalculates stats dynamically according to class and level progression.

### 6. Character Display
- Prints a formatted character sheet showing all information clearly.

---

## 🧙 Character Classes

| Class | Focus | Starting Equipment | Backstory |
|--------|--------|--------------------|------------|
| **Warrior** | High strength and health | Iron Sword | "A fearless fighter who seeks glory on the battlefield." |
| **Mage** | High magic and intelligence | Wooden Staff | "A scholar of the arcane, mastering the mysteries of magic." |
| **Rogue** | Balanced agility and speed | Dagger | "A quick and clever trickster who trusts no one but themselves." |
| **Cleric** | High health and healing ability | Healing Staff | "A devoted healer who travels to bring peace and balance." |

---

## 🧮 Stat Formulas (Design Choice)

| Class | Strength Formula | Magic Formula | Health Formula |
|--------|------------------|----------------|----------------|
| Warrior | `10 + (level * 3)` | `2 + (level)` | `100 + (level * 5)` |
| Mage | `3 + (level)` | `12 + (level * 4)` | `70 + (level * 3)` |
| Rogue | `7 + (level * 2)` | `6 + (level * 2)` | `80 + (level * 3)` |
| Cleric | `6 + (level * 2)` | `10 + (level * 3)` | `90 + (level * 4)` |

These formulas ensure each class has a unique progression path that aligns with their strengths.

---

## 💾 File Format (Required by Tests)

Characters are saved in the following exact format:
Character Name: TestHero
Class: Warrior
Level: 1
Strength: 13
Magic: 3
Health: 105
Gold: 100
Equipment: Iron Sword
Backstory: A fearless fighter who seeks glory on the battlefield.


## 📜 Error Handling

| Error Type | Behavior |
|-------------|-----------|
| Invalid Class | Returns `None` |
| Empty/None Filename | Prints “Invalid file name.” and returns `False` |
| Missing Directory | Prints “Error: Directory does not exist.” and returns `False` |
| Missing File on Load | Prints “File not found.” and returns `None` |
| Empty Name | Automatically assigns `"Anonymous Hero"` |

---

##  Bonus Creative Features (Implemented)

| Bonus Feature | Description | Bonus Points |
|----------------|--------------|--------------|
| **Character Backstory System** | Each class has a unique narrative backstory automatically assigned during creation. |  |
| **Starting Equipment System** | Each class begins with specialized starting gear (e.g., Iron Sword, Wooden Staff, Dagger, Healing Staff). |  |

**Total Bonus Implemented:** +4 points

---

## 🧪 Testing & Validation

### To Run the Program

python3 project1_starter.py
To Run Automated Tests
bash
Copy code
pytest tests/test_comprehensive.py
Tests verify:

Proper character creation and stat scaling

File saving/loading consistency

Level-up stat changes

Proper formatting and output

Directory validation and missing file handling

📁 Project Structure
bash
Copy code
project-1-andavis24/
│
├── project1_starter.py          # Main project implementation
├── tests/
│   └── test_comprehensive.py    # Provided test suite
└── README.md                    # Project documentation
💬 AI Usage Statement
AI assistance was used to draft this README.md and to assist with debugging issues related to file saving and validation.
All logic, formulas, and implementations were created, tested, and understood independently.
