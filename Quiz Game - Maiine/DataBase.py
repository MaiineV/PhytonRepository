import random


def pick_choise(questions, answers):
    if len(questions) != 0:
        number_of_question = random.randint(0, len(questions) - 1)
        the_question = questions[number_of_question]
        the_answers = answers[number_of_question]
        questions.pop(number_of_question)
        answers.pop(number_of_question)
        return the_question, the_answers
    else:
        return '', ''



