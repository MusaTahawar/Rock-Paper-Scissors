import random

rounds = 3
player_wins = 0
comp_wins = 0

user_name = input("Enter Your Name: ")
choices = ["rock", "paper", "scissors"]

while player_wins < 2 and comp_wins < 2:
    comp_choice = random.choice(choices)
    user_choice = input("1. Rock, 2. Paper, 3. Scissors: ").lower()
    print(f"Comp Chose {comp_choice}")
    print(f"You Chose {user_choice}")

    if user_choice == comp_choice:
        print("It's a tie!")
    elif (user_choice, comp_choice) in [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]:
        print(f"{user_name} Wins!")
        player_wins += 1
    else:
        print(f"{user_name} Loses.")
        comp_wins += 1

print(f"Game Over! {user_name}: {player_wins}, Computer: {comp_wins}")
