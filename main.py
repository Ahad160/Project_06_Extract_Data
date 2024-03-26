# Open file 1 containing board rolls and CGPA
cgpa_file_path = r'E:\Codeing\Python Language\Projects\Project_6_Extract_Data\CGPA.txt'
with open(cgpa_file_path, "r") as f1:
    board_cgpa = f1.readlines()

all_roll_file_path = r'E:\Codeing\Python Language\Projects\Project_6_Extract_Data\ALL_Roll.txt'
# Open file 2 containing names and board rolls
with open(all_roll_file_path, "r") as f2:
    board_names_rolls = f2.readlines()

# Open file 3 to write matching names, rolls, and CGPA
reslt=r'E:\Codeing\Python Language\Projects\Project_6_Extract_Data\Result.txt'

with open(reslt, "w") as f3:
    # Iterate over board rolls in file 2
    for line in board_cgpa:
        if line is board_names_rolls:
            # f3.write(f"{line}\n")
            print(line)
            continue
            
