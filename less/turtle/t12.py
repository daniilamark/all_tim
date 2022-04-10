import turtle

wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")

skk = turtle.Turtle()
skk.color("blue")


def sqrfunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(90)
        size = size - 5


for i in range(10):
    sqrfunc(200)


turtle.exitonclick()
