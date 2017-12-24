from tkinter import *


def pack_stuff(*args):
    for each in args:
        each.pack()


def callback(e):
    print(e)
    try:
        evaluated = eval(entry.get())

        if evaluated is None:
            evaluated = 'None'

        answer.configure(bg='green', text=evaluated)
    except BaseException as e:
        print(e)
        answer.configure(bg='red', text='Exception happened.')


root = Tk()
root.minsize(width=500, height=500)

entry = Entry(root, width=100, justify='center')
entry.focus()
answer = Label(root)
entry.bind('<Return>', callback)

pack_stuff(entry, answer)

root.mainloop()
