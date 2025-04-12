from tkinter import *
root = Toplevel()

import time
from googletrans import Translator
from tkinter import messagebox
from PIL import ImageTk, Image
import datetime as dt
import pandas as pd

root.title('Vembar')
dat = dt.datetime.now()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

name = StringVar()
city = StringVar()
amount = StringVar()
total = StringVar()
gave = StringVar()
returned = StringVar()

list1 = []
list2 = []
list3 = []

def clear():
    

        name.set("")
        city.set("")
        amount.set("")
        total.set("")
        gave.set("")
        returned.set("")
        e1.focus()

myLabel = Label(root, text="KOOTHAN SIVANTHI - 2022", font=('Comic Sans MS', 22, 'bold'),justify='center')
myLabel.place(x=475, y=0)

date = Label(root, text=f"{dat : %d %B %Y}", font=('Comic Sans MS', 19, 'bold'))
date.place(x=918, y=4)

l1 = Label(root, text='Name', font=('Comic Sans MS', 18))
l1.place(x=325, y=128)
e1 = Entry(root, textvariable=name, font=('Arial', 19), width=17)
e1.place(x=495, y=130)

l2 = Label(root, text='City', font=('Comic Sans MS', 18))
l2.place(x=325, y=228)
e2 = Entry(root, textvariable=city, font=('Arial', 19), width=17)
e2.place(x=495, y=230)

l3 = Label(root, text='Amount', font=('Comic Sans MS', 18))
l3.place(x=325, y=328)
e3 = Entry(root, textvariable=amount, font=('Arial', 19), width=17)
e3.place(x=495, y=330)

l811 = Label(root, text='Total', font=('Comic Sans MS', 14))
l811.place(x=1062, y=258)
e811 = Entry(root, textvariable=total, font=('Arial', 14), width=9, state='disabled')
e811.place(x=1228, y=260)

l911 = Label(root, text='Gave Amount', font=('Comic Sans MS', 14))
l911.place(x=1062, y=315)
e911 = Entry(root, textvariable=gave, font=('Arial', 14), width=9)
e911.place(x=1228, y=317)

l1011 = Label(root, text='Return Amount', font=('Comic Sans MS', 14))
l1011.place(x=1062, y=372)
e1011 = Entry(root, textvariable=returned, font=('Arial', 14), width=9, state='disabled')
e1011.place(x=1228, y=374)

photo3 = PhotoImage(file="delete.png")
photoimage2 = photo3.subsample(15, 15)

z2 = Button(root, text='Clear ', image=photoimage2, font=('Cosmic Sans MS', 17), command=clear, compound=RIGHT,
                bg='#A2A2CD', cursor='hand2')
z2.place(x=595, y=428)

photo4 = PhotoImage(file="printing.png")
photoimage3 = photo4.subsample(15, 15)

z3 = Button(root, text='Print  ', image=photoimage3, font=('Cosmic Sans MS', 17), command=clear, compound=RIGHT,
                bg='#A2A2CD', cursor='hand2')
z3.place(x=465, y=508)

photo5 = PhotoImage(file="edit.png")
photoimage4 = photo5.subsample(15, 15)

z4 = Button(root, text=' Edit   ', image=photoimage4, font=('Cosmic Sans MS', 17), command=bill_window_2,
                compound=RIGHT,
                bg='#A2A2CD', cursor='hand2')
z4.place(x=595, y=508)

def gtotal(*args):
        x = amount.get()
        if x == '':
            x = '0'
        try:
            total.set(x)
        except:
            amount.set("")

def return_amount(*args):
        try:
            i = int(total.get())
            r = int(gave.get())

            if r >= i:
                r1 = r - i
                returned.set(str(r1))
            else:
                returned.set("")
        except:
            returned.set("")

gave.trace('w', return_amount)
amount.trace('w', gtotal)

def save():

        na = name.get()
        ci = city.get()
        amount = total.get()

        list1.append(na)
        list2.append(ci)
        list3.append(amount)

        dict = {'Name': list1, 'City': list2, 'Amount': list3}
        df = pd.DataFrame(dict)
        df.to_csv('Pirandhapilai.csv', mode='a', index=False)

def back():
        win.state(newstate='normal')
        root.destroy()

photo2 = PhotoImage(file="download.png")
photoimage1 = photo2.subsample(14, 14)

z1 = Button(root, image=photoimage1, text='Save ', font=('Cosmic Sans MS', 17), command=save, compound=RIGHT,
                bg='#A2A2CD', cursor='hand2')
z1.place(x=465, y=428)

photo = PhotoImage(file="home.png")
photoimage = photo.subsample(11, 11)

z2 = Button(root, image=photoimage, text='Home ', compound=TOP, font=('Comic Sans MS', 12), bg='#A2A2CD',
                command=back, cursor='hand2')
z2.place(x=10, y=10)

def f2(event):

        e2.focus()

        e1.bind('<Down>', f2)

def f3(event):

        e3.focus()

        e2.bind('<Down>', f3)

def g1(event):

        e1.focus()

        e2.bind('<Up>', g1)

def g2(event):

        e2.focus()

        e3.bind('<Up>', g2)

root.state('zoomed')

def on_closing_4():
        msg = messagebox.askquestion('Exit Application', 'Are you sure you want to quit?', icon='warning')
        if msg == 'yes':
            root.destroy()
            win.state(newstate='normal')

root.protocol("WM_DELETE_WINDOW", on_closing_4)
win.state(newstate='iconic')

img = Image.open('IMG_20220908_124140.jpg')
img = img.resize((274, 193), Image.Resampling.LANCZOS)
d = ImageTk.PhotoImage(img)
d1 = Label(root, image=d)
d1.place(x=1071, y=48)

root.mainloop()

