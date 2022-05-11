LOWER = 1
UPPER = 5
nbr = 4

while True:
    n = input('Zahl zwischen {a} und {b}'.format(a=LOWER, b=UPPER))
    n = int(n)
    
    if  n == nbr:
        print('correct!')
        break
    elif n < nbr:
        print('too small')
    else:
        print('too big')    
