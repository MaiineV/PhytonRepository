import DataBase as Data

questions = ['What does “www” stand for in a website browser?',
             'How long is an Olympic swimming pool (in meters)?',
             'What countries made up the original Axis powers in World War II?',
             'What geometric shape is generally used for stop signs?',
             'What is the name of the biggest technology company in South Korea?']

answers = ['world wide web', '50 meters', 'germany, italy, and japan', 'octagon', 'samsung']

the_question = None
the_answer = None
points = 0

print('Welcome to my quiz game')

while True:
    the_question, the_answer = Data.pick_choise(questions, answers)
    if the_question == '':
        break
    print('This is the question!')
    player_answer = input(the_question + ': ').lower()

    if player_answer == the_answer:
        print('Correct!')
        points += 1
    else:
        print('Wrong answer!')
        print('The correct answer is "' + the_answer + '"')

print('You finish the game! Your score is: ' + str(points))
