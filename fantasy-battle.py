#IMPORTS
import random
import time
import os

# ATTACKS BY WARRIOR TYPE
elf_attacks = {
    "Arrow Dynamic 🏹 💨": 3,
    "Leaf Me Alone 🍂 ❌": 4,
    "Sap Shot 🍁🔫": 3
}

human_attacks = {
    "Monday Mourning Slash 🥱🤺": 5,
    "Nine-to-Five Fury 🤬": 3,
    "HR Violation 📑 🚫": 2
}

wizard_attacks = {
    "Ctrl + Alt + Delirium 💻 🔀 ": 4,
    "Staff Infection 🧙🏿‍♂️ 🦠": 4,
    "Boomerang Spell 🔄 🪄": 2
}

# DICEROLL SUBROUTINE
def rollDice(sides, count=1):
    total = 0
    for i in range(count):
        total += random.randint(1, sides)
    return total

# BATTLE LOGIC
def fight(attackername, attackertype):
    cls = (attackertype).strip().lower()
    if cls == "elf":
        pool = elf_attacks
    elif cls == "human":
        pool = human_attacks
    elif cls == "wizard":
        pool = wizard_attacks
    else:
        print(f"{attackername} has an unknown class: {attackertype}")
        return 0

    attackname, damage = random.choice(list(pool.items()))
    print(f"⚔️ {attackername} the {cls.capitalize()} uses '{attackname}', dealing {damage} damage!")
    return damage

#FANTASY BATTLE LOOP
print("=== WELCOME TO WARRIOR FANTASY BATTLE ===")
time.sleep(1)

while True:
    #SYSTEM CLEAR FOR ROUND REPEATS 
    os.system("clear")

    #PLAYER INPUTS
    name1 = input("Player 1 - Name your warrior:\n  ").strip()
    warriortype1 = input("Player 1 - Select class (Elf, Human, Wizard):\n  ").strip().lower()
    time.sleep(1)

    name2 = input("Player 2 - Name your warrior:\n ").strip()
    warriortype2 = input("Player 2 - Select class (Elf, Human, Wizard):\n  ").strip().lower()
    

    #STATS INITIALIZATION
    p1health = ((rollDice(6) * rollDice(12)) + 10) / 2
    p2health = ((rollDice(6) * rollDice(12)) + 10) / 2
    p1strength = ((rollDice(6) * rollDice(8)) + 12) / 2
    p2strength = ((rollDice(6) * rollDice(8)) + 12) / 2
    


    #USER OUTPUT
    print(f"\n{name1} the {warriortype1.capitalize()}: Health=\033[33m{p1health}\033[0m, Strength=\033[33m{p1strength}\033[0m")
    print(f"{name2} the {warriortype2.capitalize()}: Health=\033[33m{p2health}\033[0m, Strength=\033[33m{p2strength}\033[0m")
    time.sleep(6)
    print("\033[31m 🔥 LET THE BATTLE BEGIN! 🔥 \033[0m\n")

    #WHO GOES FIRST
   # Determine first attacker
    if random.randint(1, 2) == 1:
        attackername = name1
        attackertype = warriortype1
        attackerhealth = p1health
        defendername = name2
        defendertype = warriortype2
        defenderhealth = p2health
    else:
        attackername = name2
        attackertype = warriortype2
        attackerhealth = p2health
        defendername = name1
        defendertype = warriortype1
        defenderhealth = p1health

    # TURNS FOR COMBAT LOOP
    while True:
        damage = fight(attackername, attackertype)

        defenderhealth = max(defenderhealth - damage, 0)
        print(f"\033[35m {defendername}'s Health is now {defenderhealth} \033[0m\n")
        time.sleep(1)

        if defenderhealth == 0:
            print(f"🥳 \033[32m{attackername} the {warriortype1} wins! \033[35m{defendername} the {warriortype2} has been defeated. 🥳\033[0m\n")
            break

        #ROLE SWAP
        attackername, defendername = defendername, attackername
        attackertype, defendertype = defendertype, attackertype
        attackerhealth, defenderhealth = defenderhealth, attackerhealth
        time.sleep(3)

    #PLAY AGAIN QUEUE
    playagain = input("Would you like to create new warriors and fight again? (yes/no): ").strip().lower()
    if playagain != "yes":
        print("Thank you for playing!")
        os("clear")
        break
    print()
