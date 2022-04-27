# Turtle examples
# gehe auf https://trinket.io/python
# loesch den Code im Fenster und copy/paste eines der Beispiele
# klicke auf > um das Programm zu starten

# versuche, den Code etwas abzuaendern.

# das Module Turtle ist hier dokumentiernt:
# https://docs.python.org/3/library/turtle.html

# Turtle examples
import turtle # lade das Module turtle

# hier steht dein Code

bob= turtle.Turtle()
bob.color('blue')
bob.speed(5)
bob.shape('turtle')
#bob.pendown()

bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)

alice= turtle.Turtle()
alice.color('pink')
alice.speed(0)
alice.shape('turtle')

alice.penup()
alice.goto(50,50)
alice.pendown()

# zeichne ein Quadrat
for i in range(4):
    alice.right(90)
    alice.forward(100)
    
turtle.done() # beende Programm


####################
# iteraktives Beispiel
# copy/paste den Code, klicke auf start, dann auf das Fesnster mit der Turtle
# nun kannst du die Turtle mit den Pfeiltasten steuern und mit der Maus heruziehen

import turtle
screen = turtle.Screen()
screen.setworldcoordinates(-400,-400,400,400)

bob = turtle.Turtle()
bob.color('blue')
bob.speed(5)
bob.shape('turtle')

# Define functions for each arrow key, space, 'a' and 's'
def go_left():
    bob.left(7)
 
def go_right():
    bob.right(7)
 
def go_forward():
    bob.forward(10)
  
def go_backward():
    bob.backward(10)
    
def thicker():
    bob.pensize(10)
    
def thinner():
    bob.pensize(2)       
    
def reset():
    bob.goto(0,0)
    bob.clear()
    
def drag(x,y):
    screen.tracer(0)
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
    screen.tracer(1)


# Tell the program which functions go with which keys
screen.onkey(go_left, 'Left')
screen.onkey(go_right, 'Right')
screen.onkey(go_forward, 'Up')
screen.onkey(go_backward, 'Down')
screen.onkey(reset, 'space')
screen.onkey(thicker,'a')
screen.onkey(thinner,'s')

# Tell the program what to do if we drag bob with the mouse
bob.ondrag(drag)

# Tell the screen to listen for key presses and mouse events
screen.listen()
turtle.mainloop()
