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
