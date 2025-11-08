#Grade Calculator:
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale
from Tools.scripts.var_access_benchmark import B, C

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

num = int(input("enter num3"))
if num<=-1 or num>100 :
    print("enter valid input")
else :
    if 90 <= num <= 100:
        print('A')
    elif 80 <= num <= 90:
        print('B')
    elif 70 <= num <= 80:
        print('C')
    elif 60 <= num <= 70:
        print('D')
    elif 0 <= num <= 60:
        print('E')