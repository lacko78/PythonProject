import turtle as t


screen = t.Screen()
screen.title("Háromszög rajzolás - turtle")
screen.setup(width=800, height=600)
screen.bgcolor("black")

pen = t.Turtle()
pen.hideturtle()
pen.pencolor("red")
pen.speed(1)

def draw_triangle():
    pen.clear()
    pen.penup()
    pen.goto(-75, -50)
    pen.pendown()
    pen.pensize(5)
    pen.goto(75, -50)
    pen.goto(0, 100)
    pen.goto(-75, -50)
    pen.penup()

def quit_app():
    screen.bye()


screen.onkey(draw_triangle, "h")
screen.onkey(quit_app, "q")
screen.listen()
screen.mainloop()
