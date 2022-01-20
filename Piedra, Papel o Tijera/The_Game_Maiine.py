import Random_IA as Random


def game():
    posible_choise = ['rock', 'paper', 'scissors']
    player_choise = None

    rules_dictionary = {'paper': 'rock',
                        'rock': 'scissors',
                        'scissors': 'paper'}

    while player_choise not in posible_choise:
        if player_choise is not None:
            print('This is not a valid answer')
        player_choise = input('rock, paper or scissors?: ').lower()

    print('The player choise was ' + player_choise)

    computer_choise = Random.select()
    print('The computer choise was ' + computer_choise)

    if player_choise == computer_choise:
        print('It is Draw')
    elif rules_dictionary.get(player_choise) == computer_choise:
        print('You won')
    elif rules_dictionary.get(computer_choise) == player_choise:
        print('The computer won')
