import turtle

tom = turtle.Turtle()
tom.shape("turtle")

for i in range(4):
    tom.forward(100)
    tom.right(90)

turtle.exitonclick()