# Let's give python some command line arguments
from sys import argv

# We look for 2 arguments on the command line
script, filename = argv

# Given filename from command line, we open the file
txt = open(filename)

# We are going to tell our users we are displaying the file
print(f"Here's your file {filename}:")
# We are showing the file on screen
print(txt.read())
# # I added this, we can't read it one more time because we already read the file
# print(txt.read())

# # If you know the file name, tell us
# print("Type the filename again:")
# file_again = input("> ")

# # We are opening the file again
# txt_again = open(file_again)

# # We are going to show the file
# print(txt_again.read())