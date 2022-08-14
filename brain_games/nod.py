from brain_games.repeated_steps import get_user_name_and_say_hello_to_user
from brain_games.repeated_steps import set_game_rules, congrats_to_user
from brain_games.repeated_steps import create_random_value, get_user_answer
from brain_games.repeated_steps import error_message, success_message


def brain_gcd():
    user_name = get_user_name_and_say_hello_to_user()
    set_game_rules('Find the greatest common divisor of given numbers.')
    for i in range(0, 3):
        first_randon_value = create_random_value()
        second_random_value = create_random_value()
        user_answer = get_user_answer(
            str(first_randon_value) + " " + str(second_random_value))
        correct_answer = get_common_division(first_randon_value,
                                             second_random_value)
        if user_answer.isdigit():
            if int(user_answer) != correct_answer:
                error_message(user_answer, user_name, correct_answer)
                return
            else:
                success_message()
        else:
            error_message(user_answer, user_name, correct_answer)
            return
    congrats_to_user(user_name)
    return


def get_common_division(first_randon_value, second_random_value):
    if first_randon_value == 0:
        return second_random_value
    return get_common_division(second_random_value % first_randon_value,
                               first_randon_value)
