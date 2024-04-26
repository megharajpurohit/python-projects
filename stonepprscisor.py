import random

print("Welcome to the Stone Paper Scissor game!")

choices = ["stone", "paper", "scissor"]

while True:
    user_choice = input("Enter your choice (stone/paper/scissor/q to quit): ").lower()
    if user_choice == "q":
        print("You have successfully quit the game.")
        break
    if user_choice not in choices:
        print("Invalid input. Please enter a valid choice.")
        continue

    computer_index = random.randint(0, 2)
    computer_choice = choices[computer_index]
    print("Computer picked", computer_choice + ".")

    if user_choice == "stone" and computer_choice == "scissor":
        print("You win!")
    elif user_choice == "paper" and computer_choice == "stone":
        print("You win!")
    elif user_choice == "scissor" and computer_choice == "paper":
        print("You win!")
    elif user_choice == computer_choice:
        print("It's a draw!")
    else:
        print("You lose!")