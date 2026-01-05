# import the 'dissemble' function
from dis import dis

# pass code to dis() as a string
# make sure to have no leading space, 
# do not take IDEs suggestion on formatting
dis('''
x = 10
y = 20
z = x + y
''')
