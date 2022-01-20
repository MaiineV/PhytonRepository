import Random_IA as Random


def game():
    valid_answer = True
    posible_choise = ['rock', 'paper', 'scissors']
    player_choise = ''

    rules_dictionary = {'paper': 'rock',
                        'rock': 'scissors',
                        'scissors': 'paper'}

    while valid_answer:
        player_choise = input('rock, paper or scissors?: ')
        for i in posible_choise:
            if player_choise == i:
                valid_answer = False
                print('The player choise was ' + player_choise)
        if valid_answer:
            print('This is not a valid answer')

    computer_choise = Random.select()
    print('The computer choise was ' + computer_choise)

    if player_choise == computer_choise:
        print('It is Draw')
    elif rules_dictionary.get(player_choise) == computer_choise:
        print('You won')
    elif rules_dictionary.get(computer_choise) == player_choise:
        print('The computer won')
