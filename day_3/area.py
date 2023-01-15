age = 30
height = 51.5
complex_number = -1

print("Enter the base of the triangle")
base = int(input())
print("Enter the height: ")
height = int(input())

area = 0.5 * base * height

print("The area of your triangle with base " + str(base) + " and height " + str(height) + " is " + str(area))

print("Enter side A, side B, and side C of a triangle")
side_A = int(input())
side_B = int(input())
side_C = int(input())

perimeter = side_A + side_B + side_C

print("The perimeter of the triangle with" + "side A, " + side_A + "side B," + side_B + "side C," + side_C + "is" + perimeter )

length = int(input("Enter Length: "))
width = int(input("Enter Width: "))
print("area: ",  length * width)
print("perimeter: ", 2*(length+width))

radius = int(input("Enter radius: "))
print("area: ", 3.14**2)
print("circumference: ", (2*3.14*radius))

#12
print(not len('python') == len('dragon'))

#13
print('on' in "python" and "on" in "dragon")

#14
print("jargon" in "I hope this course is not full of jargon.")

#15
print("on" not in "python" and "on" in "dragon")

#16
print(str(float(len("python"))))

#17

