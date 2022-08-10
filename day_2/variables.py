#Day 2 of 30 days of Python
from cmath import pi
from operator import truediv


first_name = "Kevin"
last_name = "Lam"
full_name = "Kevin Lam"
country = "United States"
city = "Irvine"
age = 30
year = 2022
is_married = False
is_true = True
is_light_on = False
is_door_closed, is_computer_on = False, True

print("What is your first name")
first_name = input()

print("What is your last name?")
last_name = input()

print("What country are you in?")
country = input()

print("What is your age?")
age = int(input())

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(is_door_closed))

print(len(full_name))


num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two
print(total)

print("Enter the radius: ")
radius = int(input())
area_of_circle = pi * radius ** 2
print("Area of a circle with radius" + " " + str(radius) + " " + "is " + str(area_of_circle))
cirum_of_circle = 2 * pi * radius
print("Circumference of a circle with radius " + str(radius) + " is " + str(cirum_of_circle))
