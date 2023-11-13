hidden=6
guess_number=int(input("enter number between 1-20 = "))
while guess_number != hidden:
    print("guess number is not correct")
    guess_number=int(input("enter number between 1-20 = "))
print("guessed number is corrcet")