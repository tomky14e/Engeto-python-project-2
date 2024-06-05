"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Tomáš Matějíček
email: tomas.matejicek@hotmail.com
discord: tomas_38052
"""

import os
from time import time
from random import sample

def generate_random_number() -> str:

    while True:

        random_number = "".join(str(number) for number in sample(range(10), 4))

        if not random_number.startswith("0"):

            break

    return random_number


def get_user_input() -> str:

    user_input = input(">>> ")

    return user_input


def print_welcome_banner() -> str:

    separator: str = "\n" + ("-" * 50)

    print(
        f"\nWelcome to Bulls & Cows game!",
        separator,
        f"\nI'll generate a 4-digit random number for you",
        separator,
        f"\nYour task is to guess the number:\n",
        f"\n- Number of Bulls means the number\n  of numbers guessed and their order"
        f"\n- Number of Cows means the number\n  of guessed numbers"
        f"\n- Number must be 4-digit",
        f"\n- Number cannot contain duplicate values",
        f"\n- Number cannot starts with zero",
        separator,
        f"\nType 'quit' or 'q' to quit the game",
        f"\nType 'clean' or 'c' to clean terminal",
        separator,
        f"\n\nEnter your number:\n",
    )


def print_end_banner(game_time: float, attempts: int) -> str:

    separator: str = "\n" + ("-" * 50)

    print(
        f"Congratulations!",
        f"\nYou did it in {game_time}",
        f"{'second' if game_time == 1 else 'seconds'}",
        f"and {attempts}",
        f"{'try' if attempts == 1 else 'tries'}",
        separator
    )


def validate_user_input(user_number: str) -> str:

    if not user_number:

        raise ValueError("Number cannot be empty")

    elif not user_number.isdigit():

        raise ValueError("Number cannot contain non-numeric values")

    elif len(user_number) != 4:

        raise ValueError("Number must be 4-digit")

    elif len(set(user_number)) != 4:

        raise ValueError("Number cannot contain duplicate values")

    elif user_number.startswith("0"):

        raise ValueError("Number cannot starts with 0")

    else:

        return user_number


def check_game_conditions(random_number: str, user_number: str) -> dict:

    score = {"bulls": 0, "cows": 0}

    for random_num, user_num in zip(random_number, user_number):

        if random_num == user_num:
            score["bulls"] += 1
        elif user_num in random_number:
            score["cows"] += 1

    return score


def print_game_conditions(score: dict) -> str:

    separator: str = "\n" + ("-" * 50)

    print(
        f"{score['bulls']}",
        f"{'bull' if score['bulls'] == 1 else 'bulls'}",
        f"{score['cows']}",
        f"{'cow' if score['cows'] == 1 else 'cows'}",
        separator,
    )


def game_loop():

    separator: str = "\n" + ("-" * 50)
    random_number: str = generate_random_number()
    user_input: str = ""
    user_number: str = 0
    attempts: int = 0
    game_time_start: float = time()
    game_time: float = 0

    print_welcome_banner()

    while user_number != random_number:

        attempts += 1

        try:

            user_input = get_user_input()

            if user_input == ("quit") or user_input == ("q"):

                exit()

            elif user_input == ("clean") or user_input == ("c"):

                if os.name == "nt":

                    os.system("cls")
                    continue

                else:

                    os.system("clear")
                    continue

            else:

                user_number = validate_user_input(user_input)

        except ValueError as val_err:

            print(val_err, separator)

            continue

        except KeyboardInterrupt:

            break

        else:

            if user_number != random_number:

                print_game_conditions(check_game_conditions(random_number, user_number))

            else:

                game_time = round(time() - game_time_start, 1)

                print_end_banner(game_time, attempts)

                


if __name__ == "__main__":

    game_loop()
