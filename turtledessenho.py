import turtle
t = turtle.Pen()
t.speed(0)


def move_tortuga(x, y):
    t.setpos(x, y)

turtle.onscreenclick(move_tortuga)
turtle.done()