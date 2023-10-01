import random 
options = ["Rock", "Paper", "Scissors"] 
user_choice = input("Choose Rock, Paper, or Scissors: ") 
computer_choice = random. choice(options) 
print("You chose: ", user_choice) 
print("Computer chose: ", computer_choice) 
if user_choice == computer_choice: print("It's a tie!")
