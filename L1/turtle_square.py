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

