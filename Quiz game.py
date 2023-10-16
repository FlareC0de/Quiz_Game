print("Welcome to the Quiz Show!!!! Im your host C0d3r")

playing = input("Do you want to compete?? ")

if playing.lower() != "yes":
    quit()

print("Lets Go!!! :)")
score = 0

answer = input("Who holds the most points scored in a NBA game? ")
if answer == "Wilt Chamberlain":
    print("That's Correct")
    score += 1
else:
    print("That's Wrong!!")

answer = input("Who started the Nike shoe brand?")
if answer == "Phil Knight":
    print("Outstanding, your a genius")
    score += 1
else:
    print("AHHHH!!, thats wrong champ, try again next time")

answer = input("What does GM stand for??")
if answer == "General Motors":
    print("Who's the genius?? You are")
    score += 1
else:
    print("Who's the genius? Your not")

answer = input("What does NFL stand for??")
if answer == "National Football League":
    print("Your on a Roll!!")
    score += 1
else:
    print("Today's just not your day, huh?")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100 ) + "%.")





