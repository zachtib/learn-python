# Lesson 0: What is a Program?

# Note: After writing the first few lessons, I felt the need to go back and do
# something more introductory, which is why this file is called lesson0.

# What is a program? Wikipedia defines a computer program as: "a collection of
# instructions that perform a specific task when executed by a computer," which 
# is actually a pretty good summary. The important part to focus on, especially
# if you're just starting out is the "collection of instructions" bit. Every 
# single computer program you've ever run is, at its core, a list of simple
# instructions that your computer is following, one after the other. While an
# individual instruction is often very simple, they can be put together to form
# more complex building blocks that you can then use to build your completed
# program.

# The following line of code is an example of a single programming instruction:
pass

# 'pass' is about the simplest and shortest complete instruction you can give 
# your computer in Python. It means "do nothing." In reality, there might not
# be a lot of practical reasons you'd want your computer to do nothing, so let's
# look at a slightly more complex example:
print("Hello, World")

# Now, that line of code actually did something. If you're running this file and
# take a look at your Console output, you should see the text "Hello, World"
# displayed. print() is what's known as a function. Functions take in values,
# perform tasks, and output different values. In this case, print() takes in
# what is called a "string value", or in other words, text. Most programming
# languages will offer some way of outputting text to the Console. In C#, the
# function is Console.Write(). In Java, it's System.out.print().
pass

# print() can output things besides text, like numbers:
print(100)
print(0.5)
print(3.14159)

# Each of those lines is a single instruction.
pass

# Variables
# Another core building block of programs are called variables. Variables store
# a value in memory to be accessed later. Considering the following line:
x = 3

# This tells the computer "x is equal to 3." "x" is a value that we have named,
# and could be just about anything we want to call it (with a few exceptions).
# We can define a second variable just like the first
y = 4

# As the name implies, variables can change their values. Assigning a new value
# to a variable in Python works just like assigning it the first time
x = 5

# From here on out, the value of x is 5. So, how do we use these variables?
# Well, we can print them out:
print(x)
print(y)

# Note the lack of quotation marks in those print statements. while print("x")
# would print out the literal character, x, print(x) will print out the value of
# x.
pass

# We can also use the value of variables to define new variables.
z = x + y
print(z)

# One important note, though. Once the value of z is defined here, updating x or
# y won't change it, see:
x = 2
print(z)

# One final note about print that will come up in later lessons: it can accept a
# list of items to display instead of just one at a time. The items will be 
# displayed on one line, separated by spaces:
print(x, y, z)
