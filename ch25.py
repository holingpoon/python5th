def create_car(type, size, color, speed):
  car = {
    "type": type,
    "size": size,
    "color": color,
    "speed": speed
  }
  return car

my_corvette = create_car("Corvette", "Little", "Red", "Fast");
print(f"{my_corvette}")

my_ford = create_car("Ford", "Big", "Blue", "Moderate")
print(f"{my_ford}")
