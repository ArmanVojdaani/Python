print("Hello Human")
playing = input("Do you want to play? ")

if playing != "yes":
    quit()
else:
    print(" ok, lets play:) ")
answer = input("What does cpu stand for? ")
# q1
if answer.lower() == "central proccessing unit":
    print("correct")
else:
    print("incorrect")

# q2
answer = input("What does gpu stand for? ")
if answer == "graphics proccessing unit":
    print("correct")
else:
    print("incorrect")

# q3
answer = input("What does ram stand for? ")
if answer == "random access memory":
    print("correct")
else:
    print("incorrect")
# 4
answer = input("What does psu stand for? ")
if answer == "power supply":
    print("correct")
else:
    print("incorrect")
