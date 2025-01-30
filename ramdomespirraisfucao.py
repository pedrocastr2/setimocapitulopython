import random
import turtle

t= turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red","blue","yellow","green","purple" ,"orange","white","gray"]

def random_spiral():
     t.pencolor(random.choice(colors)) #escolhe uma cor aleatória
     size = random.randint(10,40)
     
     x= random.randrange(-turtle.window_width()//2,turtle.window_width()//2)
     y= random.randrange(-turtle.window_height()//2,turtle.window_height()//2)
     

     t.penup()
     t.setpos(x,y)
     t.pendown()
     for m in range(size):
        t.forward(m*2)
        t.left(91)
        
        
for n in range(50):
    random_spiral()