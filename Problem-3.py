# Question - Read three numbers and print the largest one without using max().

# 1. Make a variable called biggest. Put the first number into it.
# 2. If the second number is bigger than biggest:
#        put the second number into biggest
# 3. If the third number is bigger than biggest:
#        put the third number into biggest
# 4. Print biggest

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

biggest = x
if y > biggest:
    biggest = y
if z > biggest:
    biggest = z

print(biggest)
