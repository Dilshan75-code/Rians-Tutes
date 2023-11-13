num=0
num1=0
sym="+","-","*","/"
ans=0

num=float(input("enter number = "))
sym=str(input("enter operator(+,-,*,/) = "))

if sym=="+":
    num1=float(input("enter number = "))
    anz=num+num1
    print("answer is = ",anz)
elif sym=="-":
    num1=float(input("enter number = "))
    anz=num-num1
    print("answer is = ",anz)
elif sym=="*":
    num1=float(input("enter number = "))
    anz=num*num1
    print("answer is = ",anz)
else:
    sym=="/"
    num1=float(input("enter number = "))
    try:
        num1!=0
        anz=num/num1
        print("answer is = ",anz)
    except ZeroDivisionError:
        print("ZeroDivision Error")

#answes

#enter number = 5
#enter operator(+,-,*,/) = /
#enter number = 0
#ZeroDivision Error
        