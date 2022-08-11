import random
from brain_games.cli import *


def get_user_name_and_say_hello_to_user():
    return welcome_user()


def set_game_rules(game_rules):
    return print(game_rules)


def create_random_value():
    return random.randint(0, 100)


def get_user_answer(randon_value):
    print("Question: " + str(randon_value))
    return prompt.string("Your answer: ")


def congrats_to_user(user_name):
    return print("Congratulations, " + user_name + "!")


def error_message(user_answer, user_name, correct_answer):
    print(
        "\"" + str(user_answer) + "\"" + " is wrong answer ;(. Correct answer was " + "\"" + str(correct_answer)
        + "\"" + ".\nLet's try again, " + str(user_name) + "!")


def success_message():
    print("Correct!")
