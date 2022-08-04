import random
from brain_games.cli import welcome_user

import prompt


def brain_even():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(5, 8):
        randon_number = random.randint(0, 100)
        print("Question: " + str(randon_number))
        user_answer = prompt.string("Your answer: ")
        correct_answer = set_correct_answer(randon_number)
        if user_answer != correct_answer:
            print(
                "\"" + user_answer + "\"" + " is wrong answer ;(. Correct answer was " + "\"" + correct_answer + "\"" +
                ".\nLet's try again, " + user_name + "!")
            return
        else:
            print("Correct!")
    print("Congratulations, " + user_name)
    return


def set_correct_answer(randon_number):
    if randon_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer
