import turtle


#turtle.right(90)
i = 0
while(True):
    run(90,100)

#turtle.backward(100)

turtle.exitonclick()


def run(int angle, float dis):
    turtle.forward(dis)
    turtle.left(angle)
