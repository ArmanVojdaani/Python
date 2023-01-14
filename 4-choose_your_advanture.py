name = input("type your name please")
print("welcome", name, "to this advanture")
answer = input(
    "you are in dirt road , it has come to an end and you can go left or right, which way would you like to go?   ").lower()


if answer == "left":
    answer = input(
        "you come to a river , you can swim across or walk around , please type you like to SWIM or WALK ?  ").lower()
    if answer == "walk":
        print("you walked many miles you ran out of water and you lose the game")
    elif answer == "swim":
        print("you swam across and eaten by aligator")


elif answer == "right":
    answer = input(
        "you come to a bridge it looks wobbly do you want to cross it or head back ? (cross/ back) ? ").lower()
    if answer == "back":
        print("you go back to main road. you lose")
    elif answer == "cross":
        answer = input(
            "you cross the bridge and meet stranger. do you talk to them? (yes/no)?  ").lower()
        if answer == "yes":
            print("you talk to strangers and they yo gold. so",
                  "\033[35m",  "YOU WIN!!!", "\033[0m")
        elif answer == "no":
            print("you ignored the strangers and they are offended and you ",
                  "\033[35m", "LOSE !!!", "\033[0m")
        else:
            print("888not a valid option, you lose")
    else:
        print("999not a valid option, you lose")

else:
    print("666not a valid option, you lose")

print("thank you for trying", name)
