Fantasy Battle Game

A simple, turn-based command-line game where two players name their warriors, choose a class (Elf, Human, or Wizard), and face off in a randomized battle using unique class-based attacks.

Features

Three warrior classes with distinct attack pools:

Elf (e.g., Arrow Dynamic, Leaf Me Alone, Sap Shot)

Human (e.g., Monday Mourning Slash, Nine-to-Five Fury, HR Violation)

Wizard (e.g., Ctrl + Alt + Delirium, Staff Infection, Boomerang Spell)

Randomized stats for health and strength using dice rolls

Turn-based combat with attack swapping until one warrior is defeated

Colorful console output with emojis and ANSI colors for an engaging CLI experience

Replayability: prompt to start a new duel when a game ends

Prerequisites

Python 3.6 or higher

Installation

Clone the repository

git clone https://github.com/Nthomalas/Fantasy-Battle-game.git
cd Fantasy-Battle-game

(Optional) Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\\Scripts\\activate  # Windows

Install dependencies

There are no external dependencies beyond the Python standard library.

Usage

Run the game script:

python battle.py

Follow the on-screen prompts:

Enter names and choose classes for Player 1 and Player 2.

Watch the randomly determined stats (health and strength).

See who strikes first, then take turns until one warrior’s health drops to zero.

After the battle ends, choose whether to play again.

How It Works

Stat Generation: Health and strength are calculated using the rollDice helper, simulating dice rolls.

Attack Selection: Each class has a dictionary of attack names and damage values. On each turn, a random attack is chosen and applied.

Turn Order: Randomly decided at the start of each battle.

Game Loop: Continues swapping attacker/defender roles until one warrior’s health is depleted.

File Structure

Fantasy-Battle-game/
├── battle.py       # Main game script
├── .gitignore      # Suggested ignores (e.g., __pycache__/, venv/)
└── README.md       # This file

Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for:

New warrior classes or attacks

Enhanced game mechanics (e.g., spells, items, critical hits)

Bug fixes or code refactoring

Fork the repo

Create a new branch (git checkout -b feature/my-feature)

Commit your changes (git commit -m "Add feature: ...")

Push to the branch (git push origin feature/my-feature)

Open a Pull Request

