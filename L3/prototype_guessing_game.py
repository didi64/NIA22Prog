LOWER = 1
UPPER = 5
nbr = 4

n = None
while n != nbr:
    n = input('Zahl zwischen {a} und {b}'.format(a=LOWER, b=UPPER))
    n = int(n)
    
    if  n < nbr:
        print('too small')
    elif n == nbr:
        print('correct')
    else:    
        print('too big')    
