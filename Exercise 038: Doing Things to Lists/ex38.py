ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ') # split(ten_things, ' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # pop (more_stuff)
    print("Adding: ", next_one)
    stuff.append(next_one) # append (stuff, next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
print('#'.join(stuff[3:5])) # super stellar!

# what happens when you write 'mystuff.append('hello')'?
# 1. Python looks for the the variable 'mystuff'.
# 2. He reads the . (period) operator and look at variables that are part of 'mystuff'. Since 'mystuff' is a list, Python knows 'mystuff' has a lot of functions.
# 3. It then hits 'append' and compares the name to all the names that 'mystuff' says it owns. If 'append' is in there (it is), then Python grabs that to use.
# 4. Python reaches the parenthesis and executes the function with an extra argument: 'mystuff'.
# 5. So, in the end, the function works like 'append(mystuff, 'hello')'.

# Data structure: a formal way to structure (organize) some data (facts). Lists are one of the most common data structures that programmers use.

# When to use lists:
# 1. If you need to maintain order.
# 2. If you nedd to access the contents by a number. Using cardinal numbers, starting at 0.
# 3. If you need to go through the contents linearly (first to last). For-loops.
