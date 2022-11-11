from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")


print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

final_txt = "{}\n{}\n{}\n"
target.write(final_txt.format(line1, line2, line3))

target = open(filename)
print("This is your new file: ")
print(target.read())

# close: Closes the file.
# read: Reads the contents od the file. You can assign the result to a variable.
# readline: Reads just one line of a text file.
# truncate: Empties a file.
# write ('stuff'): writes "stuff" to the file
# seek(0): Moves the read write location to the beginning of the file
