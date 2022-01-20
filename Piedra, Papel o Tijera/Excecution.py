import The_Game_Maiine as SGame

play_again = True
while play_again:
    SGame.game()
    while True:
        answer = input('Do you want to play again? (yes/no): ').lower()
        if answer == 'yes':
            pass
            break
        elif answer == 'no':
            play_again = False
            break
        else:
            print('This is not a valida answer')
