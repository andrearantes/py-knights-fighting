KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "breastplate",
                "protection": 20,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {
            "name": "Sword",
            "power": 45
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        }
    }
}


def battle(knights_config: dict) -> dict[str, int]:
    knight = []
    for knight in knights_config:

        lancelot = knight
        name = knight["lancelot"]["name"],
        power = knight["lancelot"]["power"],
        hp = knight["lancelot"]["hp"],
        armour = knight["lancelot"]["armour"],
        weapon = knight["lancelot"]["weapon"],
        potion = knight["lancelot"]["potion"]
        lancelot.prepare_for_battle()

        arthur = knight
        name = knight["arthur"]["name"],
        power = knight["arthur"]["power"],
        hp = knight["arthur"]["hp"],
        armour = knight["arthur"]["armour"],
        weapon = knight["arthur"]["weapon"],
        potion = knight["arthur"]["potion"]
        arthur.prepare_for_battle()

        mordred = knight
        name = knight["mordred"]["name"],
        power = knight["mordred"]["power"],
        hp = knight["mordred"]["hp"],
        armour = knight["mordred"]["armour"],
        weapon = knight["mordred"]["weapon"],
        potion = knight["mordred"]["potion"]

        mordred.prepare_for_battle()

        red_knight = knight
        name = knight["red_knight"]["name"],
        power = knight["red_knight"]["power"],
        hp = knight["red_knight"]["hp"],
        armour = knight["red_knight"]["armour"],
        weapon = knight["red_knight"]["weapon"],
        potion = knight["red_knight"]["potion"]
        red_knight.prepare_for_battle()

    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.fight(mordred)

    # 2 Arthur vs Red Knight:
    arthur.fight(red_knight)

    # Return fight results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
