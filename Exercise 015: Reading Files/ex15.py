from sys import argv    # import argument variable from sys module

script, filename = argv    # unpack this 2 variables with the arguments

txt = open(filename, mode='r')    # open the filename and adds it to the variable txt

print(f"Here's your file {filename}: ") # print this format string, with the variable filename
print(txt.read())    # print the read of the txt

close(txt)

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

close(txt_again)
