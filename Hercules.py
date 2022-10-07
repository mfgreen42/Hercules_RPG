

def print_greeting():
    print("""
    Hercules, it's about time you showed up! King Eurystheus has been waiting, it's never good to keep a king waiting. 
    
    You have been given three tasks: 
        Slay the vicious Nemean Lion
        Defeat the impossible nine-headed Lernaean Hydra
        Capture the guard dog of the underword - Cerberus
    Are you ready to get started? oh who am I kidding?! you don't get a choice...
    """)


#each char starts with 100 health points
#list of attatcks and points

hercules = {
    'health': 100,
    'attack power': 25,
    'attack 1': 'Sword Slash',
    'attack 2': 'Flying Side Kick',
    'attatck 3': 'Skull Crusher'
}

lion = {
    'health': 100,
    'attack power': 20,
    'attack 1': 'Raging Claw Strike',
    'attack 2': 'Deafening Roar',
    'attack 3': 'Razor Bite'
}

hydra = {
    'health': 100,
    'attack power': 20,
    'attack 1': 'Vemon Bite',
    'attack 2': 'Fire Ball',
    'attack 3': 'Multi Razor Bites'
}

cerberus = {
    'health': 100,
    'attack power': 20,
    'attack 1': 'Snake Tail Whip',
    'attack 2': 'Acid Drool',
    'attack 3': 'Shredding Bite'
}

def hercules_attatck():#should be able to choose attack
    pass


def lion_attack(): #random attatck 
    pass

def hydra_attack(): #random attatck
    pass

def cerberus_attatck(): #random attatck
    pass

def attack(): #As a developer, I want to use an Attack() function that will terminate when Hercules or an enemy’s health reaches zero.
    pass

def run_game():
    print_greeting()

run_game()
