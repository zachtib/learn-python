# Lesson 1
# Variables, if/elif/else statements, while loops

# Run this program by pressing F9 and choosing lesson1
# Then use the F8 key to step through and observe the output in the Console pane

# Variable assignment

# The equals sign is the assignment operator. The value on the right will be stored
# into the named variable on the left. Think of the next line as instructing the computer
# that "greeting is equal to Hello"
greeting = "Hello"
name = "George"
age = 35

# The print function will let you display output to the user
print(greeting, name)
print("You are", age, "years old")

# Conditionals: if

# While a single = is used for assignment, == is used to compare
if age == 30:
    print("Wow, you're exactly 30. What are the odds?")
# The above will compare age to 30. If they are equal, the message will be printed

# This will check if age is OVER 30, and display an unfortunate truth to the user if so
if age > 30:
    print("You are old,", name)

# Conditionals: if/else
# If you follow an if statement with an else statement, the else statement will be executed in
# the event that the first condition is not met
if age >= 40:
    print("Wow, you are REALLY old!")
else:
    print("OK, not THAT old.")  # This line will be reached only if age is less than 40
# Standard comparison operators are ==, !=, <, >, <=, and >=

# Conditionals: if/elif/else
# elif is short for "else, if", and it's a way of chaining more than two conditions together
# For example:
if age < 20:
    print("You are under 20")
elif age < 40:
    print("You are at least 20, but under 40")
else:
    print("You are at least 40")
# Notice that once the program find a true condition, it will stop evaluating further elifs

# Loops: while
# Loops execute a set of statements UNTIL a condition is met
while age < 40:
    age = age + 1  # This will increase the value of age by 1
    print("Happy Birthday,", name)

# Poor George
print("Now you are old")

# End of Lesson 1

print("Now try it out yourself")
pass  # Pass does nothing. This is here to prevent you from stepping past the end of the file
# Exercise

# Create two variables here named 'a' and 'b' and assign numeric values to them


# Now create a variable called 'c' and set it to the sum of 'a' and 'b'

# Finally, display c to the user

# Finally, print a new message if c is greater than 10
