# python calculator

operator = input("Enter an operator (*,-,+,//,/,%):")
num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter the second number:"))

if operator == '*':
    answer= num_1*num_2
    print(answer)
elif operator =='+':
    answer= num_1 + num_2
    print(answer)
elif operator == '-':
    answer= num_1 - num_2
    print(answer)
elif operator == '%':
    answer= num_1 % num_2
    print(answer)
elif operator == '/':
    answer= num_1 / num_2
    print(answer)
elif operator == '//':
    answer= num_1// num_2
    print(answer)
else:
    print("Math error😚😁")
    
 # triangles in python
 
rows=6
for i in range(1, rows):
    print("* " * i)

# 60°

for i in range(rows):
    print(" " * (rows - i), end="")
    print("* " * (i + 1))  
    

# using numerics

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
