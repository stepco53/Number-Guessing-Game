# Number Guessing Game
# ask the user to guess a number between 1 and 100
# if the guess is too low, print "Too low! Try again."
# if the guess is too high, print "Too high! Try again."
# if the guess is correct, print "Congratulations! You've guessed the number!"
# after user guesses the number, print how many attempts it took
# print the user's probability for guessing the number correctly
# ask the user wanna play again
import random


def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while not guessed_correctly:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(
                    f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts!"
                )
        except ValueError:
            print("Please enter a valid integer.")

    probability = 1 / (100 / attempts) if attempts > 0 else 0
    print(f"Your probability of guessing the number correctly is: {probability:.2f}")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        number_guessing_game()
    else:
        print("Thank you for playing! Goodbye!")


if __name__ == "__main__":
    number_guessing_game()
