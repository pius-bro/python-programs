# String formatting in python
# String formatting in python means inserting a variable or expressions inside a string

#1 f- Strings -> MODERN WAY i python 3.6.....

name = 'Python'
age = 21

print(f'My name is {name} and I am {age} years old.')

#2 .format() Method
print('My name is {} and I am {} years old.'.format(name,age))

#3. Formatting Numbers
pi = 3.1415926
print(f'{pi:.2f}')

# widith and alignment

num = 5
print(f'{num:5}')
print(f'{num:05}')

#4. Aligning Text

word = 'Python'
language ='Python'
experience ='Junior'
print(f'{word:<10}') # left align {value:format}
print(f'{language:>10}') # right align {value:format}
print(f'{experience:^10}') # center {value:format}

# integers

age = 25

print(f"Your age is {age} years old")
quantity = 3

print(f"You're buying {quantity} items")

# floats
height = 5.3

print(f'You are {height}m high')

gpa = 3.2

print(f"Your gpa is:{gpa}")

# booleams

is_running = True
for_sale = False

x = 7
y = 8
x = y

print(x is y)

if is_running:
    print("Great")
else:
    print("How 😂😂😂😂😊😊👏")
    
if for_sale:
    print("Not today")
else:
    print("We can talk")
    
    # QUIZ_1

if 10==10.0:
    print("True")
else:
    print("False")


#QUIZ_2

y=10
if y == 10 and '':
    print("Correct")
else:
    print("Incorrect")
    
    
# operators
# Assignment oprator

curent_age = 8  # assignig a value to a variable

birthday_age = curent_age + 1 # *=,-=,%=

print(f"You are {curent_age} years old")

print(f"Happy birthday you are {birthday_age} years old")

# Arithmetic operators (*,/,+,-,%,//)

# note that you don't space between operators but its good for readability
num_1 = 2
num_2 = 3
sum = num_1 + num_2

exponent = num_1**2 

print(sum)
print(exponent)

num_1 = 2
num_2 = 3
mult = num_1 * num_2

print(mult)

num_1 = 2
num_2 = 3
div = num_1 / num_2

print(div)

num_1 = 7
num_2 = 3
rem = num_1 % num_2

print(rem)

num_1 = 5
num_2 = 3
abs = num_1 // num_2

print(abs)


# comparison(Relational Operators) --> returs boolean values 
# ( ==,!=,>,<,>=,<=)
x = 10
y = 8

print(x == y)
print(x >= y)
print(x <= y)
print(x != y)
print(x > y)
print(x < y)

print('')

# Logical operators (AND,OR,NOT) --> Used with conditions

z = 10

print( z > 5 and z < 15)
print( z > 5 or z < 15)
print (not z > 5)

# EX involving input(),strings,operations e.t.c 

# Calculating the area of a rectangle,triangle,circle

from math import pi
 
L = int(input("Enter the length:"))
W = int(input("Enter the width:"))

area = L * W
print(area)

# Triangle

base = int(input("Enter the base: "))
height =  int(input("Enter the base: "))

area = 0.5*base*height
print(area)

# Circle

radius = int(input("Enter the radius: "))
area = pi * radius**2
print(area)












