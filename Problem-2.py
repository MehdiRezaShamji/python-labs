# Question - Read a number and print whether it is positive, negative or zero.

# First i will ask for number using {input}
# then i wil create a logic where if the input is less than 0 than print negative, more than 0 than postive and equal to 0 than 0


x = int(input("Enter a number: "))
if x < 0:
    print("Negative")
elif x > 0:
    print("Positive")
else:
    print("Zero")
