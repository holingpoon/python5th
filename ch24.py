fruit = [
  {'kind': 'Apples', 'count': 12, 'rating': 'AAA'},
  {'kind': 'Oranges', 'count': 1, 'rating': 'B'},
  {'kind': 'Pears', 'count': 2, 'rating': 'A'},
  {'kind': 'Grapes', 'count': 14, 'rating': 'UR'}
]

cars = [
    {'type': 'Cadillac', 'color': 'Black',
     'size': 'Big', 'miles': 34500},
    {'type': 'Corvette', 'color': 'Red',
     'size': 'Little', 'miles': 1000000},
    {'type': 'Ford', 'color': 'Blue',
     'size': 'Medium', 'miles': 1234},
    {'type': 'BMW', 'color': 'White',
     'size': 'Baby', 'miles': 7890}
];

languages = [
    {'name': 'Python', 'speed': 'Slow',
     'opinion': ['Terrible', 'Mush']},
    {'name': 'JavaScript', 'speed': 'Moderate',
     'opinion': ['Alright', 'Bizarre']},
    {'name': 'Perl6', 'speed': 'Moderate',
     'opinion': ['Fun', 'Weird']},
    {'name': 'C', 'speed': 'Fast',
     'opinion': ['Annoying', 'Dangerous']},
    {'name': 'Forth', 'speed': 'Fast',
     'opinion': ['Fun', 'Difficult']},
];

print("**Fruit Challenge**")
print(f"12: {fruit[0]["count"]}")
print(f"AAA: {fruit[0]["rating"]}")
print(f"2: {fruit[2]["count"]}")
print(f"Oranges: {fruit[1]["kind"]}")
print(f"Grapes: {fruit[3]["kind"]}")
print(f"14: {fruit[3]["count"]}")
print(f"Apples: {fruit[0]["kind"]}")

print("**Cars Challenge**")
print(f"Big: {cars[0]["size"]}")
print(f"Red: {cars[1]["color"]}")
print(f"1234: {cars[2]["miles"]}")
print(f"White: {cars[3]["color"]}")
print(f"7890: {cars[3]["miles"]}")
print(f"Black: {cars[0]["color"]}")
print(f"34500: {cars[0]["miles"]}")
print(f"Blue: {cars[2]["color"]}")

print("**Languages challenge**")
print(f"Slow: {languages[0]["speed"]}")
print(f"Alright: {languages[1]["opinion"][0]}")
print(f"Dangerous: {languages[3]["opinion"][1]}")
print(f"Fast: {languages[3]["speed"]}, {languages[4]["speed"]}")
print(f"Difficult: {languages[4]["opinion"][1]}")
print(f"Fun: {languages[2]["opinion"][0]}, {languages[4]["opinion"][0]}")
print(f"Annoying: {languages[3]["opinion"][0]}")
print(f"Weird: {languages[2]["opinion"][1]}")
print(f"Moderate: {languages[1]["speed"]}, {languages[2]["speed"]}")

print("\n**Little Red Corvette**")
print(f"{cars[1]["size"]} {cars[1]["color"]} {cars[1]["type"]} ")
print(f"{cars[3]["size"]} {fruit[3]["rating"]} {languages[0]["opinion"][1]} {fruit[2]["count"]} {languages[3]["speed"]}")
