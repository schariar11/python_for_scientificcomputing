while True:
    x = float(input('Enter Your Score Between 0.0 and 1.0 : '))
    if 1 >= x >= 0.9:
        print('A')
    elif 1 >= x >= 0.8:
        print('B')
    elif 1 >= x >= 0.7:
        print('C')
    elif 1 >= x >= 0.6:
        print('D')
    elif 1 >= x >= 0.5:
        print('E')
    elif 0.5 > x >= 0:
        print('F')
    else:
        print('Bad score')
