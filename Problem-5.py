# Question - Read a number and print its multiplication table from 1 to 10.

# first i will create a variable called number where it takes a number from user
# then i will wite a loop where for each item in range(1, 11)
# multiply the item with the number
# the final print will look something like this -
# number x item = number * item
# this will give - 7 x 1 = 7
# this will go on to 10 as this is a loop

number = int(input("Enter a number to get the multiplication: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
