import turtle

tom = turtle.Turtle()
tom.shape("turtle")
tom.color("red", 'green')

tom.begin_fill()

for j in range(3):
    for i in range(4):
        tom.forward(100)
        tom.left(90)
    tom.left(20)
tom.end_fill()
turtle.exitonclick()