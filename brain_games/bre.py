from brain_games.repeated_steps import get_user_name_and_say_hello_to_user, set_game_rules, congrats_to_user
from brain_games.repeated_steps import get_user_answer, error_message, success_message
import random


def brain_even():
    user_name = get_user_name_and_say_hello_to_user()
    set_game_rules('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(0, 3):
        randon_value = random.randint(0, 100)
        user_answer = get_user_answer(randon_value)
        correct_answer = set_correct_answer(randon_value)
        if user_answer != correct_answer:
            error_message(user_answer, user_name, correct_answer)
            return
        else:
            success_message()
    congrats_to_user(user_name)
    return


def set_correct_answer(randon_number):
    if randon_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer

