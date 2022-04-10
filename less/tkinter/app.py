from tkinter import *
from tkinter.ttk import Combobox

num_1 = 0
num_2 = 0


def clicked():
    num_1 = int(txt_1.get())
    num_2 = int(txt_2.get())

    if (combo.get() == "+"):
        res = num_1 + num_2
    elif (combo.get() == "-"):
        res = num_1 - num_2
    elif (combo.get() == "*"):
        res = num_1 * num_2
    elif (combo.get() == "/"):
        res = num_1 / num_2

    lbl.configure(text=res)


window = Tk()
window.title("калькулятор")
window.geometry('335x80')

lbl = Label(window, text="Результат: ")
lbl.grid(column=1, row=2)

lbl = Label(window, text="")
lbl.grid(column=2, row=2)

txt_1 = Entry(window, width=10)
txt_1.grid(column=0, row=0, padx=(10), pady=(10))

txt_2 = Entry(window, width=10)
txt_2.grid(column=2, row=0, padx=(10), pady=(10))

combo = Combobox(window, width=2)
combo['values'] = ("+", "-", "/", "*", "!")
combo.current(0)
combo.grid(column=1, row=0, padx=(10), pady=(10))

btn = Button(window, text="Решить", command=clicked, width=10)
btn.grid(column=3, row=0, padx=(10), pady=(10))

window.mainloop()
