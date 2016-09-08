# Lesson 3
# Collections and for loops

# Brackets [] denote a list
numbers = ["one", "two", "three"]

# Lists can be printed out like anything else
print(numbers)

# You can access specific items in a list with the syntax 'list_name[index]'
print(numbers[0])  # The first item has index 0, the second item index 1, and so on

# Adding two lists appends them together
numbers = numbers + ["four", "five"]
print(numbers)
# You can also use the append method to directly append a single item:
numbers.append("six")
print(numbers)

# You can also check the number of items in a list by checking its length
print(len(numbers))
# The built in len() function tells you the number of items in a collection

# Tuples are a second kind of collection, denoted with parens ()
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

# Unlike lists, tuples are "Immutable." This means that they can not be changed
# once created, so they are mostly useful for values that won't change, such
# as the days of the week.

# for loops are a second kind of loop, like while.
# Imagine we wanted to print out all of the days. Using while might look like this:
index = 0  # Remember, collections start at Item 0
while index < len(days):
    print(days[index])
    index += 1

# This technically works, but there's an easier way, for.

for num in numbers:
    print(num)

# The syntax of a for loop is: for 'item' in 'collection'
# For each value in collection, the code inside will be run with
# that value store in 'item'. Since we get the value directly, we
# don't have to use an index to look up the value like in the while loop

# End of Lessons 1-3

# Putting things together

secret = 58  # Shh, don't tell anyone
guesses = []  # An empty list
users_guess = -1  # We need a starting value, which you'll see in a second

while users_guess != secret:  # Ok, so we're going to loop until these values are equal
    users_guess = int(input("Guess a number 1-100? "))  # Read in an integer value from the user
    guesses.append(users_guess)  # Stick that guess into our list
    if users_guess > secret:            # If the guess is GREATER than secret
        print("You guessed too high")
    if users_guess < secret:            # If the guess is LESS than secret
        print("You guessed too low")

# Now we're back outside of that while loop, meaning the correct answer must have been guessed
print("You guessed it!")

# Since we saved all of the user's guesses, we can give them a score:
score = len(guesses)

print("It took you", score, "guesses")

if score == 1:
    print("Wow, you're lucky")
elif score < 5:
    print("You are pretty smart")
elif score < 10:
    print("You are pretty good at this")
else:
    print("Are you even trying?")

print("All of your guesses:", guesses)
