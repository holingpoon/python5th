def print_number(x):
  print("NUMBER IS", x)

rename_print = print_number
rename_print(100)
print_number(100)

def add_two_numbers(x,y):
  print(f"Sum of {x} and {y} is {x+y}")

function_pointer = add_two_numbers
add_two_numbers(1,2)
function_pointer(3,4)

color = "Red"

corvette = {
  "color": color
}

print("LITTLE", corvette["color"], "CORVETTE")

def run():
  print("VROOM")

corvette = {
  "color": "Red",
  "run": run
}

print("My", corvette["color"], "can go")
# In python everything is an object. Since run is a function object, adding () will 
# execute the function
corvette["run"]()

# This object is not a function but just a string, python will fail when trying to
# execute color as a function
# corvette["color"]()
