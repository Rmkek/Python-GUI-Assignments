from tkinter import *
from datetime import datetime


def pack_stuff(*args):
    for each in args:
        each.pack()


def callback():
    global username

    if username is None or '':
        username = entry.get()
        label.configure(text='Введите сообщение')
        return

    if entry.get() == '':
        return

    if entry.get() == 'exit()':
        root.destroy()

    msg.configure(text='{username}@{current_time} >> {message}'.format(username=username,
                                                                       current_time=datetime.now().strftime('%H:%M:%S'),
                                                                       message=entry.get()))


root = Tk()
root.minsize(width=500, height=500)

username = None
label = Label(root, text='Введите имя')
entry = Entry(root)
entry.focus()
button = Button(root, text='Ок', command=callback)
msg = Message(root, width=400)


pack_stuff(label, entry, button, msg)

root.mainloop()
