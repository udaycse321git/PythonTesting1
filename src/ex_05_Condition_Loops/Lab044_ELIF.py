# Find the positive number is even or odd
num =int(input("enter num").strip())
if(num>0) :
    if(num % 2 == 0) :
        print("even")
    else :
        print("odd")
else :
    print("enter valid input")

#convert into ternary one line code
if(num>0) :

        print("even" if num % 2 == 0 else "odd")

else :
    print("enter valid input")