import random

welcome_message = "🟡 Hello, welcome to the game!"
ball_position = random.randint(1, 4)

print(welcome_message)
name = input("🔵 What is your name? ")
print("👋 Hi, Good to see you, " + name + "!")

print(f'''
Please take a look at the box below:
📦  📦  📦  📦
 1   2   3   4
 ''')

user_choice = int(input("Where do you think the ball is? [1 / 2 / 3 / 4]: "))

if user_choice not in [1, 2, 3, 4]:
    print("Invalid input. Please input a number between 1 and 4.")
    exit()

user_confirmation = input(f"Are you sure you want to choose box number {user_choice}? [Yes / No]: ")
if user_confirmation.lower() == "no":
    print("Please re-enter the box number.")
    user_choice = int(input("Where do you think the ball is? [1 / 2 / 3 / 4]: "))

if int(user_choice) == ball_position:
    print(f"🎉 Congratulations, {name}! You found the ball in the box number {ball_position}!")
else:
    print(f"Sorry, {name}! The ball was in the box number {ball_position}.")