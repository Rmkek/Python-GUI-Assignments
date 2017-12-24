from tkinter import *


def pack_stuff(*args):
    for each in args:
        each.pack()


root = Tk()
root.minsize(width=500, height=500)

first_frame = Frame(root, width=200, height=150, bg='light grey')
your_address = Label(first_frame, text='Ваш адрес:')
your_address_entry = Entry(first_frame)
comment = Label(first_frame, text='Комментарий:')
comment_text = Text(first_frame, height=3, width=25)
send_button = Button(first_frame, text='Отправить')

second_frame = Frame(root, width=150, height=250, bg='light grey')
mockup = IntVar()
how_many_label = Label(second_frame, text='Сколько штук?')
first_choice = Radiobutton(second_frame, text='0-10', variable=mockup, value=0)
second_choice = Radiobutton(second_frame, text='11-20', variable=mockup, value=1)
third_choice = Radiobutton(second_frame, text='21-30', variable=mockup, value=2)
fourth_choice = Radiobutton(second_frame, text='31-40', variable=mockup, value=3)
which_color_label = Label(second_frame, text='Какого цвета?')
color_mockup = IntVar()
red_color = Checkbutton(second_frame, text="RED", variable=color_mockup, onvalue=1, offvalue=0, bg='red')
blue_color = Checkbutton(second_frame, text="BLUE", variable=color_mockup, onvalue=2, offvalue=0, bg='blue')
green_color = Checkbutton(second_frame, text="GREEN", variable=color_mockup, onvalue=3, offvalue=0, bg='green')
yellow_color = Checkbutton(second_frame, text="YELLOW", variable=color_mockup, onvalue=4, offvalue=0, bg='yellow')


pack_stuff(first_frame, your_address, your_address_entry, comment, comment_text, send_button,
           second_frame, how_many_label, first_choice, second_choice, third_choice, fourth_choice,
           which_color_label, red_color, blue_color, green_color, yellow_color)

root.mainloop()
