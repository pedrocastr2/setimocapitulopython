import random
import turtle

t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen() 
turtle.bgcolor("black")

colors=["red","yellow","blue","green","orange","purple","white","gray"]

def spiral(x, y):
    t.pencolor(random.choice(colors))     
    size = random.randint(10, 40)
    
    t.penup()
    t.setpos(x, y)
    t.pendown()
    
    for m in range(size):
        t.forward(m*2)
        t.left(91)
              
screen.onscreenclick(spiral) 
screen.mainloop()