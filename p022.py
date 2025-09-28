import turtle
import random

def negyszog (x, y):
    ker= 2*x+2*y
    ter= x*y
    if x==y:
        alakzat="négyzet"
    else:
        alakzat="téglalap"
    return ker,ter,alakzat

def negyzet():
    turtle.penup()
    turtle.goto(-50,50)
    turtle.pendown()
    turtle.pencolor("blue")
    turtle.pensize(5)
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
def pont(x,y):
    turtle.penup()
    turtle.pencolor("red")
    turtle.goto(x,y)
    turtle.dot(10)
def dobas():
    turtle.hideturtle()
    turtle.clear()
    negyzet()
    szam=random.randint(1, 6)

    if szam==1:
        pont(0, 0)
    elif szam==2:
        pont(-25, 25)
        pont(25, -25)
    elif szam==3:
        pont(-25, 25)
        pont(25, -25)
        pont(0, 0)
    elif szam==4:
        pont(-25, 25)
        pont(25, -25)
        pont(25, 25)
        pont(-25, -25)
    elif szam==5:
        pont(-25, 25)
        pont(25, -25)
        pont(25, 25)
        pont(-25, -25)
        pont(0, 0)
    elif szam==6:
        pont(-25, 25)
        pont(25, -25)
        pont(25, 25)
        pont(-25, -25)
        pont(-25, 0)
        pont(25, 0)



#app
ablak=turtle.Screen()

turtle.listen()
turtle.onkey(dobas, "d")
turtle.onkey(turtle.bye,"Escape")
turtle.mainloop()






'''if __name__=="__main__":
    a=4
    b=4
    eredmeny=negyszog(a, b)
    print(f"A {eredmeny[2]} kerülete =",eredmeny[0])
    print(f"A {eredmeny[2]} területe =",eredmeny[1])
    print("Saját hívás.")'''