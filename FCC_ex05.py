x = 0
som = 0
cont = 0
while x != 'done' and 'Done':
    x = input('Enter a number: ')
    try:
        x = float(x)
        som = som + x
        cont += 1
    except:
        if x != 'Done' and 'done':
            print('BAD DATA')
print(som, cont, round(som/cont))
