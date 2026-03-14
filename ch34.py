from dis import dis

# dis('''

numbers = []
def print_numbers(the_numbers,offset):
    i = 0
    # while i < int(the_numbers):
    #     print(f"At the top i is {i}")
    #     numbers.append(i)

    #     i = i + int(offset)
    #     print("Numbers now: ", numbers)
    #     print(f"At the bottom i is {i}")
    for i in range(0, int(the_numbers), int(offset)):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

prompt = "> "
print("Enter a number: ")
a_number = input(prompt)
print("Enter an offset: ")
offset = input(prompt)
print_numbers(a_number,offset)

for num in numbers:
    print(num)

# # ''')
