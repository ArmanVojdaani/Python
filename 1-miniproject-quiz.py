print("Hello Human")
score = 0
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
else:
    print(" ok, lets play:) ")
answer = input("What does cpu stand for? ")
# q1
if answer.lower() == "central proccessing unit":
    print("correct")
    score += 1
else:
    print("incorrect")

# q2
answer = input("What does gpu stand for? ")
if answer.lower() == "graphics proccessing unit":
    print("correct")
    score += 1
else:
    print("incorrect")

# q3
answer = input("What does ram stand for? ")
if answer.lower() == "random access memory":
    score += 1
    print("correct")
else:
    print("incorrect")
# 4
answer = input("What does psu stand for? ")
if answer.lower() == "power supply":
    score += 1
    print("correct")
else:
    print("incorrect")

# end of question

print(" you got " + str(score) + " question correct")
print("equal to " + str(score/4*100) + "percent")
