import turtle

spiral = turtle.Turtle()
for i in range(20):
    spiral.fd(i * 10)
    spiral.rt(144)
    spiral.goto(0,0)

turtle.exitonclick()