"""
Rock, Paper, Scissors Game Example

This is a Python Generated Game with a Twist!

https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/
"""

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ #
# Game Initializer
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ #

from random import randint

# Creates a list of playable options for the game. #
play = ["Rock", "Paper", "Scissors"]

# Assigns a random number to the computer #
bot = play[randint(0,2)]

# Set's the player to False at the beginning of the loop to start the program. #
player = False

# Enable Points #
bot_points = 0
player_points = 0
points_tied = 0

while player == False:
# To initalize the game we need to set the player to true. #
    print('Welcome to Rock, Paper, Scissors. Type quit to exit the program.')
    player = input("Rock, Paper, Scissors? ").title()
    if player == bot:
        print("Tie!")
        points_tied += 1
    elif player == "Rock":
        if bot == "Paper":
            print("Unfortunately, you lost.", bot, "covers", player)
            bot_points += 1
        else:
            print("Congrats, you won!", player, "crushes", bot)
            player_points += 1
    elif player == "Paper":
        if bot == "Scissors":
            print("Unfortunately, you lost.", bot, "cuts", player)
            bot_points += 1
        else:
            print("Congrats, you won!", player, "covers", bot)
            player_points += 1
    elif player == "Scissors":
        if bot == "Rock":
            print("Unfortunately, you lost.", bot, "crushes", player)
            bot_points += 1
        else:
            print("Congrats, you won!", player, "cuts", bot)
            player_points += 1
    elif player == "Quit":
        print()
        print("Game Statistics:")
        print(f"The player won {player_points} games, while the computer won {bot_points} games.")
        print(f"There were {points_tied} games tied.")
        quit()
    else:
        print("That's not an option. Please select the correct option.")
    # The player was set to true, in order for the loop to continue, we need to set the player to false. #
    player = False
    bot = play[randint(0,2)]
    print() # adds spacing for the loop. #