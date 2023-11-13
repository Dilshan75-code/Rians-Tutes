number=0
total=0
for number in range(5):
    try:
        number=int(input("Enter number = "))
        total+=number
    except ValueError:
        print("Invalid Input Enter valid number")
print("Total is ",total)