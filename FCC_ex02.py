def cel_to_fahr(cel):
    fahr = 1.8*cel + 32
    return fahr


def fahr_to_cel(fahr):
    cel = (fahr-32)/1.8
    return cel


x = '0'
while x != '1' and x != '2' and x != '3':
    x = input('\nHello \nType 1 for Celsius to Fahrenheit Conversion \nType 2'' for Fahrenheit to Celsius Convertion \nOr Type 3 to Quit \nHERE: ')
if x == '1':
    x = round(int(input('TYPE THE VALUE: ')))
    print(cel_to_fahr(x), 'ºF')
elif x == '2':
    x = round(int(input('TYPE THE VALUE: ')))
    print(fahr_to_cel(x), 'ºC')
else: quit()

while True:
    x=0
