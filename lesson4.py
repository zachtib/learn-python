# Lesson 4

# Hey! This file will execute in a different order than you might assume but don't worry,
# all will be explained in time

# Functions

# Take a look at the code below:
def sum(x, y):
    return x + y


# Two things you probably haven't seen before:

# def, short for 'define'. This means that we're defining a function.
# The function's name is immediately after def. In this case, it's "sum"
# After the function names are parens (), inside of which we declare the
# *inputs* of our function. In this case, we take in two: x and y

# Our function contains only one line of code. That line begins with 'return'
# return specifies the *output* of our function. In this case, sum is going
# to return the value of x plus y

# To summarize, we've *defined* a function, named "sum", that takes in two
# numbers, x and y, and returns their sum

# Here is another function, called main:
# In programs with multiple functions, it's customary to put the starting point
# of your program inside a function called main, like this:
def main():
    print("This is the beginning of our program")
    # Ok, this is all inside our main function now. While this is customary,
    # python itself doesn't know that. So, the very final line of this file
    # will be us calling main(). Of course, you could put the logic we're
    # about to run outside of any function and it would still work, this is
    # purely an organizational technique

    # Ok, let's do something. We're going to get two values from the user
    # This should look familiar. If not, look back at Lesson 2
    a = float(input("Give me a number: "))
    b = float(input("Give me another number: "))

    # Ok, we've got two floating point numbers. Remember, the program is assuming
    # the user is smart enough to type in a number, and will generate an error if
    # they do not

    # Let's create a new variable called c, and set it to the sum of a and b
    # To call a function you've defined, the syntax is: function_name(list, of, arguments)
    c = sum(a, b)

    # That's it! Let's show the result to the user
    print("The sum of your numbers is", c)

    # Functions are at their most useful when they contain a bit of logic you want to use
    # over and over again. For instance
    print("The sum of 3 and 5 is", sum(3, 5))
    print("The sum of 2 and 4 is", sum(2, 4))
    print("The sum of 2 and 2 is", sum(2, 2))

    # In this case, we've replaced such a simple bit of logic, we didn't save much typing
    # However, if we had replaced a more complex computation, we could have saved quite a bit

    # This is the end of our main function, which means the program will stop running now
    return

# As we mentioned earlier, we need to call the main function for it to run at all. So, we will
# do this at the end of the file.

main()


