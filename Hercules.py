
import random

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
    'attack power': 10,
}
lions_attacks = ['Raging Claw Strike', 'Deafening Roar','Razor Bite']


hydra = {
    'health': 100,
    'attack power': 10}
hydras_attacks = ['Vemon Bite','Fire Ball','Multi Razor Bites']


cerberus = {
    'health': 100,
    'attack power': 10,
    'attack 1': 'Snake Tail Whip',
    'attack 2': 'Acid Drool',
    'attack 3': 'Shredding Bite'
}

def hercules_attack_lion():#should be able to choose attack
        user_input = input('What attack would you like to use against the vicious Nemean Lion ? Sword Slash, Flying Side Kick or Skull Crusher :')
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
    user_input = input('What attack would you like to use against the Lernaean Hydra ? Sword Slash, Flying Side Kick or Skull Crusher :')
    if user_input == 'Sword Slash':
            hydra['health'] = hydra['health'] - 25
            if hydra['health'] == 0:
                print('You have defeated the vicious Lernaean Hydra!! Do you think you can handle the impossible nine-headed Lernaean Hydra? ')
            else:
                print(f'Sword Slash caused 25 damage points. The Lernaean Hydras health is now {hydra["health"]}')
    if user_input == 'Flying Side Kick':
            hydra['health'] = hydra['health'] - 25
            if hydra['health'] == 0:
                print('You have defeated the vicious Lernaean Hydra!! Do you think you can handle the impossible nine-headed Lernaean Hydra? ')
            else:
                print(f'Flying Side Kick caused 25 damage points. The Lernaean Hydras health is now {hydra["health"]}')
    if user_input == 'Skull Crusher':
            hydra['health'] = hydra['health'] - 25
            if hydra['health'] == 0:
                print('You have defeated the vicious Lernaean Hydra!! Do you think you can handle the impossible nine-headed Lernaean Hydra? ')
            else:
                print(f'Skull Crusher caused 25 damage points. The Lernaean Hydras health is now {hydra["health"]}')

def hercules_attack_cerberus():
    pass


def lion_attack(): #random attatck 
    attack = random.choice(lions_attacks)
    hercules['health'] = hercules['health'] - lion['attack power']
    print(f'The Nemean Lion has attacked you with {attack} causing {lion["attack power"]} damage.')
    print(f'Your health level is now {hercules["health"]}')



def hydra_attack(): #random attatck
    attack = random.choice(hydras_attacks)
    hercules['health'] = hercules['health'] - hydra['attack power']
    print(f'The Nemean Lion has attacked you with {attack} causing {hydra["attack power"]} damage.')
    print(f'Your health level is now {hercules["health"]}')

def cerberus_attack(): #random attatck
    pass

def attack(): #As a developer, I want to use an Attack() function that will terminate when Hercules or an enemy’s health reaches zero.
    pass

def run_game():
    print_greeting()
    while lion['health'] != 0:
        lion_attack()
        hercules_attack_lion()
    while hydra['health'] != 0:
        hydra_attack()
        hercules_attack_hydra()



run_game()
