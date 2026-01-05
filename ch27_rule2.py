# import the 'dissemble' function
from dis import dis

# dis("while True:  x = 10")
dis('''
if x > 0:
    y = 10
''')
