hidden=6
import random
guess_number=random.randint(1,20)
while guess_number != hidden:
    print("guess number is not correct")
    guess_number=random.randint(1,20)
print("guessed number is corrcet")