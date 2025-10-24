age = int(input("enter your age\n").strip())
#if not age.isdigit():
 #   print("only integer accepted")
if age <= 0 or age > 100:
    print("enter valid age")

else :
    if(age>18) :
        print("allow")
    else :
        print("not allow")
