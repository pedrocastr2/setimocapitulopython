import random
import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.bgcolor("black")


colors = ["red","blue","yellow","green","purple" ,"orange","white","gray"]


def desenhar_kaleido(x,y):
    t.pencolor(random.choice(colors))
    size = random.randint(10,  40)
    
    desenhar_espiral(x,y, size)
    desenhar_espiral(-x,y, size)
    desenhar_espiral(x,-y, size)
    desenhar_espiral(-x,-y, size)
    
    
def desenhar_espiral(x, y, size):
    t.penup()
    t.goto(x,y)
    t.pendown()
  
    for m in range(size):
        t.forward((m*2))
        t.left(92)

turtle.onscreenclick(desenhar_kaleido)

turtle.done()

