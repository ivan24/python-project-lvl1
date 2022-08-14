from brain_games.repeated_steps import get_user_name_and_say_hello_to_user
from brain_games.repeated_steps import set_game_rules, congrats_to_user
from brain_games.repeated_steps import create_random_value, get_user_answer
from brain_games.repeated_steps import error_message, success_message
import random


def brain_calc():
    user_name = get_user_name_and_say_hello_to_user()
    set_game_rules('What is the result of the expression?')
    for i in range(0, 3):
        first_randon_value = create_random_value()
        second_random_value = create_random_value()
        operation_types = ["+", "-", "*"]
        randon_operation_type = random.choice(operation_types)
        randon_value = \
            str(first_randon_value) + " " + \
            randon_operation_type + "" \
            " " + str(second_random_value)
        user_answer = get_user_answer(randon_value)
        correct_answer = get_correct_answer(first_randon_value,
                                            second_random_value,
                                            randon_operation_type)
        if int(user_answer) == correct_answer:
            success_message()
        else:
            error_message(user_answer, user_name, correct_answer)
            return
    congrats_to_user(user_name)
    return


def get_correct_answer(first_randon_value, second_random_value,
                       randon_operation_type):
    match randon_operation_type:
        case "+":
            return first_randon_value + second_random_value
        case "-":
            return first_randon_value - second_random_value
        case "*":
            return first_randon_value * second_random_value
