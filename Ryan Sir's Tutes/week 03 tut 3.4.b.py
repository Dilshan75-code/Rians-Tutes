number=0
num1=0
symble="+","-","*","/"
anz=0

number=float(input("enter number = "))
symble=str(input("enter operator(+,-,*,/) = "))

if symble=="+":
    num1=float(input("enter number = "))
    anz=number+num1
    print("answer is = ",anz)
elif symble=="-":
    num1=float(input("enter number = "))
    anz=number-num1
    print("answer is = ",anz)
elif symble=="*":
    num1=float(input("enter number = "))
    anz=number*num1
    print("answer is = ",anz)
else:
    symble=="/"
    num1=float(input("enter number = "))
    if num1==0:
        print("Error")
    else:
        anz=number/num1
        print("answer is = ",anz)

