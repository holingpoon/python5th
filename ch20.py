# Allows command line arguments
from sys import argv

input_file = argv

# Reading from this file
# input_file = "ex20_test.txt"

# Print entire file at once
def print_all(f):
  print(f.read())

# Go back to beginning of file
def rewind(f):
  f.seek(0)

# Print one line in the file with line number
def print_a_line(line_count, f):
  print(line_count, f.readline())

# Open the file to be read
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

# Start from line 1
current_line = 1
print(f"Current line is {current_line}")
print_a_line(current_line, current_file)

# Advance to line 2
current_line += 1
print(f"Current line is {current_line}")
print_a_line(current_line, current_file)

# Advance to line 3
current_line += 1
print(f"Current line is {current_line}")
print_a_line(current_line, current_file)
