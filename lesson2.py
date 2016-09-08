# Lesson 2
# User input, Augmented assignment, basic math, imports

# Getting input from the User

greeting = "Hello"
name = input("What is your name? ")
print(greeting, name)

# input() returns a string, or text, value
# if we want a numeric input, we will have to convert it

age = input("What is your age? ")  # age is a string
age = int(age)  # age is an integer

# Note that this conversion will throw an error if the user enters a non-numeric value
# For now, we'll leave this alone, and hope that your user doesn't enter "potato"

# Now let's compute something for the user

# Augmented Assignment
# The += operator adds the value to the specified value and re-stores it
age += 1  # This is equivalent to 'age = age + 1'
print("Next year you will be", age)

# Math

# Unlike the above example with age, we can simply do the conversion from text to number inline
# This allows our code to be more concise, and doesn't bother storing the text value in memory
a = float(input("Enter a value for a: "))
b = float(input("Enter a value for b: "))
# A float is a floating-point numeric value

# Let's compute the pythagorean theorem for these values

# ** is the power operator. So, you would express "a squared" as "a**2"
c = (a**2 + b**2)**0.5
# We can't directly assign a value to "c squared", so we have to get the square root of the
# a^2 + b^2 side by raising it to the .5 power, then assign that value to c
print("Value of c is: ", c)

# Alternatively, we can import some functions from the math library and achieve the same result
from math import sqrt
from math import pow

c = sqrt(pow(a, 2) + pow(b, 2))
print("Value of c is: ", c)
