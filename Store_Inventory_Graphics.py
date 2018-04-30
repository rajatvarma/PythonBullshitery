from tkinter import *

master = Tk()

description_label = Label(master, text="What do you want to do?", relief="raised")
description_label.pack()

label_radio_value = Label(master)
label_radio_value.pack()

set_radio_value = StringVar()

radio_option_search = Radiobutton(master, text="Search", variable=set_radio_value, value='s')
radio_option_search.pack()

radio_option_add = Radiobutton(master, text="Add", variable=set_radio_value, value='a')
radio_option_add.pack()

radio_option_remove = Radiobutton(master, text="Remove", variable=set_radio_value, value='r')
radio_option_remove.pack()

radio_option_list = Radiobutton(master, text="List", variable=set_radio_value, value='l')
radio_option_list.pack()

radio_option_update = Radiobutton(master, text="Update", variable=set_radio_value, value='u')
radio_option_update.pack()

radio_option_report = Radiobutton(master, text="Report", variable=set_radio_value, value='e')
radio_option_report.pack()

radio_option_quit = Radiobutton(master, text="Quit", variable=set_radio_value, value='q')
radio_option_quit.pack()


def return_radio_value():
    label_radio_value.config(text=str(set_radio_value.get()), relief="sunken")


b = Button(master, text="get", width=10, command=return_radio_value)
b.pack()

mainloop()
