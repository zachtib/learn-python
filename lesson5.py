# Lesson 5

# Objects

# Python is an object-oriented language. This mean that it uses, well, objects

# The simplest object is created with object()
o = object()

# Well, that's boring. Let's see what happens if we try to print it
print(o)


# That should have printed out something along the lines of <object object at 0x7f1e6784e170>
# Basically all that means is, this is an object of type object, and it's at this location
# in memory. This is the default value that Python will print out for objects that don't
# have a better description

# While simple values like integers and strings are easy to express and print out,
# objects are more complex. Later in this lesson, we'll write some code for our objects so
# that they generate a better description of themselves

# So, what is an object?

# An object is a collection of variables and functions that work together. You've already been
# exposed to both variables and functions, so let's dive in

# The built in object() doesn't really provide anything useful, so let's create our own

# Objects are defined by a template, called a class:
class MyObject:
    pass


# This is the simplest class we could make, and it's functionally the same as object(). We can
# create an instance of it just like with object():

m = MyObject()
print(m)


# Note that when it's printed, we see the new class's name

# So, let's create a more complex class. This will be a good chunk of code, so we'll go through
# it one step at a time. Our class is going to have three functions

class Point:
    # __init__ is a special python function name for an object's constructor. A constructor is
    # called when an object is created. The first argument of any function in an object is self,
    # which is a reference to the object. We have two additional arguments, x and y
    def __init__(self, x, y):
        self.x = x  # Note the difference between self.x (our object's internal value) and x (the value passed in)
        self.y = y
        # So, our constructor is pretty simple. It takes in two values and stores them

    # Like __init__, __str__ is a special function name that determines how an object should be described. This will
    # give us much nicer output when we try to print our objects
    def __str__(self):
        # in this case, we're using standard (x,y) point notation. Note we have to convert the ints to strings
        return "(" + str(self.x) + "," + str(self.y) + ")"

    # Now we'll define a completely custom function that returns the distance from our point to another

    def distance(self, other):
        """ Simple pythagorean theorem, right? """
        # Let's compute the difference in x and y values first:
        dx = self.x - other.x
        dy = self.y - other.y
        # Notice that we can access both x and y values of ourself and the other Point
        # Now add the squares
        dsq = dx**2 + dy**2
        # Finally, return the square root of that
        return dsq**.5


# Ok, so, we've defined a class. Now lets make some instances of it

p1 = Point(0, 0)
p2 = Point(3, 4)
p3 = Point(5, 7)

# And let's print them out
print(p1, p2, p3)

# We can directly access the properties of objects using a period '.'
print(p2.x, p2.y)

# We can even change the values by assigning to them
p1.x = 2
p1.y = 3
print(p1)

# Objects are a good way to store pieces of related information. In this case, either the x or y value is
# not useful on its own, both values are needed to describe a Point.

# Since we declared a distance function, let's use it:

print(p1.distance(p2))
print(p2.distance(p3))
