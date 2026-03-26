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


def battle(knightsConfig):
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Knight(
        name=knightsConfig['lancelot']['name'],
        power=knightsConfig['lancelot']['power'],
        hp=knightsConfig['lancelot']['hp'],
        armour=knightsConfig['lancelot']['armour'],
        weapon=knightsConfig['lancelot']['weapon'],
        potion=knightsConfig['lancelot']['potion']
    )
    lancelot.prepare_for_battle()

    # arthur
    arthur = Knight(
        name=knightsConfig['arthur']['name'],
        power=knightsConfig['arthur']['power'],
        hp=knightsConfig['arthur']['hp'],
        armour=knightsConfig['arthur']['armour'],
        weapon=knightsConfig['arthur']['weapon'],
        potion=knightsConfig['arthur']['potion']
    )
    arthur.prepare_for_battle()

    # mordred
    mordred = knight(
        name=knightsConfig['mordred']['name'],
        power=knightsConfig['mordred']['power'],
        hp=knightsConfig['mordred']['hp'],
        armour=knightsConfig['mordred']['armour'],
        weapon=knightsConfig['mordred']['weapon'],
        potion=knightsConfig['mordred']['potion']
    )
    mordred.prepare_for_battle()

    # red_knight
    red_knight = knight(
        name=knightsConfig['red_knight']['name'],
        power=knightsConfig['red_knight']['power'],
        hp=knightsConfig['red_knight']['hp'],
        armour=knightsConfig['red_knight']['armour'],
        weapon=knightsConfig['red_knight']['weapon'],
        potion=knightsConfig['red_knight']['potion']
    )
    red_knight.prepare_for_battle()

    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.battle(mordred)

    # 2 Arthur vs Red Knight:
    arthur.battle(red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
