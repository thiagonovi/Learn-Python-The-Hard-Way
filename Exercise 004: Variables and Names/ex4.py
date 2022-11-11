# assigns the value 100 to the variable 'cars'
cars = 100
# shows the space available in a car: 4
space_in_a_car = 4
# show how many drivers there are: 30
drivers = 30
# shows how many passengers there are: 90
passengers = 90
# how many cars are not driven: 100 (cars) - 30 (drivers)
cars_not_driven = cars - drivers
# how many cars are driven: 30 (drivers)
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
