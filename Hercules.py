

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
    'attack power': 15,
    'attack 1': 'Raging Claw Strike',
    'attack 2': 'Deafening Roar',
    'attack 3': 'Razor Bite'
}

hydra = {
    'health': 100,
    'attack power': 15,
    'attack 1': 'Vemon Bite',
    'attack 2': 'Fire Ball',
    'attack 3': 'Multi Razor Bites'
}

cerberus = {
    'health': 100,
    'attack power': 15,
    'attack 1': 'Snake Tail Whip',
    'attack 2': 'Acid Drool',
    'attack 3': 'Shredding Bite'
}

def hercules_attack_lion():#should be able to choose attack
        user_input = input('what attack would you like to use against the vicious Nemean Lion ? Sword Slash, Flying Side Kick or Skull Crusher :')
        if user_input == 'Sword Slash':
            lion['health'] = lion['health'] - 25
            if lion['health'] == 0:
                print('You have defeated the vicious Nemean Lion!! Do you think you can handle the impossible nine-headed Lernaean Hydra? ')
            else:
                print(f'Sword Slash caused 25 damage points. The Nemean Lions health is now {lion["health"]}')
        if user_input == 'Flying Side Kick':
            lion['health'] = lion['health'] - 25
            if lion['health'] == 0:
                print('You have defeated the vicious Nemean Lion!! Do you think you can handle the impossible nine-headed Lernaean Hydra? ')
            else:
                print(f'Flying Side Kick caused 25 damage points. The Nemean Lions health is now {lion["health"]}')
        if user_input == 'Skull Crusher':
            lion['health'] = lion['health'] - 25
            if lion['health'] == 0:
                print('You have defeated the vicious Nemean Lion!! Do you think you can handle the impossible nine-headed Lernaean Hydra? ')
            else:
                print(f'Skull Crusher caused 25 damage points. The Nemean Lions health is now {lion["health"]}')

def hercules_attack_hydra():
    pass

def hercules_attack_cerberus():
    pass


def lion_attack(): #random attatck 
    pass



def hydra_attack(): #random attatck
    pass

def cerberus_attack(): #random attatck
    pass

def attack(): #As a developer, I want to use an Attack() function that will terminate when Hercules or an enemy’s health reaches zero.
    pass

def run_game():
    print_greeting()
    hercules_attack_lion()
    lion_attack()




run_game()
