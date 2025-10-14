
# Write a Python program to calculate the
# area of a circle given its radius using the formula
#area=nxr^2 *** ( Take pie as 3.14)

# i/p - r - float
# o/p -> string formatted output of area.

# String data formatting
radius = float(input("enter the radius of circle : \n "))
area = 3.14 * (pow(radius, 2))
area1 = 3.14 * (radius ** 2)
print("area of circle is : " ,area)
print(f"area of circle is :  ,{area:.3f}")  
print(f"Area of the circle is -> {area :. 2f}")
print(area1)


