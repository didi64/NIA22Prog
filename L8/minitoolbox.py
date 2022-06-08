'''
Beispiel eines Moduls.
Soll demonstrieren, wie Imports funktionieren.
'''
    
# functions   
def double(x):
    '''gibt das Doppelte von x zurueck'''
    return 2*x

def print_PI():
    print(PI)
    
# data
PI = 3.1415926535

print('minitoolbox.py ausgefuehrt')
# Die Variable __name__ ist offenbar definiert
# Wir werden noch sehen, was es mit dieser Variable auf sich hat
print("{} = '{}'".format('__name__', __name__)) 

# test double
print('testing double for values 0,...,9')
for i in range(10):
    print(double(i), end =',')