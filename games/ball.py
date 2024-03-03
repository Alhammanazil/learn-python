import random
import main

def start():
    while True:
        box = "|__|"
        boxes = [box] * 4

        ball_position = random.randint(1, 4)

        tmp_boxes = boxes.copy()
        boxes[ball_position - 1] = "|0_0|"

        boxes = " ".join(boxes)
        tmp_boxes = " ".join(tmp_boxes)

        print(f'Please follow the ball in the boxes: \n\n{tmp_boxes}\n')

        user_choice = int(input("Where do you think the ball is? [1 / 2 / 3 / 4]: "))

        if user_choice not in [1, 2, 3, 4]:
            print("Invalid input. Please input a number between 1 and 4.")
            exit()

        if int(user_choice) == ball_position:
            print(
                f"🎉 Congratulations! You found the ball in the box number {ball_position}!"
            )
            print(f"{boxes}")
        else:
            print(f"Sorry! The ball was in the box number {ball_position}")
            print(f"{boxes}")
        play_again = input("Do you want to play again? [y/n]: ")
        if play_again.lower() != "y":
            main.menu()

if __name__ == "__main__":
    start()
