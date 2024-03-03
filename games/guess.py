import random
import main

def start():
    def guess_number():
        secret_number = random.randint(1, 10)
        guess = None
        guess_count = 0
        max_guesses = 10

        print("Welcome to the Guess Number game!")
        print("I have chosen a number between 1 and 10. Try to guess the number!")

        while guess != secret_number and guess_count < max_guesses:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            guess_count += 1

            if guess < secret_number:
                print("Your guess is too low. Try again!")
            elif guess > secret_number:
                print("Your guess is too high. Try again!")

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {guess_count} attempts.")
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() == "yes":
                guess_number()
            elif play_again.lower() == "no":
                main.menu()
            else:
                print("Invalid input. Please input 'yes' or 'no'.")
        else:
            print(f"Sorry, you ran out of guesses. The secret number was {secret_number}.")

    guess_number()

if __name__ == "__main__":
    start()