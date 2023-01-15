"""
  age = int(input("What is your age? "))

if age >= 18:
  print("You are old enough to drive a car!")
  
else:
  print("You need " + str(18 - age) + " years to learn too drive. ")
  
  #Excercise 2
  
my_age = 31
your_age = int(input("Enter your age "))

if my_age > your_age:
  print("I am " + str(my_age-your_age) + " years older than you.")
elif my_age < your_age:
  print("You are " + str(your_age - my_age) + " years older than me")
else:
  print("We are the same age.")
#
  """


"""
first_number = int(input("Choose your first number: "))
second_number = int(input("Choose your second number: "))

if first_number > second_number:
  print(first_number, " is greater than ",  second_number)
elif second_number > first_number:
  print(second_number,  " is greater than ",  first_number)
elif first_number == second_number:
  print("Both numbers are the same and tied")
else:
  print("Error try different numbers")
  
  """
  
score = int(input("Enter score: "))

grades = {}
for i in range(90, 101):
    grades[i] = 'A'
for i in range(70, 90):
    grades[i] = 'B'
for i in range(60, 70):
    grades[i] = 'C'
for i in range(50, 60):
    grades[i] = 'D'
for i in range(0, 50):
    grades[i] = 'F'

print("Grade:", grades[score])