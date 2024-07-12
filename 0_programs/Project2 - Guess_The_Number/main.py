from random import randint


def play():
    secret_number = randint(1, 100)
    guess = 0
    guess_count = 0

    print(
        "Welcome to Guess the number!!!\nYou have to guess the number between 1 and 100.\nYou can have as many tries as you want.\n")
    username = input("Enter your name: ")
    confirmation = input(f"Continue as {username}? (y/n): ")

    if confirmation.lower() != "y":
        print("Exiting...")
        exit()

    print("\n")

    while guess != secret_number:
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            print("Invalid input. Please enter a number.\n")

        if int != type(guess) or (guess < 1 or guess > 100):
            print("Invalid input. Please enter a number between 1 and 100.")
        else:
            if guess < secret_number:
                print("Guess a larger number!")
                guess_count += 1
            elif guess > secret_number:
                print("Guess a smaller number!")
                guess_count += 1

    print(f"{username} guessed the number in {guess_count} tries!")

    try:
        with open("high_scores.txt", "r") as file:
            high_scores = file.read()
            if high_scores == "":
                with open("high_scores.txt", "w") as f:
                    f.write(f"{username} guessed the number in {guess_count} tries")
            elif guess_count < int(high_scores):
                with open("high_scores.txt", "w") as f:
                    f.write(f"{username} guessed the number in {guess_count} tries")
    except FileNotFoundError:
        with open("high_scores.txt", "w") as f:
            f.write(f"{username} guessed the number in {guess_count} tries")

    replay = input("Do you want to play again? (y/n): ")
    if replay.lower() == "y":
        play()
    else:
        exit()


play()
