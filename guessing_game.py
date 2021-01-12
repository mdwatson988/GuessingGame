import random


# create functions necessary to play the game
def flip_coin():
    coin = random.randint(0, 1)
    if coin == 0:
        return "Heads"
    return "Tails"


def get_user_flip_choice():
    while True:
        user_flip_input = input('\nPress "H" to choose Heads or "T" to choose Tails.\n')
        if user_flip_input == "H" or user_flip_input == "h":
            user_flip_choice = "Heads"
            return user_flip_choice
        elif user_flip_input == "T" or user_flip_input == "t":
            user_flip_choice = "Tails"
            return user_flip_choice
        print('Sorry, invalid selection.')


def roll_die():
    roll = random.randint(1, 6)
    return roll


def get_user_die_choice():
    while True:
        user_die_input = input('\nChoose a number between 1 and 6. Enter your choice on your keyboard.\n')
        try:
            user_die_input_int = int(user_die_input)
            if user_die_input_int in range(1, 7):
                return user_die_input_int
            else:
                print('Sorry, invalid selection.')
                break
        # additional catch for inappropriate entry of non-numeric string
        except ValueError:
            print('Sorry, invalid selection.')
            break


def guessed_correctly(guess, result):
    if guess == result:
        return True
    return False


def choose_game():
    while True:
        game_choice_input = input("\n\nWould you like to guess the results of a coin flip or a six sided die?"
                                  '\nPress "C" for coin flip or "D" for die.\n')
        if game_choice_input == "C" or game_choice_input == "c":
            user_game_choice = "Coin"
            return user_game_choice
        elif game_choice_input == "D" or game_choice_input == "d":
            user_game_choice = "Die"
            return user_game_choice
        print('Sorry, invalid selection.')


# Start the game
print(
    "\n\nStep right up and test your luck! Welcome to the New and Improved Guessing Game!")

# Set variable to keep track of score
num_guessed = 0
num_correct = 0
play_again = 0

while play_again == 0:
    # have user select game
    game_choice = choose_game()

    # play coin flip game
    if game_choice == "Coin":
        print("\nYou've chosen the coin flip guessing game.")

        flip = flip_coin()
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

    # play six sided die game
    elif game_choice == "Die":
        print("\nYou've chosen the six sided die guessing game.")

        die_result = roll_die()
        choice = get_user_die_choice()

        # Inform user of choice and die roll results
        for i in range(1, 7):
            if i == choice:
                print("You chose {}.".format(i))
                break
        for i in range(1, 7):
            if i == die_result:
                print("The die roll was {}.\n".format(i))
                break

        # Check die vs choice and update tallies
        if guessed_correctly(choice, die_result):
            print("Congratulations! You guessed correctly!")
            num_guessed += 1
            num_correct += 1
        else:
            print("Sorry, you guessed incorrectly.")
            num_guessed += 1

    # Inform users of totals
    percent_correct: float = (num_correct / num_guessed) * 100
    print(
        "You've guessed {c} correctly out of a total of {g} guesses, or {p}% correct.".format(c=num_correct,
                                                                                              g=num_guessed,
                                                                                              p=percent_correct))
    # Play again?
    replay = input('\nWould you like to play again?\nPress "N" to stop playing or any other key to continue.\n')
    if replay == "N" or replay == "n":
        play_again = 1