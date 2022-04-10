import turtle

turtle.title("Turtle Drawing")
circle = turtle.Turtle()
circle.shape("turtle")
circle.pensize(5)
circle.pencolor("cyan")

circle.dot(20)


def paint(color, r):
    circle.pencolor(color)
    circle.penup()
    circle.goto(0, -r)
    circle.pendown()
    circle.circle(r)

paintCircle("red", 30)

paintCircle( "green", 60)
paintCircle("blue", 90)
paintCircle("yellow", 120)

turtle.exitonclick()