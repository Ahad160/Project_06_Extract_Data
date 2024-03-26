def get_roll_cgpa(line):
    """
    Extracts the roll number and CGPA from a line in File-2.
    """
    parts = line.strip().split()
    roll = parts[0]
    cgpa = parts[1].strip('()')  # Removing parentheses from CGPA
    return roll, cgpa

def check_and_copy(file1_path, file2_path, output_file_path):
    """
    Checks if roll numbers from File-1 exist in File-2 and copies the lines accordingly.
    """
    # Read rolls from File-1
    with open(file1_path, 'r') as file1:
        rolls_list = [line.strip() for line in file1]

    # Open File-2 for reading and create the output file for writing
    with open(file2_path, 'r') as file2, open(output_file_path, 'w') as output_file:
        # Iterate over each line in File-2
        for line in file2:
            # Extract roll number and CGPA from the line
            roll, cgpa = get_roll_cgpa(line)
            # Check if roll exists in File-1
            if roll in rolls_list:
                # If the roll exists in File-1, write the line to the output file
                output_file.write(f"{roll} ({cgpa})\n")

# Example usage
file1_path = "E:\Codeing\Python Language\Projects\Project_06_Extract_Data\ALL_Roll.txt"
file2_path = "E:\Codeing\Python Language\Projects\Project_06_Extract_Data\CGPA.txt"
output_file_path = "output.txt"
check_and_copy(file1_path, file2_path, output_file_path)
