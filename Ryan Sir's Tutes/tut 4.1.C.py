hidden=6
import random
guess_number=int(input("guess a number = "))
while guess_number != hidden:
    if guess_number<hidden:
        print("guess number is too low")
    else:
        print("guess number is too high")
    guess_number=int(input("guess a number = "))
print("guessed number is corrcet")