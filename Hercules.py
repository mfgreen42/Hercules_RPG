
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
    'attack power': 10}
cerberus_attack_list = ['Snake Tail Whip','Acid Drool','Shredding Bite']

def gift_from_the_gods():
    gift = random.randrange(50, 100)
    hercules['health'] = hercules['health'] + gift
    print(f"""
    Hercules, you have been given a Healing Elixor from the Gods! 
        Your health has been restored by {gift} points. You now have {hercules['health']}""")


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
                print('You have defeated the vicious Lernaean Hydra!! Do you think you can Capture the guard dog of the underword? ')
            else:
                print(f'Sword Slash caused 25 damage points. The Lernaean Hydras health is now {hydra["health"]}')
    if user_input == 'Flying Side Kick':
            hydra['health'] = hydra['health'] - 25
            if hydra['health'] == 0:
                print('You have defeated the vicious Lernaean Hydra!! Do you think you can Capture the guard dog of the underword? ')
            else:
                print(f'Flying Side Kick caused 25 damage points. The Lernaean Hydras health is now {hydra["health"]}')
    if user_input == 'Skull Crusher':
            hydra['health'] = hydra['health'] - 25
            if hydra['health'] == 0:
                print('You have defeated the vicious Lernaean Hydra!! Do you think you can Capture the guard dog of the underword? ')
            else:
                print(f'Skull Crusher caused 25 damage points. The Lernaean Hydras health is now {hydra["health"]}')

def hercules_attack_cerberus():
    user_input = input('What attack would you like to use against Cerberus ? Sword Slash, Flying Side Kick or Skull Crusher :')
    if user_input == 'Sword Slash':
            cerberus['health'] = cerberus['health'] - 25
            if hydra['health'] == 0:
                print('You have Capture the guard dog of the underword!! ')
            else:
                print(f'Sword Slash caused 25 damage points. Cerberus health is now {cerberus["health"]}')
    if user_input == 'Flying Side Kick':
            cerberus['health'] = cerberus['health'] - 25
            if cerberus['health'] == 0:
                print('You have Capture the guard dog of the underword ')
            else:
                print(f'Flying Side Kick caused 25 damage points. Cerberus health is now {cerberus["health"]}')
    if user_input == 'Skull Crusher':
            cerberus['health'] = cerberus['health'] - 25
            if cerberus['health'] == 0:
                print('You have Capture the guard dog of the underword ')
            else:
                print(f'Skull Crusher caused 25 damage points. Cerberus health is now {hydra["health"]}')

    
def lion_attack(): #random attatck 
    attack = random.choice(lions_attacks)
    hercules['health'] = hercules['health'] - lion['attack power']
    print(f'The Nemean Lion has attacked you with {attack} causing {lion["attack power"]} damage.')
    print(f'Your health level is now {hercules["health"]}')

def hydra_attack(): #random attack
    attack = random.choice(hydras_attacks)
    hercules['health'] = hercules['health'] - hydra['attack power']
    print(f'The Nemean Lion has attacked you with {attack} causing {hydra["attack power"]} damage.')
    print(f'Your health level is now {hercules["health"]}')

def cerberus_attack(): #random attack
    attack = random.choice(cerberus_attack_list)
    hercules['health'] = hercules['health'] - cerberus['attack power']
    print(f'Cerberus has attacked you with {attack} causing {cerberus["attack power"]} damage.')
    print(f'Your health level is now {hercules["health"]}')

def print_winner():
    print(f"""Congratulations Hercules, you have completed your tasks! and you still have {hercules['health']} health left, amazing! 
    """)

def run_game():
    print_greeting()
    while lion['health'] != 0: 
        lion_attack()
        hercules_attack_lion()
    while hydra['health'] != 0: 
        hydra_attack()
        hercules_attack_hydra()
    gift_from_the_gods()
    while cerberus['health'] != 0: 
        cerberus_attack()
        hercules_attack_cerberus()
    print_winner()
run_game()
