#1
def add_two_numbers (x, y):
  sum = x +y
  return sum

print(add_two_numbers(2, 3))

#2 Write a function that calculates the area of a circle
def area_circle(r):
  pi = 3.14
  area = pi*(r*r)
  return area

print(area_circle(3))

# 3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
  sum = 0
  for i in args:
    if isinstance(i, int):
      sum += i
  return sum

print(add_all_nums(1, "two", 2))

# 4 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def conversion(celsius):
  farenheit = (int(celsius) * (9 / 5) + 32)
  return farenheit

print(conversion(80))

#5 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
#How too convert input to lower or upper case? Is it in the parameter section or in the def declaration?
def check_season(month):
 
  spring = ["January", "February", "March"]
  summer = ["April", "May", "June"]
  autumn = ["July", "August", "September"]
  winter = ["October", "November", "December"]
  
  if month in spring:
    print("Spring")
  if month in summer:
    print("Summer")
  if month in autumn:
    print("Autumn")
  if month in winter:
    print("Winter")
  else:
    print("Not a month")
    
check_season("october")

# 6 Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, x2, y1, y2):
  m = (y2-y1) / (x2-x1)
  return m

# 8 Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# ? How to print a list in a single line?
def print_list(lst):
  for i in lst:
    print(i)
    
fruits = ["Apple", "Banna", "Oranges"]
print_list(fruits)

# 9 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(arr):
  return arr[::-1]

numbers = [1, 2, 3]
print(reverse_list(numbers))

# 10 Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
  for i in lst:
    lst[lst.index(i)] = i.capitalize()
  return lst
a = ["taxi", "blueberry", "jam"]
print(capitalize_list_items(a))

# 11 Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
groceries = ["Apple", "Chicken", "Juice"]

def add_item(lst, b):
  lst.append(b)
  return lst
print(add_item(groceries, "Beef"))

# 12 Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lst, a):
  lst.remove(a)
  return lst
print(remove_item(groceries, "Chicken"))

# 13 Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(nums):
  sum = 0
  for i in range (nums + 1):
    sum += i
  return sum
print(sum_of_numbers(10))

# 14 Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# 15 Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_odds(nums):
  sum_odds = 0
  for i in range(nums + 1):
    if i % 2 == 1:
       sum_odds += i
  return sum_odds
print("Odd sum is", sum_of_odds(10))


def sum_of_evens(nums):
  sum_evens = 0
  for i in range(nums + 1):
    if i % 2 == 0:
       sum_evens += i
  return sum_evens
print("Even sum is", sum_of_evens(10))

def evens_and_odds(nmb):
  odd_count = 0
  even_count = 0
  for x in range(nmb + 1):
    if x % 2 == 1:
      odd_count += 1
    if x % 2 == 0:
      even_count += 1
  print("Total number of odds ", odd_count)
  print("Total number of evens ", even_count)
  
evens_and_odds(100)

