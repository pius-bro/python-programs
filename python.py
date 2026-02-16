import os 

txt_data = "I like pizza"
file_path = "C:/Users/Administrator/Desktop/PYTHON PROGRAMES/python.txt"

with open(file_path,"w") as file:
    file.write(txt_data)
    print(f"txt file{file_path} was created")