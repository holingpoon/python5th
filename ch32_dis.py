from dis import dis

dis('''
if door == "1":
    print("1")
    bear = input("> ")
    if bear == "1":
        print("bear 1")
    elif bear == "2":
        print("bear 2")
    else:
        print("bear 3")
''')
