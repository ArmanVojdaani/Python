import random
top = input("type a number")
if top.isdigit():
    top = int(top)
    if top <= 0:
        print("please type larger number nex time")
        quit()
    if top >= 1:
        print("ok thank you")
else:
    print("please type a number next time")
    quit()


random_number = random.randint(0, top)
guesses_counter = 0
while True:
    guesses_counter += 1
    user_guess = input("make a guess!")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type number")

    if user_guess == random_number:
        print("you got it")
        break
    else:
        if user_guess > random_number:
            print("you were above the number")
        else:
            print("you were below the number")


print("you guess", guesses_counter,  "times")
