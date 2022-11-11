from sys import argv
script, ps, st = argv

def pas_seats(passenger, seats):
    cars = round(passenger / seats)
    print(f"We'll need {cars} cars to accomodate all the passengers.\n")

prompt = '> '

print("How many passengers there are? ")
number_passengers = int(input(prompt))

print("How many seats does the cars have? ")
number_seats = int(input(prompt))

pas_seats(number_passengers, number_seats)
pas_seats(25, 4)
pas_seats(number_passengers * 100, number_seats / 2)
