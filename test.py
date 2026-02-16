import os 
file_path = "test.txt"

txt_data = "i like pizza"

with open(file_path,"w") as file:
    file.write(txt_data)
    