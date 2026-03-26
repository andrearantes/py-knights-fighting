from app.models.knight import Knight


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


def battle(knights_config: dict[str, int]) -> dict[str, int]:
    # BATTLE PREPARATIONS:

    lancelot = Knight(
        name=knights_config["lancelot"]["name"],
        power=knights_config["lancelot"]["power"],
        hp=knights_config["lancelot"]["hp"],
        armour=knights_config["lancelot"]["armour"],
        weapon=knights_config["lancelot"]["weapon"],
        potion=knights_config["lancelot"]["potion"]
    )
    lancelot.prepare_for_battle()

    arthur = Knight(
        name=knights_config["arthur"]["name"],
        power=knights_config["arthur"]["power"],
        hp=knights_config["arthur"]["hp"],
        armour=knights_config["arthur"]["armour"],
        weapon=knights_config["arthur"]["weapon"],
        potion=knights_config["arthur"]["potion"]
    )
    arthur.prepare_for_battle()

    mordred = Knight(
        name=knights_config["mordred"]["name"],
        power=knights_config["mordred"]["power"],
        hp=knights_config["mordred"]["hp"],
        armour=knights_config["mordred"]["armour"],
        weapon=knights_config["mordred"]["weapon"],
        potion=knights_config["mordred"]["potion"]
    )
    mordred.prepare_for_battle()

    red_knight = Knight(
        name=knights_config["red_knight"]["name"],
        power=knights_config["red_knight"]["power"],
        hp=knights_config["red_knight"]["hp"],
        armour=knights_config["red_knight"]["armour"],
        weapon=knights_config["red_knight"]["weapon"],
        potion=knights_config["red_knight"]["potion"]
    )
    red_knight.prepare_for_battle()

    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.fight(mordred)

    # 2 Arthur vs Red Knight:
    arthur.fight(red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
