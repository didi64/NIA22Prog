# 1) gehe auf https://pythontutor.com/
# 2) klicke auf "Start visualizing your code now"
# 3) copy/paste jeweils eines  der Code Beispiele
# 4) klicke auf 'Visualize Execution'
# 5) klicke "next"
# 6) Was wird aufgezeigt?

#Beispiel 1
###############
x = 'hello,'
y = x
y += ' world!'

r = [1,2,3]
s = r
r+= [4,5]
#########

# Beispiel 2

# Falsch Weg eine 3x2 Matrix mit 0 zu initialisieren:
# 2 * [0] liefert die Liste [0,0], das ist noch ok.

m = 3 * [2 * [0]]  # hier geht etwas schief, was?

m[0][0] = 1 # 1. (0te) Spalte ist nun 1

# Ausgabe der Matrix
print((m[0][0], m[0][1]))
print((m[1][0], m[1][1]))
print((m[2][0], m[1][1]))
############################


# Beispiel 3a
m=[]
for i in range(3):
   m.append(2 * [0]) # fuegt [0,0] als letztes Element zur Liste m hinzu
   
m[0][0] = 1   
print((m[0][0], m[0][1]))
print((m[1][0], m[1][1]))
print((m[2][0], m[1][1]))

# Beispiel 3b

# obige Schleife in kompater Form (List-comprehension)
m = [2 * [0] for i in range(3)] # kurz fuer for i in range(3)

m[0][0] = 1 # Nur 1. Element der 1. Spalte ist 1
print((m[0][0], m[0][1]))
print((m[1][0], m[1][1]))
print((m[2][0], m[1][1]))

