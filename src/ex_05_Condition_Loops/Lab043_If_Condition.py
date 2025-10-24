#Write a program to take ą user age and
# let him know if he can go the club.
# 21

age = int(input("enter your age\n").strip())
if not age.isdigit():
    print("age must be an integer")
if age <= 0 or age > 100:
    print("enter valid age")

else :
    if age>=21 :
        print("go")

    else :
        print("not go")

    # Step 4. Check for the edge cases.
    # We should consider edge cases such as:
    # Negative ages or extremely high values -> program will break.
    # Non-numeric input - ABC
    # Age which is valid. > 130
    # Step 5. Optimize¡the code.
    # Handle all the edges.|


