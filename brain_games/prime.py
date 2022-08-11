from math import sqrt

from brain_games.repeated_steps import *


def brain_prime():
    user_name = get_user_name_and_say_hello_to_user()
    set_game_rules('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(0, 3):
        randon_value = random.randint(0, 100)
        user_answer = get_user_answer(randon_value)
        correct_answer = set_correct_answer(randon_value)
        if str(user_answer) != correct_answer:
            error_message(user_answer, user_name, correct_answer)
            return
        else:
            success_message()
    congrats_to_user(user_name)
    return


def set_correct_answer(randon_value):
    if randon_value < 1:
        return 'no'
    if randon_value == 2:
        return 'yes'
    if randon_value % 2 == 0:
        return 'no'
    for i in range(2, int(sqrt(randon_value))+1):
        if randon_value % i == 0:
            return 'no'
    return 'yes'
