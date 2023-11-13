#a)
temp_C=0
temp_f=0
number=0
number=int(input("Enter number 1 to calculate  from Celsius to Fahrenheit , number 2 to calculate from Fahrenheit to Celsius = "))
if number==1:
    temp_c=float(input("Enter temperature in celsius = "))
    temp_f= (temp_c * 1.8) + 32
    print("temperature in Fahrenheit is = ",temp_f)
elif num==2:
    temp_f=float(input("Enter temperature in Fahrenheit = "))
    temp_c = (temp_f - 32) / 1.8
    print("temperature in celsius is = ",temp_c)
else:
    print("invalid option enterd" )




