# Every time you put "" around a piece of text you have been making a string.

# A string is how you make something that your program might give to a human. You print strings, save strings to files, send strings to web servers, etc.

# Strings with variables embedded in them use a {} and start with f for 'format' (format string).

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffe.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

height_m = height * 2.54
weight_m = weight * 0.45359237
print(f"His height in the metric system is {round(height_m)}cm.")
print(f"His weight in the metric system is {round(weight_m)}kg.")
