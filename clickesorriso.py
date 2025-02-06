import random
import turtle

t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen() 
turtle.bgcolor("black")

def desenha_sorriso(x,y):
     t.penup()
     t.setpos(x,y)
     t.pendown()
     
     #A cabeça do sorriso
     t.pencolor("yellow")
     t.fillcolor("yellow")
     t.begin_fill()
     t.circle(50)
     t.end_fill()
     
     #O Olho esquerdo
     t.setpos(x-15,y+60)
     t.fillcolor("red")
     t.begin_fill()
     t.circle(10)
     t.end_fill()
     
       
     #O Olho direito
     t.setpos(x+15,y+60)
     t.fillcolor("red")
     t.begin_fill()
     t.circle(10)
     t.end_fill()
     
     #A boca
     t.setpos(x-25,y+40)
     t.pencolor("black")
     t.width(10)
     t.goto(x-10,y+20)
     t.goto(x+10,y+20)
     t.goto(x+20,y+40)




screen.onscreenclick(desenha_sorriso)
screen.mainloop()