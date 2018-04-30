from tkinter import *
import Quadratic_Factorisation
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

style.use("ggplot")
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

master = Tk()
description_label = Label(master,
                          text="This is a quadratic equation calculator to find the real roots! "
                               "You have to enter a quadratic equation of the form ax^2+bx+c")
description_label.pack()

equation = Variable()
quadratic_input = Entry(master, textvariable=equation)
quadratic_input.pack()
answer_label = Label(master)
answer_label.pack()


def get_user_equation():
    user_equation = str(equation.get())
    answer = Quadratic_Factorisation.quadratic_equation(user_equation)
    answer_label.config(text=str(answer)[0])
    x = np.arange(-20, 20)
    y = eval(answer[1])
    f = Figure(figsize=(10, 10), dpi=100)
    a = f.add_subplot(111)
    a.plot(x, y)

    canvas = FigureCanvasTkAgg(f, master)
    canvas.draw()
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)


input_receive_button = Button(master, command=get_user_equation, text="OK")
input_receive_button.pack()
master.mainloop()
