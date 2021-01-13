import random


# create functions necessary to play the game
def flip_coin():
    coin = random.randint(0, 1)
    if coin == 0:
        return "Heads"
    return "Tails"


def get_user_flip_choice():
    while True:
        user_input = input('\nPress "H" to choose Heads or "T" to choose Tails.\n')
        if user_input == "H" or user_input == "h":
            user_choice = "Heads"
            return user_choice
        elif user_input == "T" or user_input == "t":
            user_choice = "Tails"
            return user_choice
        else:
            print('Sorry, invalid selection.')


def guessed_correctly(guess, result):
    if result == guess:
        return True
    return False


# Start the game
print(
    "\n\nStep right up and test your luck! Welcome to the Coin Flip Guessing Game!"
    "\n\nGo ahead and make your first guess!")

# Set variable to keep track of score
num_guessed = 0
num_correct = 0
play_again = 0
while play_again == 0:
    flip = flip_coin()
    # Get user input
    choice = get_user_flip_choice()
    if choice == "Heads":
        print("You guessed Heads.")
    else:
        print("You guessed Tails.")
    # Inform user of result of coin flip
    if flip == "Heads":
        print("The coin came up Heads.\n")
    else:
        print("The coin came up Tails.\n")

    # Check coin vs choice and update tallies
    if guessed_correctly(choice, flip):
        print("Congratulations! You guessed correctly!")
        num_guessed += 1
        num_correct += 1
    else:
        print("Sorry, you guessed incorrectly.")
        num_guessed += 1

    # Inform users of totals
    percent_correct: float = (num_correct / num_guessed) * 100
    print(
        "You've guessed {c} correctly out of a total of {g} guesses, or {p}% correct.".format(c=num_correct, g=num_guessed,
                                                                                      p=int(percent_correct)))
    # Play again?
    replay = input('\nWould you like to play again?\nPress "N" to stop playing or any other key to continue.\n')
    if replay == "N" or replay == "n":
        play_again = 1
