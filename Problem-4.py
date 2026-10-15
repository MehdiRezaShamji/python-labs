# Question - Read marks out of 100 and print a grade: A for 90 and above, B for 75 to 89, C for 60   to 74, D for 40 to 59, F below 40.

# Make a variable called marks that takes a number from user
# now make a logic where if the marks is 90 or above print A grade
# same with B for 75 to 89, C for 60   to 74, D for 40 to 59, F below 40

marks = int(input("Enter the marks out of 100: "))

if 100 >= marks >= 90:
    print("A grade")
elif 89 >= marks >= 75:
    print("B grade")
elif 74 >= marks >= 60:
    print("C grade")
elif 59 >= marks >= 40:
    print("D grade")
elif 39 >= marks >= 0:
    print("F grade")
else:
    print("invalid marks")
