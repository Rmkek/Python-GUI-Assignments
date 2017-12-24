from tkinter import *


def pack_stuff(*args):
    for each in args:
        each.pack()


def evaluate():
    if convert_value.get() == '+':
        label.configure(text='Evaluated: {}'.format(first_scale.get() + second_scale.get()))
    if convert_value.get() == '*':
        label.configure(text='Evaluated: {}'.format(first_scale.get() * second_scale.get()))
    if convert_value.get() == '/':
        label.configure(text='Evaluated: {}'.format(first_scale.get() / second_scale.get()))
    if convert_value.get() == '-':
        label.configure(text='Evaluated: {}'.format(int(first_scale.get() - second_scale.get())))


root = Tk()
root.minsize(width=300, height=100)
convert_value = StringVar()

first_scale = Scale(root, orient=HORIZONTAL)
second_scale = Scale(root, orient=HORIZONTAL)
label = Label(root)

addition_button = Radiobutton(root, text='+', variable=convert_value, value='+')
addition_button.select()
subtraction_button = Radiobutton(root, text='-', variable=convert_value, value='-')
multiply_button = Radiobutton(root, text='*', variable=convert_value, value='*')
division_button = Radiobutton(root, text='/', variable=convert_value, value='/')

calculate_button = Button(root, text='Посчитать', command=evaluate)

pack_stuff(first_scale, second_scale, label, addition_button,
           subtraction_button, multiply_button, division_button, calculate_button)

root.mainloop()
