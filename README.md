# setimocapitulopython
O sétimo capitulo do livro ensine python para seus filhos
Este capitulo é focado na criação de funções, diferente do anteriores que utilizam funções internas ou importadas de biblioteca, essa parte do livro possui muita importância se tratado de uma parte do código pautada na reutilização e criação de programas estruturados e complexos.

exemplo de utilização de uma função:

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
        


![image](https://github.com/user-attachments/assets/6112bf41-50c1-43d8-966b-708fd21d373e)



#Esse capitulo tem destaque também na interatividade com o usúario , através de eventos , como um clicar de um mouse e uma movitação :

exemplo:


import turtle
t = turtle.Pen()

t.speed(0)

turtle.onscreenclick()


![image](https://github.com/user-attachments/assets/5c4c60a1-513d-4930-86b9-c71e207bfdcc)


