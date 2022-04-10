import turtle
import random

turtle.title("Turtle Drawing")
circle = turtle.Turtle()
circle.shape("turtle")
circle.pensize(5)
circle.pencolor("cyan")

colors = ["red", "orange", "blue", "black", "green", "purple"]

circle.dot(20)
def paintCircle(color, r):
    circle.pencolor(color)
    circle.penup()
    circle.goto(0, -r)
    circle.pendown()
    circle.circle(r)

ls = 0
for i in range(10):
    ls = ls + 30
    paintCircle(random.choice(colors), ls)



turtle.exitonclick()