A = int(input('Give me a number over 100: ')) 
try:    
    if A <= 100:
        print(A, 'is not over 100')
    else:
        print(A,'is over 100')
except ValueError as e:
    print('please enter a number')





