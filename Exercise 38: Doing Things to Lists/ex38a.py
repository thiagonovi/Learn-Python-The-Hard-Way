# list of books on my shelf

books = []
print("How many books do you have on your shelf?")
number_books = input("> ")

count = len(books) + 1

while count <= int(number_books):
    if count == 1:
        ordinal = "st"
    elif count == 2:
        ordinal = "nd"
    elif count == 3:
        ordinal = "rd"
    else:
        ordinal = "th"
    print(f"What's the name of the {count}{ordinal} book?")
    new_book = input("> ")
    books.append(new_book)

print(f"All your books: ")
for b in books:
    print(b)
