import random

print("************************************")
print("*** Welcome to the Guessing Game ***")
print("************************************")

hiddenNumber = random.randrange(1,102)
totalTries = 5
round = 1

while round <= totalTries:
    print(f"Round {round} of 5")

    guess = int(input("What number am I thinking of? "))
    showNumber = print(f"You said {guess}")

    # we can write the boolean factors like this to leave the logic somewhat cleaner.
    greater = hiddenNumber < guess
    lower = hiddenNumber > guess
    bullseye = hiddenNumber == guess


    if bullseye:
        print("You got it! GG!")
    else:
        if greater:
            print("Your guess was higher than my number!!")
        elif lower:
            print("Your guess was lower than my number!!")

    round += 1

print("Game Over")