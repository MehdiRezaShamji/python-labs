# Question - Read an integer and print the sum of its digits using a loop, without converting it to a string.

# Predict before you run

# first we store the digits in a variable
# then create a loop where we add the first with second
# cant do this because its showing int object is not iterable

# okay so i understood that im trying to make a list of a single number, i though it would go like [1,2,3,4] but apparently thats not how it works, so i tried to split but we can only split str with it and i cant convert it to string according to the ruls.


num = int(input("Enter the digits: "))

while num == 0:
    num += num % 10
print(num)

# rough work
# i want to add first with second and so on
# it worked

# num = [1, 2, 3]

# for i in num:
#    i += i
# print(i)
