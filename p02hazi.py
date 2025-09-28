import turtle as t
import random

SIDE = 150
COLORS = ["red", "orange", "yellow", "lime", "cyan", "blue", "purple", "magenta", "white", "green"]

screen = t.Screen()
screen.title("Véletlenszínű nyolcszög - turtle")
screen.setup(900, 700)
screen.bgcolor("black")

pen = t.Turtle()
pen.hideturtle()
pen.speed(1)
pen.pensize(5)

def nyolcszog():
    pen.clear()
    pen.penup()
    pen.goto(-SIDE/2, -SIDE/2)
    pen.pendown()

    colors = COLORS[:]
    random.shuffle(colors)

    for i in range(8):
        pen.pencolor(colors[i % len(colors)])
        pen.forward(SIDE)
        pen.left(45)

def kilepes():
    screen.bye()

screen.onkey(nyolcszog, "h")
screen.onkey(kilepes, "q")
screen.listen()
screen.mainloop()
