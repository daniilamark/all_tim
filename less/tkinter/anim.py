from tkinter import *


def motion():
    c.move(ball, 1, 0)
    if c.coords(ball)[2] < 300:
        root.after(10, motion)

root = Tk()
c = Canvas(root, width=300, height=200, bg="white")
c.pack()

ball = c.create_oval(0, 50, 40, 140, fill='green')
motion()
root.mainloop()