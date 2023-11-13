while True:
 A = input("Please enter an integer: ")
 try:
    A = int(A)
    break
 except ValueError:
    print("Requires a valid integer! Please try again.")
print("You successfully entered an integer.")