import random
user_wins: 0
bot_wins = 0
options = ["paper", "rock", "scissors"]

user_input = input("Type rock or paper or scissors or type Q").lower()

random_number = random.randint(0, 2)
bot_pick = options[random_number]
print("the bot picks", bot_pick + ".")
