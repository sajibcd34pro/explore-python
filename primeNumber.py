# get prime number using python
number = int(input("type your number:"))
div = 2
if(div<number):
    if(number % div ==0):
        print("Non Prime")
    elif(number% div != 0):
        div = div +1
        print("prime")
    
# get prime number using elif

number2 = int(input("type your number:"))
division = 2

if(division<number2 and number2 % division==0):
    print("Non prime number")
else:
    division = division + 3
    print("prime number")