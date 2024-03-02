import random

welcome_message = "🟡 Hello, welcome to the game!"
ball_position = random.randint(1, 4)

print(welcome_message)
name = input("🔵 What is your name? ")
print("👋 Hi, Good to see you, " + name + "!")

box = "|__| "
boxes = [box] * 4

tmp_boxes = boxes.copy()

boxes[ball_position - 1] = "|0_0|"

print(f'''
Please take a look at the box below:
{' '.join(tmp_boxes)}
''')

user_choice = int(input("Where do you think the ball is? [1 / 2 / 3 / 4]: "))

if user_choice not in [1, 2, 3, 4]:
    print("Invalid input. Please input a number between 1 and 4.")
    exit()

user_confirmation = input(f"Are you sure you want to choose box number {user_choice}? [Yes / No]: ")

if user_confirmation.lower() == "no":
    print("Please re-enter the box number.")
    user_choice = int(input("Where do you think the ball is? [1 / 2 / 3 / 4]: "))
elif user_confirmation.lower() != "yes":
    print("Invalid input. Please input 'Yes' or 'No'.")
    exit()

if user_choice == ball_position:
    print(f"🎉 Congratulations, {name}! You found the ball in the box number {ball_position}!")
else:
    print(f"Sorry, {name}! The ball was in the box number {ball_position}")
    print(' '.join(boxes))
    