def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")



print("Here is a puzzle.")


what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

# Our function is called with two arguments: a and b
# we print out what our functions is doing, in this case "ADDING"
# We tell Python to do something of backward: we return the addition of a + b. You might say this as "I add a and b, the return them."
# Python adds the 2 numbers. Then when the functions ends, any line that runs it will be able to assign this a + b result to a variable.
