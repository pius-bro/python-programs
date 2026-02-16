grades= {"carol":"A","pius":"C","obita":"D","masi":"B"}
student = input("Enter the student :")
if student in grades:
    print(F"{student}'s grade is {grades[student]}")
else:
    print(F"{student}'s grade  is not available")