import random
import main

def start():
    # Create a list of options for the game
    Glist = ["Rock", "Scissors", "Paper"]

    # Randomly choose an option using random.choice
    computer = random.choice(Glist)

    # Set player to False
    player = False

    while not player:
        # Set player to True
        player = input("Rock, Scissors, Paper? (Type 'exit' to quit): ")
        
        if player.lower() == "exit":
            main.menu()
        
        if player == computer:
            print("It's a tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose!", computer, "smashes", player)
            else:
                print("You win!", player, "cuts", computer)
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cuts", player)
            else:
                print("You win!", player, "covers", computer)
        else:
            print("Invalid input...")

        # Set player to False again to continue the loop
        player = False
        computer = random.choice(Glist)

if __name__ == "__main__":
    start()