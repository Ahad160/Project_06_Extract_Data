# Open file 1 containing board rolls and CGPA
Cgpa=r'E:\Codeing\Python Language\Projects\Project_06_Extract_Data\CGPA.txt'
with open(Cgpa, "r") as f1:
    board_cgpa = f1.readlines()

All_Roll=r'E:\Codeing\Python Language\Projects\Project_06_Extract_Data\ALL_Roll.txt'
# Open file 2 containing names and board rolls
with open(All_Roll, "r") as f2:
    board_names_rolls = f2.readlines()

# Extract board rolls from file 2
board_rolls = [line.strip().split()[1] for line in board_names_rolls]

# Open file 3 to write matching names, rolls, and CGPA
with open("file3.txt", "w") as f3:
    # Iterate over board rolls and CGPA in file 1
    for line in board_cgpa:
        # Extract roll and CGPA (if available)
        values = line.strip().split()
        if len(values) > 1:
            roll = values[0]
            cgpa = values[1]
            # Search for roll in file 2
            for name_roll in board_names_rolls:
                name, roll2 = name_roll.strip().split()
                if roll == roll2:
                    # Write name, roll, and CGPA to file 3
                    f3.write(f"{name} {roll} {cgpa}\n")
                    break
