# ask user for the F
# convert it to float()
# C = (F - 32) * 5 / 9
# print C to the user

F = input("Enter temperature in Fahrenheit: ")
try:
    F = float(F)
    C = (F - 32) * 5 / 9
    print("Temperature in Celsius: {:.2f}".format(C))
except ValueError:
    print("Invalid input. Please enter a numeric value for Fahrenheit.")
