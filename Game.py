#Rock Paper Scissors

# random module
import random

# winning pattern
win = [("scissors","paper"),("paper","rock"),("rock","scissors")]

# Difficulty levels
difficulty = input("Choose difficulty level (easy, intermediate, hard): ").lower()

# Set computer decision-making process based on difficulty level
if difficulty == "easy" or difficulty == "intermediate":
    computer_decision = random.choice
elif difficulty == "hard":
    def computer_decision():
        if player_input == "rock":
            return "paper"
        elif player_input == "paper":
            return "scissors"
        elif player_input == "scissors":
            return "rock"
else:
    print("Invalid difficulty level. Setting to easy.")
    computer_decision = random.choice

# game instruction
print("\nThere are 6 round.\nYou are playing against the computer.\nYou will win if you have highest point.")

# choices for computer to select
choices = ["rock","paper","scissors"]

# count for rounds
count = 0

# player score
player_points = 0

# computer score
computer_points = 0

# rounds to be valuated
while count != 6:
    
    print("\nRound : ", count+1)
    player_input = input("\nSelect your move.... : ").lower()
    computer_input = random.choice(choices)
    
# show the choossed option for each
    print(" ")
    print("Player Input : ","🪨" if player_input == "rock" else ("📜" if player_input == "paper" else "✂️"))
    print("Computer Input : ","🪨" if computer_input == "rock" else ("📜" if computer_input == "paper" else "✂️"))

# check for patterns and who wins Calculations

    if player_input != computer_input:
        player_wins = (player_input,computer_input) #(rock,paper)
        computer_wins = (computer_input,player_input) #(paper,rock)
        
        if player_wins in win:
            print(f"\n{player_input.capitalize()} beats {computer_input}. \nYou Won!")
            player_points += 1
        elif computer_wins in win:
            print(f"\n{computer_input.capitalize()} beats {player_input}. \nComputer Won!")
            computer_points += 1
        else:
            print("Invalid Input of the Player. \nComputer won!")
            computer_points += 1
        
    elif player_input == computer_input:
        print("Draw, Player and Computer gets Half points")
        player_points += 0.5
        computer_points += 0.5
    print(" ")

# display the points for each    
    print("Player Score : ", player_points)
    print("Computer Score : ", computer_points)
    count += 1
    
# score validation
if player_points > computer_points:
    print("You are the Champion🏆")
elif player_points == computer_points:
    print("You both are Champion🏆💻")
else:
    print("Computer is the Champion💻")