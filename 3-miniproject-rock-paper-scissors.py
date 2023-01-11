import random
user_wins = 0
bot_wins = 0
equal = 0
options = ["paper", "rock", "scissors"]

while True:

    user_input = input("Type rock or paper or scissors or type Q").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    bot_pick = options[random_number]
    print("the bot picks", bot_pick + ".")

    if user_input == "rock" and bot_pick == "scissors":
        print("You won")
        user_wins += 1

    elif user_input == "scissors" and bot_pick == "paper":
        print("You won")
        user_wins += 1

    elif user_input == "paper" and bot_pick == "rock":
        print("You won")
        user_wins += 1

    elif user_input == bot_pick:
        print("You both choose same , try more")
        equal += 1
    else:
        print("computer won You lost")
        bot_wins += 1

print("you won", user_wins, "Times")
print("computer wons", bot_wins, "Times")
print("equals", equal, "Times")
print("Goodbye")
