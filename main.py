from libs import welcome_message, exit_program
from games import ball, rsp, guess, stall

def menu():
    user_option = int(input("\nWhat game would you like to play?:\n1. Ball\n2. Rock Scissors Paper\n3. Guess Number\n4. Stall\n5. Exit\n\ninput number of game: "))
    if user_option == 1:
        ball.start()
    elif user_option == 2:
        rsp.start()
    elif user_option == 3:
        guess.start()
    elif user_option == 4:
        stall.start()
    elif user_option == 5:
        exit_program()
    else:
        print("Invalid input. Please input a number between 1 and 2.")

def main():
    welcome_message()
    menu()

if __name__ == "__main__":
    main()