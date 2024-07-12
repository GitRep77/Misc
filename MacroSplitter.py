# This script is designed for splitting the contents of a file called "Input.txt" into multiple groups,
# each of which can fit into a World of Warcraft macro with a character limit (e.g., 255 characters).
# The grouped results are saved into a file called "MacroGroups.txt".

# How to use this script:

# 1. Install Python:
#    - Go to the official Python website: https://www.python.org/
#    - Download and install the latest version of Python for your operating system.
#    - During installation, make sure to check the box that says "Add Python to PATH".

# 2. Create an "Input.txt" file:
#    - In the same directory where you saved this script, create a file named "Input.txt".
#    - Each line in "Input.txt" should contain a single macro command or text snippet.

# 3. Open a command prompt or terminal:
#    - On Windows, you can open the command prompt by pressing Win + R, typing "cmd", and pressing Enter.
#    - On macOS, you can open the Terminal application from the Applications/Utilities folder.
#    - On Linux, you can open a terminal from your applications menu or by pressing Ctrl + Alt + T.

# 4. Navigate to the directory containing this script:
#    - Use the `cd` command to change directories. For example, if your script is in the "Downloads" folder, you can type:
#      cd Downloads

# 5. Run the script:
#    - Type the following command and press Enter:
#      python your_script_name.py
#    - Replace "your_script_name.py" with the actual name of your script file.

# 6. Check the output:
#    - The script will read the contents of "Input.txt", group the lines into batches that fit within the character limit,
#      and save the grouped batches into "MacroGroups.txt".
#    - Open "MacroGroups.txt" to see the grouped macro commands, which can be copied into separate macros in World of Warcraft.

# Example:
# If "Input.txt" contains the following lines:
# /way 69.37 68.32
# /way 73.59 68.53
# /way 73.48 36.34
# /way 81.06 32.37
# /way 82.56 43.10
# /way 82.54 43.92
# /way 80.82 44.67
# /way 77.86 48.52
# /way 73.95 47.96
# /way 71.17 46.72
# /way 66.45 40.77
# /way 70.03 36.79
# /way 66.35 37.15
# /way 70.98 42.53
# /way 66.75 58.61
# /way 61.50 63.17
# /way 58.41 62.54
# /way 54.79 50.15
# /way 54.36 49.70
# /way 51.73 47.71
# /way 49.32 47.18
# /way 49.31 48.42
# /way 50.14 39.50
# /way 61.83 35.12

# The script will split these lines into separate groups that fit within the character limit and save them in "MacroGroups.txt".
# Each group will be prefixed with "Macro {group_number}:" and separated by a newline.

import os

def ensure_file_exists(file_name):
    """Ensure that a file exists by creating it if it does not."""
    if not os.path.exists(file_name):
        with open(file_name, 'w') as f:
            pass

def read_values_from_file(file_name):
    """Read non-empty lines from a file and return them as a list of strings."""
    values = []
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.strip():
                    values.append(line.strip())
    except Exception as e:
        print(f"Error reading the file {file_name}: {e}")
    return values

def save_grouped_values_to_file(grouped_values, file_name):
    """Save grouped values to a file, with each group separated by a header and a newline."""
    try:
        with open(file_name, 'w') as file:
            group_number = 1
            for group in grouped_values:
                file.write(f"Macro {group_number}:\n")
                for value in group:
                    file.write(f"{value}\n")
                file.write("\n")
                group_number += 1
    except Exception as e:
        print(f"Error writing to the file {file_name}: {e}")

def main():
    """Main function to split the input text into groups and save them to an output file."""
    ensure_file_exists("Input.txt")
    ensure_file_exists("MacroGroups.txt")

    values = read_values_from_file("Input.txt")
    grouped_values = []
    current_list = []
    combined_values = ""
    character_limit = 255

    for value in values:
        # Check if adding this value would exceed the character limit
        if len(combined_values) + len(value) + (1 if current_list else 0) <= character_limit:
            current_list.append(value)
            if current_list:
                combined_values += " "
            combined_values += value
        else:
            grouped_values.append(current_list.copy())
            current_list.clear()
            combined_values = value
            current_list.append(value)

    # Add the last group if there are any values left
    if current_list:
        grouped_values.append(current_list)

    save_grouped_values_to_file(grouped_values, "MacroGroups.txt")

if __name__ == "__main__":
    main()
