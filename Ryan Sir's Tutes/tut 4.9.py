number=0
while True:
    print("Menu \n select on option entering nmber")
    print("1.Option 1")
    print("2.Option 2")
    print("3.Option 3")
    print("Quit")
    try:
        number=int(input("Enter selected number = "))
        if number==1:
            print("1 selected")
        elif number==2:
            print("2 selected")
        elif number==3:
            print("3 selected")
        else:
            print("Option not recognised")
    except ValueError:
        print("invalid input, enter integer")
    break
    

