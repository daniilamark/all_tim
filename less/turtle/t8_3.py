import turtle
import random

turtle.title("Turtle Drawing")

circle = turtle.Turtle()
circle.shape("turtle")
circle.pensize(5)
circle.pencolor("cyan")
circle.hideturtle()
circle.speed(100)
colors = ["red", "orange", "blue", "black", "green", "purple"]


def paintCircle(color, r):

    circle.color(col)
    circle.begin_fill()
    circle.pencolor(color)
    circle.penup()
    circle.goto(0, -r)
    circle.pendown()
    circle.circle(r)
    circle.end_fill()


lsw = 400
for i in range(10):
    col = random.choice(colors)
    lsw = lsw - 50
    paintCircle(col, lsw)

turtle.exitonclick()