# Question - Read a name and an age from the user. Print one sentence saying how old that person will be in 10 years.


# PREDICT BEFORE YOU RUN

# First i will ask for name and store it in name variable
# Then i will ask for age and store it in age variable and wrap it under int function
# Then i will create a variable called updated age where i will add the current age with 10
# Then i will create a variable called output where i will form the entire sentence in a formatted string
# Then i will print the output

name = input("Enter your name: ")
age = int(input("Enter your age: "))
updated_age = age + 10

output = f"{name} will be {updated_age} in 10 years."
print(output)
