inventory = [ ["Buick", 10], ["Corvette", 1], ["Toyota", 4]]
# get the buick record
buicks = inventory[0]
buick_count = buicks[1]
# or in one move
count_of_buicks = inventory[0][1]

print(f"Inventory: {inventory}")
print(f"Buicks: {buicks}")
print(f"Buick Count: {buick_count}")
print(f"Count of Buicks: {count_of_buicks}")
