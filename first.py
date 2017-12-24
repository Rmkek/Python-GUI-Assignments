from tkinter import *

root = Tk()
root.minsize(width=300, height=50)
convert_value = IntVar()


def translate_number():
    label.configure(text=str(bin(int(entry.get())))[2:]) if convert_value.get() == 0 else label.configure(text=(int(entry.get(), 2)))


binary_to_decimal = Radiobutton(root, justify='left', text='Decimal to binary', variable=convert_value, value=0)
decimal_to_binary = Radiobutton(root, justify='right', text='Binary to decimal', variable=convert_value, value=1)
entry = Entry(root, width=50, bg='yellow')
label = Label(root, width=50, justify='center', bg='blue')
button = Button(root, fg='blue', activebackground='green', activeforeground='red',
                width=50, height=3, text='Посчитать', command=translate_number)
button_color = button.cget('background')

binary_to_decimal.pack()
decimal_to_binary.pack()
entry.pack()
label.pack()
button.pack()

root.mainloop()
