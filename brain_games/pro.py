import random
from brain_games.repeated_steps import *


def brain_pro():
    user_name = get_user_name_and_say_hello_to_user()
    set_game_rules('What number is missing in the progression?')
    for i in range(0, 3):
        random_position = random.randint(0, 10)
        random_length = random.randint(5, 11)
        if random_position > random_length:
            random_position = random_length
        start_value = create_random_value()
        common_difference = random.randint(1, 3)
        random_values = create_random_progression(random_position, random_length, start_value, common_difference)
        user_answer = get_user_answer(' '.join([str(n) for n in random_values]))
        correct_answer = get_missing_value(start_value, common_difference, random_position)
        if str(user_answer) != str(correct_answer):
            error_message(user_answer, user_name, correct_answer)
            return
        else:
            success_message()
    congrats_to_user(user_name)
    return


def create_random_progression(random_position, random_length, start_value, common_difference):
    random_values = [start_value]
    for k in range(0, random_length):
        current_value = start_value + common_difference
        random_values.append(current_value)
        start_value = current_value
    random_values[random_position] = ".."
    return random_values


def get_missing_value(start_value, common_difference, random_position):
    return start_value + random_position * common_difference


