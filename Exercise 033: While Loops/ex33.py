from sys import argv
script, j, k = argv

i = 0
numbers = []

def while_loop(i, j, k):
    while i < int(j):
        print(f"At the top i is {i}")
        numbers.append(i)

        i += int(k)
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

while_loop(i, j, k)

print("The numbers: ")

for num in numbers:
    print(num)
