import random
scores = [0, 0]
choices = ["r", "p", "s"]


def get_user_choice():
    """
    A function that prompts the user  for a choice of 'r', 'p', or 's', converts the input to lowercase, and
    checks if the input is valid. If the input is not valid, it prompts the user again until it returns the
    user's choice.
    """
    user_input = input("Enter a choice (r, p, s): ")
    user_input = user_input.lower()
    while user_input not in choices:
        print("Invalid input. Please try again.")
        user_input = input("Enter a choice (r, p, s): ")
        user_input = user_input.lower()
    return user_input


def is_win(user, computer):
    """
    A function that determines the winner between the user and the computer based on their choices.

    Parameters:
    user (str): The choice of the user - 'r' for rock, 'p' for paper, or 's' for scissors.
    computer (str): The choice of the computer - 'r' for rock, 'p' for paper, or 's' for scissors.

    Returns:
    bool: True if the user wins, False otherwise.
    """
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True
    else:
        return False


def play(user, computer):
    """
    Determines the outcome of a game between a user and a computer.

    Parameters:
        user (str): The choice of the user - 'r' for rock, 'p' for paper, or 's' for scissors.
        computer (str): The choice of the computer - 'r' for rock, 'p' for paper, or 's' for scissors.

    Returns:
        str: The outcome of the game. Possible values are:
            - "It's a tie" if the user and computer have the same choice.
            - "You won!" if the user wins.
            - "You lost!" if the user loses.
    """
    if user == computer:
        return "It's a tie"
    elif is_win(user, computer):
        scores[0] += 1
        return "You won!"
    else:
        scores[1] += 1
        return "You lost!"


print("Let's play Rock, Paper, Scissors!")
rounds = int(input("Enter the number of rounds: "))
print("\n")

for i in range(rounds):
    print(f"Round {i+1}:")
    user_choice = get_user_choice()
    computer_choice = random.choice(choices)
    print(play(user_choice, computer_choice))
    print("\n")

print("\n\n")

if scores[0] > scores[1]:
    print("You won this championship!!!")
elif scores[0] < scores[1]:
    print("You lost this championship...")
else:
    print("No one won this championship... It's a tie")
