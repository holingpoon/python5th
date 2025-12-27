fruit = [
  ['Apples', 12, 'AAA'],
  ['Oranges', 1, 'B'],
  ['Pears', 2, 'A'],
  ['Grapes', 14, 'UR']
]

cars = [
  ['Cadillac', ['Black', 'Big', 34500]],
  ['Corvette', ['Red', 'Little', 1000000]],
  ['Ford', ['Blue', 'Medium', 1234]],
  ['BMW', ['White', 'Baby', 7890]]
]

languages = [
  ['Python', ['Slow', ['Terrible', 'Mush']]],
  ['JavaSCript', ['Moderate', ['Alright', 'Bizarre']]],
  ['Perl6', ['Moderate', ['Fun', 'Weird']]],
  ['C', ['Fast', ['Annoying', 'Dangerous']]],
  ['Forth', ['Fast', ['Fun', 'Difficult']]],
]

print("* Fruit Challenge")
print(f"12: {fruit[0][1]}")
print(f"AAA: {fruit[0][2]}")
print(f"2: {fruit[2][1]}")
print(f"Oranges: {fruit[1][0]}")
print(f"Grapes: {fruit[3][0]}")
print(f"14: {fruit[3][1]}")
print(f"Apples: {fruit[0][0]}")

print("* Cars Challenge")
print(f"Big: {cars[0][1][1]}")
print(f"Red: {cars[1][1][0]}")
print(f"1234: {cars[2][1][2]}")
print(f"White: {cars[3][1][0]}")
print(f"7890: {cars[3][1][2]}")
print(f"Black: {cars[0][1][0]}")
print(f"34500: {cars[0][1][2]}")
print(f"Blue: {cars[2][1][0]}")

print("* Languages Challenge")
print(f"Slow: {languages[0][1][0]}")
print(f"Alright: {languages[1][1][1][0]}")
print(f"Dangerous: {languages[3][1][1][1]}")
print(f"Fast: {languages[3][1][0]}")
print(f"Difficult: {languages[4][1][1][1]}")
print(f"Fun: {languages[4][1][1][0]}")
print(f"Annoying: {languages[3][1][1][0]}")
print(f"Weird: {languages[2][1][1][1]}")
print(f"Moderate: {languages[2][1][0]}")

print("* Final Challenge")
print(f"cars[1][1][1] is Little: {cars[1][1][1]}")
print(f"cars[1][1][0] is Red: {cars[1][1][0]}")
print(f"cars[1][0] is Corvette: {cars[1][0]}")
print(f"cars[3][1][1] is Baby: {cars[3][1][1]}")
print(f"fruit[3][2] is UR: {fruit[3][2]}")
print(f"languages[0][1][1][1] is Mush: {languages[0][1][1][1]}")
print(f"fruit[2][1] is 2: {fruit[2][1]}")
print(f"languages[3][1][0] is Fast: {languages[3][1][0]}")
