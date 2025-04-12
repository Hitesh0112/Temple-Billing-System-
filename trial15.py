import os
import time
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image

import datetime as dt
import pandas as pd


win = Tk()
__width = win.winfo_screenwidth()
__height = win.winfo_screenheight()
win.geometry("%dx%d" % (__width, __height))


def bill_window():
    root = Toplevel()
    root.title('Sample Bill')
    root.resizable(False, False)

    width = 500  # root.winfo_screenwidth()
    height = 570  # root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))

    f1 = Frame(root)
    f1.pack(fill=BOTH, expand=0)

    f2 = Frame(root)
    f2.pack(fill=BOTH, expand=1)

    name = StringVar()
    na = StringVar()
    city = StringVar()
    amount = StringVar()

    scroll = Scrollbar(f1, orient=VERTICAL)
    t = Listbox(f1, font=15, yscrollcommand=scroll.set)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=t.yview)
    t.pack(fill=BOTH, expand=1)

    l1 = Label(f2, text='Name', font=('Comic Sans MS', 15))
    l1.place(x=120, y=65)
    e1 = Entry(f2, textvariable=name, font=('Arial', 16), width=15)
    e1.place(x=220, y=67)

    l2 = Label(f2, text='City', font=('Comic Sans MS', 15))
    l2.place(x=120, y=115)
    e2 = Entry(f2, textvariable=city, font=('Arial', 16), width=15)
    e2.place(x=220, y=117)

    l3 = Label(f2, text='Amount', font=('Comic Sans MS', 15))
    l3.place(x=120, y=165)
    e3 = Entry(f2, textvariable=amount, font=('Arial', 16), width=15)
    e3.place(x=220, y=167)

    def select():
        z = t.curselection()[0]
        z1 = df['Name'].loc[df.index[z]]
        z2 = df['City'].loc[df.index[z]]
        z3 = df['Amount'].loc[df.index[z]]

        name.set(str(z1))
        city.set(str(z2))
        amount.set(str(z3))
        na.set(str(t.curselection()[0]))

    def save():
        v = name.get()
        v0 = city.get()
        v2 = amount.get()
        v1 = int(na.get())

        df.iloc[v1, 0] = v
        df.iloc[v1, 1] = v0
        df.iloc[v1, 2] = v2

        t.delete(0, END)
        for i1 in range(len(df.index)):
            y = df.loc[i1].values
            y1 = y[0]
            y2 = y[1]
            y3 = y[2]
            t.insert(END, f"{y1}       {y2}       {y3}")

        df.to_csv('Nankodai.csv', index=False)

    photo2 = PhotoImage(file="download.png")
    photoimage1 = photo2.subsample(15, 15)

    z1 = Button(root, image=photoimage1, text='Save   ', font=('Cosmic Sans MS', 15), command=save, compound=RIGHT,
                bg='#A2A2CD', cursor='hand2')
    z1.place(x=230, y=430)

    df = pd.read_csv('Nankodai.csv')

    photo3 = PhotoImage(file="insert.png")
    photoimage2 = photo3.subsample(16, 16)

    b4 = Button(f2, text="Insert ", command=select, image=photoimage2, font=('Cosmic Sans MS', 15), compound=RIGHT,
                bg='#A2A2CD',
                cursor='hand2')
    b4.place(x=230, y=8)

    for i in range(len(df.index)):
        x = df.loc[i].values
        x1 = x[0]
        x2 = x[1]
        x3 = x[2]
        t.insert(END, f"{x1}       {x2}       {x3}")

    win.mainloop()


def bill_window_2():
    root = Toplevel()
    root.title('Sample Bill')
    root.resizable(False, False)

    width = 500  # root.winfo_screenwidth()
    height = 570  # root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))

    f1 = Frame(root)
    f1.pack(fill=BOTH, expand=0)

    f2 = Frame(root)
    f2.pack(fill=BOTH, expand=1)

    name = StringVar()
    na = StringVar()
    city = StringVar()
    amount = StringVar()

    scroll = Scrollbar(f1, orient=VERTICAL)
    t = Listbox(f1, font=15, yscrollcommand=scroll.set)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=t.yview)
    t.pack(fill=BOTH, expand=1)

    l1 = Label(f2, text='Name', font=('Comic Sans MS', 15))
    l1.place(x=120, y=65)
    e1 = Entry(f2, textvariable=name, font=('Arial', 16), width=15)
    e1.place(x=220, y=67)

    l2 = Label(f2, text='City', font=('Comic Sans MS', 15))
    l2.place(x=120, y=115)
    e2 = Entry(f2, textvariable=city, font=('Arial', 16), width=15)
    e2.place(x=220, y=117)

    l3 = Label(f2, text='Amount', font=('Comic Sans MS', 15))
    l3.place(x=120, y=165)
    e3 = Entry(f2, textvariable=amount, font=('Arial', 16), width=15)
    e3.place(x=220, y=167)

    def select():
        z = t.curselection()
        z1 = df['Name'].loc[df.index[z]]
        z2 = df['City'].loc[df.index[z]]
        z3 = df['Amount'].loc[df.index[z]]

        name.set(str(z1))
        city.set(str(z2))
        amount.set(str(z3))
        na.set(str(t.curselection()[0]))

    def save():
        v = name.get()
        v0 = city.get()
        v2 = amount.get()
        v1 = int(na.get())

        df.iloc[v1, 0] = v
        df.iloc[v1, 1] = v0
        df.iloc[v1, 2] = v2

        t.delete(0, END)
        for i1 in range(len(df.index)):
            y = df.loc[i1].values
            y1 = y[0]
            y2 = y[1]
            y3 = y[2]
            t.insert(END, f"{y1}       {y2}       {y3}")

        df.to_csv('Pirandhapilai.csv', index=False)

    photo2 = PhotoImage(file="download.png")
    photoimage1 = photo2.subsample(16, 16)

    z1 = Button(root, image=photoimage1, text='Save   ', font=('Cosmic Sans MS', 15), command=save, compound=RIGHT,
                bg='#A2A2CD', cursor='hand2')
    z1.place(x=230, y=420)

    df = pd.read_csv('Pirandhapilai.csv')

    photo3 = PhotoImage(file="insert.png")
    photoimage2 = photo3.subsample(16, 16)

    b4 = Button(f2, text="Insert ", command=select, image=photoimage2, font=('Cosmic Sans MS', 15), compound=RIGHT,
                bg='#A2A2CD', cursor='hand2')
    b4.place(x=230, y=8)

    for i in range(len(df.index)):
        x = df.loc[i].values
        x1 = x[0]
        x2 = x[1]
        x3 = x[2]
        t.insert(END, f"{x1}       {x2}       {x3}")

    win.mainloop()


def _open_2():
    root = Toplevel()
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
    list4 = []

    def clear():

        name.set("")
        city.set("")
        amount.set("")
        total.set("")
        gave.set("")
        returned.set("")
        e1.focus()

    myLabel = Label(root, text="KOOTHAN SIVANTHI - 2022", font=('Comic Sans MS', 22, 'bold'), justify='center')
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

    z4 = Button(root, text=' Edit   ', image=photoimage4, font=('Cosmic Sans MS', 17), command=bill_window,
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
        _time = dat

        list1.append(na)
        list2.append(ci)
        list3.append(amount)
        list4.append(_time)

        dict = {'Name': list1, 'City': list2, 'Amount': list3, 'Time': list4}
        df = pd.DataFrame(dict)
        df.to_csv('Nankodai.csv', mode='a', index=False, header=True)

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

    def on_closing():

        msg = messagebox.askquestion('Exit Application', 'Are you sure you want to qui?', icon='warning')
        if msg == 'yes':
            root.destroy()
            win.state(newstate='normal')

    img = Image.open('IMG_20220908_124140.jpg')
    img = img.resize((274, 193), Image.ANTIALIAS)
    d = ImageTk.PhotoImage(img)
    d1 = Label(root, image=d)
    d1.place(x=1071, y=48)

    root.protocol("WM_DELETE_WINDOW", on_closing)
    win.state(newstate='iconic')
    root.mainloop()


name = StringVar()
city = StringVar()
Room_Rent = StringVar()
Dressing_Room = StringVar()
grand_total = StringVar()
gave = StringVar()
returned = StringVar()

all_days_adults = StringVar()

saturday_only_adults = StringVar()
sunday_only_adults = StringVar()
monday_only_adults = StringVar()

saturday_breakfast_only_adults = StringVar()
saturday_lunch_only_adults = StringVar()
saturday_dinner_only_adults = StringVar()
saturday_bf_and_lunch_adults = StringVar()
saturday_lunch_and_dinner_adults = StringVar()

sunday_breakfast_only_adults = StringVar()
sunday_lunch_only_adults = StringVar()
sunday_dinner_only_adults = StringVar()
sunday_bf_and_lunch_adults = StringVar()
sunday_lunch_and_dinner_adults = StringVar()

monday_breakfast_only_adults = StringVar()
monday_lunch_only_adults = StringVar()

total_adults = StringVar()

all_days_adults_total = StringVar()

saturday_only_adults_total = StringVar()
sunday_only_adults_total = StringVar()
monday_only_adults_total = StringVar()

saturday_breakfast_only_adults_total = StringVar()
saturday_lunch_only_adults_total = StringVar()
saturday_dinner_only_adults_total = StringVar()
saturday_bf_and_lunch_adults_total = StringVar()
saturday_lunch_and_dinner_adults_total = StringVar()

sunday_breakfast_only_adults_total = StringVar()
sunday_lunch_only_adults_total = StringVar()
sunday_dinner_only_adults_total = StringVar()
sunday_bf_and_lunch_adults_total = StringVar()
sunday_lunch_and_dinner_adults_total = StringVar()

monday_breakfast_only_adults_total = StringVar()
monday_lunch_only_adults_total = StringVar()

# ---------Kids here----------------------------

all_days_kids = StringVar()

saturday_only_kids = StringVar()
sunday_only_kids = StringVar()
monday_only_kids = StringVar()

saturday_breakfast_only_kids = StringVar()
saturday_lunch_only_kids = StringVar()
saturday_dinner_only_kids = StringVar()
saturday_bf_and_lunch_kids = StringVar()
saturday_lunch_and_dinner_kids = StringVar()

sunday_breakfast_only_kids = StringVar()
sunday_lunch_only_kids = StringVar()
sunday_dinner_only_kids = StringVar()
sunday_bf_and_lunch_kids = StringVar()
sunday_lunch_and_dinner_kids = StringVar()

monday_breakfast_only_kids = StringVar()
monday_lunch_only_kids = StringVar()

total_kids = StringVar()

all_days_kids_total = StringVar()

saturday_only_kids_total = StringVar()
sunday_only_kids_total = StringVar()
monday_only_kids_total = StringVar()

saturday_breakfast_only_kids_total = StringVar()
saturday_lunch_only_kids_total = StringVar()
saturday_dinner_only_kids_total = StringVar()
saturday_bf_and_lunch_kids_total = StringVar()
saturday_lunch_and_dinner_kids_total = StringVar()

sunday_breakfast_only_kids_total = StringVar()
sunday_lunch_only_kids_total = StringVar()
sunday_dinner_only_kids_total = StringVar()
sunday_bf_and_lunch_kids_total = StringVar()
sunday_lunch_and_dinner_kids_total = StringVar()

monday_breakfast_only_kids_total = StringVar()
monday_lunch_only_kids_total = StringVar()

def sample_bill():
    root = Toplevel()
    root.geometry("800x900")
    root.title("Sample Bill")
    f = Frame(root)
    f.pack(fill=BOTH)
    l1 = Text(f, font=15)
    l1.pack(fill=BOTH)
    da = dt.date.today()
    f1 = open("bill/" + str(da) + ".txt", "w")

    def save():
        y = l1.get('1.0', END)
        f1.write(y)
        f1.close()
        _print()

    def _print():
        os.startfile(f'C:\\Users\\Mari\\Desktop\\Python\\venv\\bill\\{da}.txt', 'print')

    b_1 = Button(root, text='Save', command=save)
    b_1.pack()

    if name.get() != '':
        l1.insert(END, f"Name:\t{name.get()}\n")

    l1.insert(END, f"Name\tQty\tAmount\n")
    l1.insert(END, f"--------------------------------------------------\n")

    if all_days_adults.get() != '':
        l1.insert(END, f"All Days:\t\t\t{all_days_adults.get()}\t{all_days_adults_total.get()}\n")

    if saturday_only_adults.get() != '':
        l1.insert(END, f"Saturday Only:\t\t{saturday_only_adults.get()}\t{saturday_only_adults_total.get()}\n")

    if sunday_only_adults.get() != '':
        l1.insert(END, f"Sunday Only:\t{sunday_only_adults.get()}\t{sunday_lunch_only_adults_total.get()}\n")

    if monday_only_adults.get() != '':
        l1.insert(END, f"Monday Only:\t{monday_only_adults.get()}\t{monday_lunch_only_adults_total.get()}\n")

    if saturday_breakfast_only_adults.get() != '':
        l1.insert(END,
                  f"Saturday BF Only:\t{saturday_breakfast_only_adults.get()}\t{saturday_breakfast_only_adults_total.get()}\n")

    if saturday_lunch_only_adults.get() != '':
        l1.insert(END,
                  f"Saturday Lunch Only:\t{saturday_lunch_only_adults.get()}\t{saturday_lunch_only_adults_total.get()}\n")

    if saturday_dinner_only_adults.get() != '':
        l1.insert(END,
                  f"Saturday Dinner Only:\t{saturday_dinner_only_adults.get()}\t{saturday_dinner_only_adults_total.get()}\n")

    if saturday_bf_and_lunch_adults.get() != '':
        l1.insert(END,
                  f"Saturday BF & Lunch:\t{saturday_bf_and_lunch_adults.get()}\t{saturday_bf_and_lunch_adults_total.get()}\n")

    if saturday_lunch_and_dinner_adults.get() != '':
        l1.insert(END,
                  f"Saturday Lunch & Dinner:\t{saturday_lunch_and_dinner_adults.get()}\t{saturday_lunch_and_dinner_adults_total.get()}\n")

    if sunday_breakfast_only_adults.get() != '':
        l1.insert(END,
                  f"Sunday BF Only:\t{sunday_breakfast_only_adults.get()}\t{sunday_breakfast_only_adults_total.get()}\n")

    if sunday_lunch_only_adults.get() != '':
        l1.insert(END,
                  f"Sunday Lunch Only:\t{sunday_lunch_only_adults.get()}\t{sunday_lunch_only_adults_total.get()}\n")

    if sunday_dinner_only_adults.get() != '':
        l1.insert(END,
                  f"Sunday Dinner Only:\t{sunday_dinner_only_adults.get()}\t{sunday_dinner_only_adults_total.get()}\n")

    if sunday_bf_and_lunch_adults.get() != '':
        l1.insert(END,
                  f"Sunday Breakfast and Lunch:\t{sunday_bf_and_lunch_adults.get()}\t{sunday_bf_and_lunch_adults_total.get()}\n")

    if sunday_lunch_and_dinner_adults.get() != '':
        l1.insert(END,
                  f"Sunday Lunch and Dinner:\t{sunday_lunch_and_dinner_adults.get()}\t{sunday_lunch_and_dinner_adults_total.get()}\n")

    if monday_breakfast_only_adults.get() != '':
        l1.insert(END,
                  f"Monday Breakfast Only:\t{monday_breakfast_only_adults.get()}\t{monday_breakfast_only_adults_total.get()}\n")

    if monday_lunch_only_adults.get() != '':
        l1.insert(END,
                  f"Monday Lunch Only:\t{monday_lunch_only_adults.get()}\t{monday_lunch_only_adults_total.get()}\n")
        
    # -----------------------------------------------------------------KIDS-----------------------------------------------------------------------------

    if all_days_kids.get() != '':
        l1.insert(END, f"All Days:\t{all_days_kids.get()}\t{all_days_kids_total.get()}\n")

    if saturday_only_kids.get() != '':
        l1.insert(END, f"Saturday Only:\t{saturday_only_kids.get()}\t{saturday_only_kids_total.get()}\n")

    if sunday_only_kids.get() != '':
        l1.insert(END, f"Sunday Only:\t{sunday_only_kids.get()}\t{sunday_lunch_only_kids_total.get()}\n")

    if monday_only_kids.get() != '':
        l1.insert(END, f"Monday Only:\t{monday_only_kids.get()}\t{monday_lunch_only_kids_total.get()}\n")

    if saturday_breakfast_only_kids.get() != '':
        l1.insert(END,
                  f"Saturday Breakfast Only:\t{saturday_breakfast_only_kids.get()}\t{saturday_breakfast_only_kids_total.get()}\n")

    if saturday_lunch_only_kids.get() != '':
        l1.insert(END,
                  f"Saturday Lunch Only:\t{saturday_lunch_only_kids.get()}\t{saturday_lunch_only_kids_total.get()}\n")

    if saturday_dinner_only_kids.get() != '':
        l1.insert(END,
                  f"Saturday Dinner Only:\t{saturday_dinner_only_kids.get()}\t{saturday_dinner_only_kids_total.get()}\n")

    if saturday_bf_and_lunch_kids.get() != '':
        l1.insert(END,
                  f"Saturday Breakfast and Lunch Only:\t{saturday_bf_and_lunch_kids.get()}\t{saturday_bf_and_lunch_kids_total.get()}\n")

    if saturday_lunch_and_dinner_kids.get() != '':
        l1.insert(END,
                  f"Saturday Lunch and Dinner Only:\t{saturday_lunch_and_dinner_kids.get()}\t{saturday_lunch_and_dinner_kids_total.get()}\n")

    if sunday_breakfast_only_kids.get() != '':
        l1.insert(END,
                  f"Sunday Breakfast Only:\t{sunday_breakfast_only_kids.get()}\t{sunday_breakfast_only_kids_total.get()}\n")

    if sunday_lunch_only_kids.get() != '':
        l1.insert(END, f"Sunday Lunch Only:\t{sunday_lunch_only_kids.get()}\t{sunday_lunch_only_kids_total.get()}\n")

    if sunday_dinner_only_kids.get() != '':
        l1.insert(END, f"Sunday Dinner Only:\t{sunday_dinner_only_kids.get()}\t{sunday_dinner_only_kids_total.get()}\n")

    if sunday_bf_and_lunch_kids.get() != '':
        l1.insert(END,
                  f"Sunday Breakfast and Lunch:\t{sunday_bf_and_lunch_kids.get()}\t{sunday_bf_and_lunch_kids_total.get()}\n")

    if sunday_lunch_and_dinner_kids.get() != '':
        l1.insert(END,
                  f"Sunday Lunch and Dinner:\t{sunday_lunch_and_dinner_kids.get()}\t{sunday_lunch_and_dinner_kids_total.get()}\n")

    if monday_breakfast_only_kids.get() != '':
        l1.insert(END,
                  f"Monday Breakfast Only:\t{monday_breakfast_only_kids.get()}\t{monday_breakfast_only_kids_total.get()}\n")

    if monday_lunch_only_kids.get() != '':
        l1.insert(END, f"Monday Lunch Only:\t{monday_lunch_only_kids.get()}\t{monday_lunch_only_kids_total.get()}\n")


    root.mainloop()


def _open():
    root = Toplevel()
    root.title('Vembar')

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))

    df = pd.read_excel('main.xlsx')
    dat = dt.datetime.now()

    c1 = df['ADULTS'].loc[df.index[18]]
    c2 = df['ADULTS'].loc[df.index[19]]

    a = df['ADULTS'].loc[df.index[1]]
    a0 = df['ADULTS'].loc[df.index[2]]
    a1 = df['ADULTS'].loc[df.index[3]]
    a2 = df['ADULTS'].loc[df.index[4]]
    a3 = df['ADULTS'].loc[df.index[5]]
    a4 = df['ADULTS'].loc[df.index[6]]
    a5 = df['ADULTS'].loc[df.index[7]]
    a6 = df['ADULTS'].loc[df.index[8]]
    a7 = df['ADULTS'].loc[df.index[9]]
    a8 = df['ADULTS'].loc[df.index[10]]
    a9 = df['ADULTS'].loc[df.index[11]]
    a10 = df['ADULTS'].loc[df.index[12]]
    a11 = df['ADULTS'].loc[df.index[13]]
    a12 = df['ADULTS'].loc[df.index[14]]
    a13 = df['ADULTS'].loc[df.index[15]]
    a14 = df['ADULTS'].loc[df.index[16]]

    # KIDS

    b = df['KIDS'].loc[df.index[1]]
    b1 = df['KIDS'].loc[df.index[2]]
    b2 = df['KIDS'].loc[df.index[3]]
    b3 = df['KIDS'].loc[df.index[4]]

    b4 = df['KIDS'].loc[df.index[5]]
    b5 = df['KIDS'].loc[df.index[6]]
    b6 = df['KIDS'].loc[df.index[7]]
    b7 = df['KIDS'].loc[df.index[8]]
    b8 = df['KIDS'].loc[df.index[9]]

    b9 = df['KIDS'].loc[df.index[10]]
    b10 = df['KIDS'].loc[df.index[11]]
    b11 = df['KIDS'].loc[df.index[12]]
    b12 = df['KIDS'].loc[df.index[13]]
    b13 = df['KIDS'].loc[df.index[14]]

    b14 = df['KIDS'].loc[df.index[15]]
    b15 = df['KIDS'].loc[df.index[16]]

    # LIST

    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    list10 = []
    list11 = []
    list12 = []
    list13 = []
    list14 = []
    list15 = []
    list16 = []
    list17 = []
    list18 = []
    list19 = []
    list20 = []
    list21 = []
    list22 = []
    list23 = []
    list24 = []
    list25 = []
    list26 = []
    list27 = []
    list28 = []
    list29 = []
    list30 = []
    list31 = []
    list32 = []
    list33 = []
    list34 = []
    list35 = []
    list36 = []
    list37 = []
    list38 = []
    list39 = []
    list40 = []
    list41 = []
    list42 = []
    list43 = []
    list44 = []
    list45 = []
    list46 = []
    list47 = []
    list48 = []
    list49 = []
    list50 = []
    list51 = []
    list52 = []
    list53 = []
    list54 = []
    list55 = []
    list56 = []
    list57 = []
    list58 = []
    list59 = []
    list60 = []
    list61 = []
    list62 = []
    list63 = []
    list64 = []
    list65 = []
    list66 = []
    list67 = []
    list68 = []
    list69 = []

    # LABELS,TXT BOXES

    def save():
        na = name.get()
        ci = city.get()

        nrooms = Room_Rent.get()
        drooms = Dressing_Room.get()
        gtotal = grand_total.get()

        p1 = all_days_adults.get()

        p2 = saturday_only_adults.get()
        p3 = sunday_only_adults.get()
        p4 = monday_only_adults.get()

        p5 = saturday_breakfast_only_adults.get()
        p6 = saturday_lunch_only_adults.get()
        p7 = saturday_dinner_only_adults.get()
        p8 = saturday_bf_and_lunch_adults.get()
        p9 = saturday_lunch_and_dinner_adults.get()
        p10 = sunday_breakfast_only_adults.get()
        p11 = sunday_lunch_only_adults.get()
        p12 = sunday_dinner_only_adults.get()
        p13 = sunday_bf_and_lunch_adults.get()
        p14 = sunday_lunch_and_dinner_adults.get()
        p15 = monday_breakfast_only_adults.get()
        p16 = monday_lunch_only_adults.get()

        p17 = all_days_adults_total.get()

        p18 = saturday_only_adults_total.get()
        p19 = sunday_only_adults_total.get()
        p20 = monday_only_adults_total.get()

        p21 = saturday_breakfast_only_adults_total.get()
        p22 = saturday_lunch_only_adults_total.get()
        p23 = saturday_dinner_only_adults_total.get()
        p24 = saturday_bf_and_lunch_adults_total.get()
        p25 = saturday_lunch_and_dinner_adults_total.get()
        p26 = sunday_breakfast_only_adults_total.get()
        p27 = sunday_lunch_only_adults_total.get()
        p28 = sunday_dinner_only_adults_total.get()
        p29 = sunday_bf_and_lunch_adults_total.get()
        p30 = sunday_lunch_and_dinner_adults_total.get()
        p31 = monday_breakfast_only_adults_total.get()
        p32 = monday_lunch_only_adults_total.get()

        q1 = all_days_kids.get()

        q2 = saturday_only_kids.get()
        q3 = sunday_only_kids.get()
        q4 = monday_only_kids.get()

        q5 = saturday_breakfast_only_kids.get()
        q6 = saturday_lunch_only_kids.get()
        q7 = saturday_dinner_only_kids.get()
        q8 = saturday_bf_and_lunch_kids.get()
        q9 = saturday_lunch_and_dinner_kids.get()
        q10 = sunday_breakfast_only_kids.get()
        q11 = sunday_lunch_only_kids.get()
        q12 = sunday_dinner_only_kids.get()
        q13 = sunday_bf_and_lunch_kids.get()
        q14 = sunday_lunch_and_dinner_kids.get()
        q15 = monday_breakfast_only_kids.get()
        q16 = monday_lunch_only_kids.get()

        q17 = all_days_kids_total.get()

        q18 = saturday_only_kids_total.get()
        q19 = sunday_only_kids_total.get()
        q20 = monday_only_kids_total.get()

        q21 = saturday_breakfast_only_kids_total.get()
        q22 = saturday_lunch_only_kids_total.get()
        q23 = saturday_dinner_only_kids_total.get()
        q24 = saturday_bf_and_lunch_kids_total.get()
        q25 = saturday_lunch_and_dinner_kids_total.get()
        q26 = sunday_breakfast_only_kids_total.get()
        q27 = sunday_lunch_only_kids_total.get()
        q28 = sunday_dinner_only_kids_total.get()
        q29 = sunday_bf_and_lunch_kids_total.get()
        q30 = sunday_lunch_and_dinner_kids_total.get()
        q31 = monday_breakfast_only_kids_total.get()
        q32 = monday_lunch_only_kids_total.get()

        list1.append(na)
        list2.append(ci)
        list3.append(nrooms)
        list4.append(drooms)
        list5.append(p1)
        list6.append(p2)
        list7.append(p3)
        list8.append(p4)
        list9.append(p5)
        list10.append(p6)
        list11.append(p7)
        list12.append(p8)
        list13.append(p9)
        list14.append(p10)
        list15.append(p11)
        list16.append(p12)
        list17.append(p13)
        list18.append(p14)
        list19.append(p15)
        list20.append(p16)
        list21.append(p17)
        list22.append(p18)
        list23.append(p19)
        list24.append(p20)
        list25.append(p21)
        list26.append(p22)
        list27.append(p23)
        list28.append(p24)
        list29.append(p25)
        list30.append(p26)
        list31.append(p27)
        list32.append(p28)
        list33.append(p29)
        list34.append(p30)
        list35.append(p31)
        list36.append(p32)

        list37.append(q1)
        list38.append(q2)
        list39.append(q3)
        list40.append(q4)
        list41.append(q5)
        list42.append(q6)
        list43.append(q7)
        list44.append(q8)
        list45.append(q9)
        list46.append(q10)
        list47.append(q11)
        list48.append(q12)
        list49.append(q13)
        list50.append(q14)
        list51.append(q15)
        list52.append(q16)
        list53.append(q17)
        list54.append(q18)
        list55.append(q19)
        list56.append(q20)
        list57.append(q21)
        list58.append(q22)
        list59.append(q23)
        list60.append(q24)
        list61.append(q25)
        list62.append(q26)
        list63.append(q27)
        list64.append(q28)
        list65.append(q29)
        list66.append(q30)
        list67.append(q31)
        list68.append(q32)
        list69.append(gtotal)

        dict = {'Name': list1, 'City': list2,
                'No of Rooms': list3,
                'Dressing Room': list4, 'All Days Adults': list5,
                'Saturday Only Adults': list6,
                'Sunday Only Adults': list7,
                'Monday Only Adults': list8,

                'Saturday Breakfast Only Adults': list9,
                'Saturday Lunch Only Adults': list10,
                'Saturday Dinner Only Adults': list11,
                'Saturday Bf & Lunch Adults': list12,
                'Saturday Lunch & Dinner Adults': list13,

                'Sunday Breakfast Only Adults': list14,
                'Sunday Lunch Only Adults': list15,
                'sunday Dinner Only Adults': list16,
                'Sunday BF & Lunch Adults': list17,
                'Sunday Lunch & Dinner Adults': list18,

                'Monday Breakfast Only Adults': list19,
                'Monday Lunch Only Adults': list20,

                'All Days Total Adults': list21,
                'Saturday Only Total Adults': list22,
                'Sunday Only Total Adults': list23,
                'Monday Only Total Adults': list24,

                'Saturday Breakfast Only Total Adults': list25,
                'Saturday Lunch Only Total Adults': list26,
                'Saturday Dinner Only Total Adults': list27,
                'Saturday Bf & Lunch Total Adults': list28,
                'Saturday Lunch & Dinner Total Adults': list29,

                'Sunday Breakfast Only Total Adults': list30,
                'Sunday Lunch Only Total Adults': list31,
                'sunday Dinner Only Total Adults': list32,
                'Sunday BF & Lunch Total Adults': list33,
                'Sunday Lunch & Dinner Total Adults': list34,

                'Monday Breakfast Only Total Adults': list35,
                'Monday Lunch Only Total Adults': list36,

                'All Days Kids': list37,
                'Saturday Only Kids': list38,
                'Sunday Only Kids': list39,
                'Monday Only Kids': list40,

                'Saturday Breakfast Only Kids': list41,
                'Saturday Lunch Only Kids': list42,
                'Saturday Dinner Only Kids': list43,
                'Saturday Bf & Lunch Kids': list44,
                'Saturday Lunch & Dinner Kids': list45,

                'Sunday Breakfast Only Kids': list46,
                'Sunday Lunch Only Kids': list47,
                'sunday Dinner Only Kids': list48,
                'Sunday BF & Lunch Kids': list49,
                'Sunday Lunch & Dinner Kids': list50,

                'Monday Breakfast Only Kids': list51,
                'Monday Lunch Only Kids': list52,

                'All Days Total Kids': list53,
                'Saturday Only Total Kids': list54,
                'Sunday Only Total Kids': list55,
                'Monday Only Total Kids': list56,

                'Saturday Breakfast Only Total Kids': list57,
                'Saturday Lunch Only Total Kids': list58,
                'Saturday Dinner Only Total Kids': list59,
                'Saturday Bf & Lunch Total Kids': list60,
                'Saturday Lunch & Dinner Total Kids': list61,

                'Sunday Breakfast Only Total Kids': list62,
                'Sunday Lunch Only Total Kids': list63,
                'sunday Dinner Only Total Kids': list64,
                'Sunday BF & Lunch Total Kids': list65,
                'Sunday Lunch & Dinner Total Kids': list66,

                'Monday Breakfast Only Total Kids': list67,
                'Monday Lunch Only Total Kids': list68,
                'Grand Total Kids': list69

                }
        df = pd.DataFrame(dict)
        df.to_csv('example.csv', mode='a', index=False)
        # df.to_excel('example2.xlsx', sheet_name='example', m)

    # CLEAR EVERYTHING

    def clear():

        name.set("")
        city.set("")
        Room_Rent.set("")
        Dressing_Room.set("")

        all_days_kids.set("")

        saturday_only_kids.set("")
        sunday_only_kids.set("")
        monday_only_kids.set("")

        saturday_breakfast_only_kids.set("")
        saturday_lunch_only_kids.set("")
        saturday_dinner_only_kids.set("")
        saturday_bf_and_lunch_kids.set("")
        saturday_lunch_and_dinner_kids.set("")

        sunday_breakfast_only_kids.set("")
        sunday_lunch_only_kids.set("")
        sunday_dinner_only_kids.set("")
        sunday_bf_and_lunch_kids.set("")
        sunday_lunch_and_dinner_kids.set("")

        monday_breakfast_only_kids.set("")
        monday_lunch_only_kids.set("")
        all_days_kids_total.set("")
        total_kids.set("")

        all_days_adults.set("")
        saturday_only_adults.set("")
        sunday_only_adults.set("")
        monday_only_adults.set("")

        saturday_breakfast_only_adults.set("")
        saturday_lunch_only_adults.set("")
        saturday_dinner_only_adults.set("")
        saturday_bf_and_lunch_adults.set("")
        saturday_lunch_and_dinner_adults.set("")

        sunday_breakfast_only_adults.set("")
        sunday_lunch_only_adults.set("")
        sunday_dinner_only_adults.set("")
        sunday_bf_and_lunch_adults.set("")
        sunday_lunch_and_dinner_adults.set("")
        monday_breakfast_only_adults.set("")
        monday_lunch_only_adults.set("")
        all_days_adults_total.set("")
        total_adults.set("")
        gave.set("")
        returned.set("")
        e1.focus()

    def dressing(*args):
        try:
            u = int(Room_Rent.get())
            if u == 1:
                Dressing_Room.set("0")
            elif u > 1:
                Dressing_Room.set("1")
            else:
                Dressing_Room.set("")
        except:
            Dressing_Room.set("")

    Room_Rent.trace('w', dressing)

    myLabel = Label(root, text="KOOTHAN SIVANTHI - 2022", font=('Comic Sans MS', 22, 'bold'), justify='center')
    myLabel.place(x=475, y=0)

    l1 = Label(root, text='Name', font=('Comic Sans MS', 12))
    l1.place(x=105, y=56)
    e1 = Entry(root, textvariable=name, font=('Arial', 13), width=17)
    e1.place(x=296, y=58)

    l2 = Label(root, text='City', font=('Comic Sans MS', 12))
    l2.place(x=700, y=56)
    e2 = Entry(root, textvariable=city, font=('Arial', 13), width=17)
    e2.place(x=881, y=58)

    date = Label(root, text=f"{dat : %d %B %Y}", font=('Comic Sans MS', 19, 'bold'))
    date.place(x=918, y=4)

    l3 = Label(root, text='No of Rooms', font=('Comic Sans MS', 12))
    l3.place(x=105, y=88)
    e3 = Entry(root, textvariable=Room_Rent, font=('Arial', 13), width=17)
    e3.place(x=296, y=90)

    l4 = Label(root, text='Dressing Room      100', font=('Comic Sans MS', 12))
    l4.place(x=700, y=88)
    e4 = Entry(root, textvariable=Dressing_Room, state='disabled', font=('Arial', 13), width=17)
    e4.place(x=881, y=90)

    l5 = Label(root, text='Adults', font=('Comic Sans MS', 14, 'bold'))
    l5.place(x=249, y=119)

    l6 = Label(root, text='Kids', font=('Comic Sans MS', 14, 'bold'))
    l6.place(x=858, y=119)

    l711 = Label(root, text='Total', font=('Comic Sans MS', 15, 'bold'))
    l711.place(x=1198, y=171)

    l811 = Label(root, text='Grand Total', font=('Comic Sans MS', 14))
    l811.place(x=1062, y=258)
    e811 = Entry(root, textvariable=grand_total, font=('Arial', 14), width=9, state='disabled')
    e811.place(x=1228, y=260)

    l911 = Label(root, text='Given Amount', font=('Comic Sans MS', 14))
    l911.place(x=1062, y=315)
    e911 = Entry(root, textvariable=gave, font=('Arial', 14), width=9)
    e911.place(x=1228, y=317)

    l1011 = Label(root, text='Return Amount', font=('Comic Sans MS', 14))
    l1011.place(x=1062, y=372)
    e1011 = Entry(root, textvariable=returned, font=('Arial', 14), width=9, state='disabled')
    e1011.place(x=1228, y=374)

    # ADULTS_LABELS

    l7 = Label(root, text='All Days                            1100', font=('Comic Sans MS', 12))
    l7.place(x=5, y=151)
    e7 = Entry(root, textvariable=all_days_adults, font=('Arial', 13), width=6)
    e7.place(x=296, y=153)
    e71 = Entry(root, textvariable=all_days_adults_total, font=('Arial', 13), width=8, state='disabled')
    e71.place(x=412, y=153)

    l8 = Label(root, text='Saturday Only                    360', font=('Comic Sans MS', 12))
    l8.place(x=5, y=180)
    e8 = Entry(root, textvariable=saturday_only_adults, font=('Arial', 13), width=6)
    e8.place(x=296, y=182)
    e81 = Entry(root, textvariable=saturday_only_adults_total, font=('Arial', 13), width=8, state='disabled')
    e81.place(x=412, y=182)

    l9 = Label(root, text='Sunday Only                       480', font=('Comic Sans MS', 12))
    l9.place(x=5, y=209)
    e9 = Entry(root, textvariable=sunday_only_adults, font=('Arial', 13), width=6)
    e9.place(x=296, y=211)
    e91 = Entry(root, textvariable=sunday_only_adults_total, font=('Arial', 13), width=8, state='disabled')
    e91.place(x=412, y=211)

    l10 = Label(root, text='Monday Only                      260', font=('Comic Sans MS', 12))
    l10.place(x=5, y=238)
    e10 = Entry(root, textvariable=monday_only_adults, font=('Arial', 13), width=6)
    e10.place(x=296, y=240)
    e101 = Entry(root, textvariable=monday_only_adults_total, font=('Arial', 13), width=8, state='disabled')
    e101.place(x=412, y=240)

    l11 = Label(root, text='Saturday Breakfast Only     150', font=('Comic Sans MS', 12))
    l11.place(x=5, y=267)
    e11 = Entry(root, textvariable=saturday_breakfast_only_adults, font=('Arial', 13), width=6)
    e11.place(x=296, y=269)
    e111 = Entry(root, textvariable=saturday_breakfast_only_adults_total, font=('Arial', 13), width=8, state='disabled')
    e111.place(x=412, y=269)

    l12 = Label(root, text='Saturday Lunch Only           150', font=('Comic Sans MS', 12))
    l12.place(x=5, y=296)
    e12 = Entry(root, textvariable=saturday_lunch_only_adults, font=('Arial', 13), width=6)
    e12.place(x=296, y=298)
    e121 = Entry(root, textvariable=saturday_lunch_only_adults_total, font=('Arial', 13), width=8, state='disabled')
    e121.place(x=412, y=298)

    l13 = Label(root, text='Saturday Dinner Only          150', font=('Comic Sans MS', 12))
    l13.place(x=5, y=325)
    e13 = Entry(root, textvariable=saturday_dinner_only_adults, font=('Arial', 13), width=6)
    e13.place(x=296, y=327)
    e131 = Entry(root, textvariable=saturday_dinner_only_adults_total, font=('Arial', 13), width=8, state='disabled')
    e131.place(x=412, y=327)

    l14 = Label(root, text='Saturday BF and Lunch        300', font=('Comic Sans MS', 12))
    l14.place(x=5, y=354)
    e14 = Entry(root, textvariable=saturday_bf_and_lunch_adults, font=('Arial', 13), width=6)
    e14.place(x=296, y=356)
    e141 = Entry(root, textvariable=saturday_bf_and_lunch_adults_total, font=('Arial', 13), width=8, state='disabled')
    e141.place(x=412, y=356)

    l15 = Label(root, text='Saturday Lunch and Dinner  300', font=('Comic Sans MS', 12))
    l15.place(x=5, y=383)
    e15 = Entry(root, textvariable=saturday_lunch_and_dinner_adults, font=('Arial', 13), width=6)
    e15.place(x=296, y=385)
    e151 = Entry(root, textvariable=saturday_lunch_and_dinner_adults_total, font=('Arial', 13), width=8,
                 state='disabled')
    e151.place(x=412, y=385)

    l16 = Label(root, text='Sunday Breakfast Only        200', font=('Comic Sans MS', 12))
    l16.place(x=5, y=412)
    e16 = Entry(root, textvariable=sunday_breakfast_only_adults, font=('Arial', 13), width=6)
    e16.place(x=296, y=414)
    e161 = Entry(root, textvariable=sunday_breakfast_only_adults_total, font=('Arial', 13), width=8, state='disabled')
    e161.place(x=412, y=414)

    l17 = Label(root, text='Sunday Lunch Only              250', font=('Comic Sans MS', 12))
    l17.place(x=5, y=441)
    e17 = Entry(root, textvariable=sunday_lunch_only_adults, font=('Arial', 13), width=6)
    e17.place(x=296, y=443)
    e171 = Entry(root, textvariable=sunday_lunch_only_adults_total, font=('Arial', 13), width=8, state='disabled')
    e171.place(x=412, y=443)

    l18 = Label(root, text='Sunday Dinner Only             150', font=('Comic Sans MS', 12))
    l18.place(x=5, y=470)
    e18 = Entry(root, textvariable=sunday_dinner_only_adults, font=('Arial', 13), width=6)
    e18.place(x=296, y=472)
    e181 = Entry(root, textvariable=sunday_dinner_only_adults_total, font=('Arial', 13), width=8, state='disabled')
    e181.place(x=412, y=472)

    l19 = Label(root, text='Sunday BF and Lunch           450', font=('Comic Sans MS', 12))
    l19.place(x=5, y=499)
    e19 = Entry(root, textvariable=sunday_bf_and_lunch_adults, font=('Arial', 13), width=6)
    e19.place(x=296, y=501)
    e191 = Entry(root, textvariable=sunday_bf_and_lunch_adults_total, font=('Arial', 13), width=8, state='disabled')
    e191.place(x=412, y=501)

    l20 = Label(root, text='Sunday Lunch and Dinner     430', font=('Comic Sans MS', 12))
    l20.place(x=5, y=528)
    e20 = Entry(root, textvariable=sunday_lunch_and_dinner_adults, font=('Arial', 13), width=6)
    e20.place(x=296, y=530)
    e201 = Entry(root, textvariable=sunday_lunch_and_dinner_adults_total, font=('Arial', 13), width=8, state='disabled')
    e201.place(x=412, y=530)

    l21 = Label(root, text='Monday Breakfast Only       130', font=('Comic Sans MS', 12))
    l21.place(x=5, y=557)
    e21 = Entry(root, textvariable=monday_breakfast_only_adults, font=('Arial', 13), width=6)
    e21.place(x=296, y=559)
    e211 = Entry(root, textvariable=monday_breakfast_only_adults_total, font=('Arial', 13), width=8, state='disabled')
    e211.place(x=412, y=559)

    l22 = Label(root, text='Monday Lunch Only             150', font=('Comic Sans MS', 12))
    l22.place(x=5, y=586)
    e22 = Entry(root, textvariable=monday_lunch_only_adults, font=('Arial', 13), width=6)
    e22.place(x=296, y=588)
    e221 = Entry(root, textvariable=monday_lunch_only_adults_total, font=('Arial', 13), width=8, state='disabled')
    e221.place(x=412, y=588)

    l23 = Label(root, text='Total Adults', font=('Comic Sans MS', 14))
    l23.place(x=5, y=642)
    e23 = Entry(root, textvariable=total_adults, font=('Arial', 15), width=8, state='disabled')
    e23.place(x=412, y=639)

    # KIDS_LABELS

    l24 = Label(root, text='All Days                              900', font=('Comic Sans MS', 12))
    l24.place(x=530, y=151)
    e24 = Entry(root, textvariable=all_days_kids, font=('Arial', 13), width=6)
    e24.place(x=821, y=153)
    e241 = Entry(root, textvariable=all_days_kids_total, font=('Arial', 13), width=8, state='disabled')
    e241.place(x=957, y=153)

    l25 = Label(root, text='Saturday Only                     280', font=('Comic Sans MS', 12))
    l25.place(x=530, y=180)
    e25 = Entry(root, textvariable=saturday_only_kids, font=('Arial', 13), width=6)
    e25.place(x=821, y=182)
    e251 = Entry(root, textvariable=saturday_only_kids_total, font=('Arial', 13), width=8, state='disabled')
    e251.place(x=957, y=182)

    l26 = Label(root, text='Sunday Only                        400', font=('Comic Sans MS', 12))
    l26.place(x=530, y=209)
    e26 = Entry(root, textvariable=sunday_only_kids, font=('Arial', 13), width=6)
    e26.place(x=821, y=211)
    e261 = Entry(root, textvariable=sunday_only_kids_total, font=('Arial', 13), width=8, state='disabled')
    e261.place(x=957, y=211)

    l27 = Label(root, text='Monday Only                       220', font=('Comic Sans MS', 12))
    l27.place(x=530, y=238)
    e27 = Entry(root, textvariable=monday_only_kids, font=('Arial', 13), width=6)
    e27.place(x=821, y=240)
    e271 = Entry(root, textvariable=monday_only_kids_total, font=('Arial', 13), width=8, state='disabled')
    e271.place(x=957, y=240)

    l28 = Label(root, text='Saturday Breakfast Only      100', font=('Comic Sans MS', 12))
    l28.place(x=530, y=267)
    e28 = Entry(root, textvariable=saturday_breakfast_only_kids, font=('Arial', 13), width=6)
    e28.place(x=821, y=269)
    e281 = Entry(root, textvariable=saturday_breakfast_only_kids_total, font=('Arial', 13), width=8, state='disabled')
    e281.place(x=957, y=269)

    l29 = Label(root, text='Saturday Lunch Only            100', font=('Comic Sans MS', 12))
    l29.place(x=530, y=296)
    e29 = Entry(root, textvariable=saturday_lunch_only_kids, font=('Arial', 13), width=6)
    e29.place(x=821, y=298)
    e291 = Entry(root, textvariable=saturday_lunch_only_kids_total, font=('Arial', 13), width=8, state='disabled')
    e291.place(x=957, y=298)

    l30 = Label(root, text='Saturday Dinner Only           100', font=('Comic Sans MS', 12))
    l30.place(x=530, y=325)
    e30 = Entry(root, textvariable=saturday_dinner_only_kids, font=('Arial', 13), width=6)
    e30.place(x=821, y=327)
    e301 = Entry(root, textvariable=saturday_dinner_only_kids_total, font=('Arial', 13), width=8, state='disabled')
    e301.place(x=957, y=327)

    l31 = Label(root, text='Saturday BF and Lunch         200', font=('Comic Sans MS', 12))
    l31.place(x=530, y=354)
    e31 = Entry(root, textvariable=saturday_bf_and_lunch_kids, font=('Arial', 13), width=6)
    e31.place(x=821, y=356)
    e311 = Entry(root, textvariable=saturday_bf_and_lunch_kids_total, font=('Arial', 13), width=8, state='disabled')
    e311.place(x=957, y=356)

    l32 = Label(root, text='Saturday Lunch and Dinner   200', font=('Comic Sans MS', 12))
    l32.place(x=530, y=383)
    e32 = Entry(root, textvariable=saturday_lunch_and_dinner_kids, font=('Arial', 13), width=6)
    e32.place(x=821, y=385)
    e321 = Entry(root, textvariable=saturday_lunch_and_dinner_kids_total, font=('Arial', 13), width=8, state='disabled')
    e321.place(x=957, y=385)

    l33 = Label(root, text='Sunday Breakfast Only         150', font=('Comic Sans MS', 12))
    l33.place(x=530, y=412)
    e33 = Entry(root, textvariable=sunday_breakfast_only_kids, font=('Arial', 13), width=6)
    e33.place(x=821, y=414)
    e331 = Entry(root, textvariable=sunday_breakfast_only_kids_total, font=('Arial', 13), width=8, state='disabled')
    e331.place(x=957, y=414)

    l34 = Label(root, text='Sunday Lunch Only               150', font=('Comic Sans MS', 12))
    l34.place(x=530, y=441)
    e34 = Entry(root, textvariable=sunday_lunch_only_kids, font=('Arial', 13), width=6)
    e34.place(x=821, y=443)
    e341 = Entry(root, textvariable=sunday_lunch_only_kids_total, font=('Arial', 13), width=8, state='disabled')
    e341.place(x=957, y=443)

    l35 = Label(root, text='Sunday Dinner Only              100', font=('Comic Sans MS', 12))
    l35.place(x=530, y=470)
    e35 = Entry(root, textvariable=sunday_dinner_only_kids, font=('Arial', 13), width=6)
    e35.place(x=821, y=472)
    e351 = Entry(root, textvariable=sunday_dinner_only_kids_total, font=('Arial', 13), width=8, state='disabled')
    e351.place(x=957, y=472)

    l36 = Label(root, text='Sunday BF and Lunch            300', font=('Comic Sans MS', 12))
    l36.place(x=530, y=499)
    e36 = Entry(root, textvariable=sunday_bf_and_lunch_kids, font=('Arial', 13), width=6)
    e36.place(x=821, y=501)
    e361 = Entry(root, textvariable=sunday_bf_and_lunch_kids_total, font=('Arial', 13), width=8, state='disabled')
    e361.place(x=957, y=501)

    l37 = Label(root, text='Sunday Lunch and Dinner      250', font=('Comic Sans MS', 12))
    l37.place(x=530, y=528)
    e37 = Entry(root, textvariable=sunday_lunch_and_dinner_kids, font=('Arial', 13), width=6)
    e37.place(x=821, y=530)
    e371 = Entry(root, textvariable=sunday_lunch_and_dinner_kids_total, font=('Arial', 13), width=8, state='disabled')
    e371.place(x=957, y=530)

    l38 = Label(root, text='Monday Breakfast Only        100', font=('Comic Sans MS', 12))
    l38.place(x=530, y=557)
    e38 = Entry(root, textvariable=monday_breakfast_only_kids, font=('Arial', 13), width=6)
    e38.place(x=821, y=559)
    e381 = Entry(root, textvariable=monday_breakfast_only_kids_total, font=('Arial', 13), width=8, state='disabled')
    e381.place(x=957, y=559)

    l39 = Label(root, text='Monday Lunch Only              130', font=('Comic Sans MS', 12))
    l39.place(x=530, y=586)
    e39 = Entry(root, textvariable=monday_lunch_only_kids, font=('Arial', 13), width=6)
    e39.place(x=821, y=588)
    e391 = Entry(root, textvariable=monday_lunch_only_kids_total, font=('Arial', 13), width=8, state='disabled')
    e391.place(x=957, y=588)

    l40 = Label(root, text='Total Kids', font=('Comic Sans MS', 14))
    l40.place(x=530, y=642)
    e40 = Entry(root, textvariable=total_kids, font=('Arial', 15), width=8, state='disabled')
    e40.place(x=957, y=642)

    photo3 = PhotoImage(file="download.png")
    photoimage3 = photo3.subsample(15, 15)

    z1 = Button(root, text='Save ', font=('Cosmic Sans MS', 17), command=save, image=photoimage3, compound=RIGHT,
                bg='#A2A2CD', cursor='hand2')
    z1.place(x=1084, y=451)

    photo5 = PhotoImage(file="printing.png")
    photoimage6 = photo5.subsample(15, 15)

    z3 = Button(root, text='Print  ', image=photoimage6, font=('Cosmic Sans MS', 17), command=sample_bill,
                compound=RIGHT,
                bg='#A2A2CD', cursor='hand2')
    z3.place(x=1234, y=451)

    photo4 = PhotoImage(file="delete.png")
    photoimage4 = photo4.subsample(15, 15)

    z2 = Button(root, text='Clear ', font=('Cosmic Sans MS', 17), command=clear, image=photoimage4, compound=RIGHT,
                bg='#A2A2CD', cursor='hand2')
    z2.place(x=1158, y=531)

    # KIDS TOTAL AMOUNT

    def tot1(*args):
        x = all_days_kids.get()
        if x != '':
            all_days_kids_total.set(str(int(b) * int(x)))
        else:
            all_days_kids_total.set("")
            x = '0'

        x1 = saturday_only_kids.get()
        if x1 != '':
            saturday_only_kids_total.set(str(int(b1) * int(x1)))
        else:
            saturday_only_kids_total.set("")
            x1 = '0'

        x2 = sunday_only_kids.get()
        if x2 != '':
            sunday_only_kids_total.set(str(int(b2) * int(x2)))
        else:
            sunday_only_kids_total.set("")
            x2 = '0'
        x3 = monday_only_kids.get()
        if x3 != '':
            monday_only_kids_total.set(str(int(b3) * int(x3)))
        else:
            monday_only_kids_total.set("")
            x3 = '0'
        x4 = saturday_breakfast_only_kids.get()
        if x4 != '':
            saturday_breakfast_only_kids_total.set(str(int(b4) * int(x4)))
        else:
            saturday_breakfast_only_kids_total.set("")
            x4 = '0'
        x5 = saturday_lunch_only_kids.get()
        if x5 != '':
            saturday_lunch_only_kids_total.set(str(int(b5) * int(x5)))
        else:
            saturday_lunch_only_kids_total.set("")
            x5 = '0'
        x6 = saturday_dinner_only_kids.get()
        if x6 != '':
            saturday_dinner_only_kids_total.set(str(int(b6) * int(x6)))
        else:
            saturday_dinner_only_kids_total.set("")
            x6 = '0'
        x7 = saturday_bf_and_lunch_kids.get()
        if x7 != '':
            saturday_bf_and_lunch_kids_total.set(str(int(b7) * int(x7)))
        else:
            saturday_bf_and_lunch_kids_total.set("")
            x7 = '0'
        x8 = saturday_lunch_and_dinner_kids.get()
        if x8 != '':
            saturday_lunch_and_dinner_kids_total.set(str(int(b8) * int(x8)))
        else:
            saturday_lunch_and_dinner_kids_total.set("")
            x8 = '0'

        x9 = sunday_breakfast_only_kids.get()
        if x9 != '':
            sunday_breakfast_only_kids_total.set(str(int(b9) * int(x9)))
        else:
            sunday_breakfast_only_kids_total.set("")
            x9 = '0'

        x10 = sunday_lunch_only_kids.get()
        if x10 != '':
            sunday_lunch_only_kids_total.set(str(int(b10) * int(x10)))
        else:
            sunday_lunch_only_kids_total.set("")
            x10 = '0'
        x11 = sunday_dinner_only_kids.get()
        if x11 != '':
            sunday_dinner_only_kids_total.set(str(int(b11) * int(x11)))
        else:
            sunday_dinner_only_kids_total.set("")
            x11 = '0'
        x12 = sunday_bf_and_lunch_kids.get()
        if x12 != '':
            sunday_bf_and_lunch_kids_total.set(str(int(b12) * int(x12)))
        else:
            sunday_bf_and_lunch_kids_total.set("")
            x12 = '0'
        x13 = sunday_lunch_and_dinner_kids.get()
        if x13 != '':
            sunday_lunch_and_dinner_kids_total.set(str(int(b13) * int(x13)))
        else:
            sunday_lunch_and_dinner_kids_total.set("")
            x13 = '0'

        x14 = monday_breakfast_only_kids.get()
        if x14 != '':
            monday_breakfast_only_kids_total.set(str(int(b14) * int(x14)))
        else:
            monday_breakfast_only_kids_total.set("")
            x14 = '0'
        x15 = monday_lunch_only_kids.get()
        if x15 != '':
            monday_lunch_only_kids_total.set(str(int(b15) * int(x15)))
        else:
            monday_lunch_only_kids_total.set("")
            x15 = '0'

        try:
            total1 = int(x) * int(b) + int(x1) * int(b1) + int(x2) * int(b2) + int(x3) * int(b3) + int(x4) * int(
                b4) + int(
                x5) * int(b5) + int(x6) * int(b6) + int(x7) * int(b7) + int(x8) * int(b8) + int(x9) * int(b9) + int(
                x10) * int(
                b10) + int(x11) * int(b11) + int(x12) * int(b12) + int(x13) * int(b13) + int(x14) * int(b14) + int(
                x15) * int(b15)

            total_kids.set(str(total1))
        except:
            total_kids.set("")

    # Grand Total

    def gtotal(*args):
        x = all_days_kids_total.get()
        if x == '':
            x = '0'

        x1 = saturday_only_kids_total.get()
        if x1 == '':
            x1 = '0'

        x2 = sunday_only_kids_total.get()
        if x2 == '':
            x2 = '0'

        x3 = monday_only_kids_total.get()
        if x3 == '':
            x3 = '0'
        x4 = saturday_breakfast_only_kids_total.get()
        if x4 == '':
            x4 = '0'

        x5 = saturday_lunch_only_kids_total.get()
        if x5 == '':
            x5 = '0'

        x6 = saturday_dinner_only_kids_total.get()
        if x6 == '':
            x6 = '0'

        x7 = saturday_bf_and_lunch_kids_total.get()
        if x7 == '':
            x7 = '0'

        x8 = saturday_lunch_and_dinner_kids_total.get()
        if x8 == '':
            x8 = '0'

        x9 = sunday_breakfast_only_kids_total.get()
        if x9 == '':
            x9 = '0'

        x10 = sunday_lunch_only_kids_total.get()
        if x10 == '':
            x10 = '0'

        x11 = sunday_dinner_only_kids_total.get()
        if x11 == '':
            x11 = '0'
        x12 = sunday_bf_and_lunch_kids_total.get()
        if x12 == '':
            x12 = '0'

        x13 = sunday_lunch_and_dinner_kids_total.get()
        if x13 == '':
            x13 = '0'

        x14 = monday_breakfast_only_kids_total.get()
        if x14 == '':
            x14 = '0'

        x15 = monday_lunch_only_kids_total.get()
        if x15 == '':
            x15 = '0'

        y = all_days_adults_total.get()
        if y == '':
            y = '0'

        y1 = saturday_only_adults_total.get()
        if y1 == '':
            y1 = '0'

        y2 = sunday_only_adults_total.get()
        if y2 == '':
            y2 = '0'

        y3 = monday_only_adults_total.get()
        if y3 == '':
            y3 = '0'
        y4 = saturday_breakfast_only_adults_total.get()
        if y4 == '':
            y4 = '0'

        y5 = saturday_lunch_only_adults_total.get()
        if y5 == '':
            y5 = '0'

        y6 = saturday_dinner_only_adults_total.get()
        if y6 == '':
            y6 = '0'

        y7 = saturday_bf_and_lunch_adults_total.get()
        if y7 == '':
            y7 = '0'

        y8 = saturday_lunch_and_dinner_adults_total.get()
        if y8 == '':
            y8 = '0'

        y9 = sunday_breakfast_only_adults_total.get()
        if y9 == '':
            y9 = '0'

        y10 = sunday_lunch_only_adults_total.get()
        if y10 == '':
            y10 = '0'

        y11 = sunday_dinner_only_adults_total.get()
        if y11 == '':
            y11 = '0'
        y12 = sunday_bf_and_lunch_adults_total.get()
        if y12 == '':
            y12 = '0'

        y13 = sunday_lunch_and_dinner_adults_total.get()
        if y13 == '':
            y13 = '0'

        y14 = monday_breakfast_only_adults_total.get()
        if y14 == '':
            y14 = '0'

        y15 = monday_lunch_only_adults_total.get()
        if y15 == '':
            y15 = '0'

        z4 = Room_Rent.get()
        if z4 == '':
            z4 = '0'

        z5 = Dressing_Room.get()
        if z5 == '':
            z5 = '0'
        try:
            total = int(x) + int(x1) + int(x2) + int(x3) + int(x4) + int(x5) + int(x6) + int(x7) + int(x8) + int(
                x9) + int(
                x10) + int(x11) + int(x12) + int(x13) + int(x14) + int(x15) + int(y) + int(y1) + int(y2) + int(
                y3) + int(
                y4) + int(y5) + int(y6) + int(y7) + int(y8) + int(y9) + int(y10) + int(y11) + int(y12) + int(y13) + int(
                y14) + int(y15) + int(z4) * int(c1) + int(z5) * int(c2)
            grand_total.set(str(total))

        except:
            grand_total.set("")

    def return_amount(*args):
        try:
            i = int(grand_total.get())
            r = int(gave.get())

            if r >= i:
                r1 = r - i
                returned.set(str(r1))
            else:
                returned.set("")
        except:
            returned.set("")

    gave.trace('w', return_amount)

    Room_Rent.trace('w', gtotal)
    Dressing_Room.trace('w', gtotal)
    all_days_kids.trace('w', gtotal)

    saturday_only_kids.trace('w', gtotal)
    sunday_only_kids.trace('w', gtotal)
    monday_only_kids.trace('w', gtotal)

    saturday_breakfast_only_kids.trace('w', gtotal)
    saturday_lunch_only_kids.trace('w', gtotal)
    saturday_dinner_only_kids.trace('w', gtotal)
    saturday_bf_and_lunch_kids.trace('w', gtotal)
    saturday_lunch_and_dinner_kids.trace('w', gtotal)

    sunday_breakfast_only_kids.trace('w', gtotal)
    sunday_lunch_only_kids.trace('w', gtotal)
    sunday_dinner_only_kids.trace('w', gtotal)
    sunday_bf_and_lunch_kids.trace('w', gtotal)
    sunday_lunch_and_dinner_kids.trace('w', gtotal)

    monday_breakfast_only_kids.trace('w', gtotal)
    monday_lunch_only_kids.trace('w', gtotal)

    all_days_adults.trace('w', gtotal)
    saturday_only_adults.trace('w', gtotal)
    sunday_only_adults.trace('w', gtotal)
    monday_only_adults.trace('w', gtotal)

    saturday_breakfast_only_adults.trace('w', gtotal)
    saturday_lunch_only_adults.trace('w', gtotal)
    saturday_dinner_only_adults.trace('w', gtotal)
    saturday_bf_and_lunch_adults.trace('w', gtotal)
    saturday_lunch_and_dinner_adults.trace('w', gtotal)

    sunday_breakfast_only_adults.trace('w', gtotal)
    sunday_lunch_only_adults.trace('w', gtotal)
    sunday_dinner_only_adults.trace('w', gtotal)
    sunday_bf_and_lunch_adults.trace('w', gtotal)
    sunday_lunch_and_dinner_adults.trace('w', gtotal)
    monday_breakfast_only_adults.trace('w', gtotal)
    monday_lunch_only_adults.trace('w', gtotal)

    all_days_kids.trace('w', tot1)

    saturday_only_kids.trace('w', tot1)
    sunday_only_kids.trace('w', tot1)
    monday_only_kids.trace('w', tot1)

    saturday_breakfast_only_kids.trace('w', tot1)
    saturday_lunch_only_kids.trace('w', tot1)
    saturday_dinner_only_kids.trace('w', tot1)
    saturday_bf_and_lunch_kids.trace('w', tot1)
    saturday_lunch_and_dinner_kids.trace('w', tot1)

    sunday_breakfast_only_kids.trace('w', tot1)
    sunday_lunch_only_kids.trace('w', tot1)
    sunday_dinner_only_kids.trace('w', tot1)
    sunday_bf_and_lunch_kids.trace('w', tot1)
    sunday_lunch_and_dinner_kids.trace('w', tot1)

    monday_breakfast_only_kids.trace('w', tot1)
    monday_lunch_only_kids.trace('w', tot1)

    # ADULTS TOTAL AMOUNT

    def tot2(*args):
        y = all_days_adults.get()

        if y != '':
            all_days_adults_total.set(str(int(a) * int(y)))
        else:
            all_days_adults_total.set('')
            y = '0'
        y0 = saturday_only_adults.get()
        if y0 != '':
            saturday_only_adults_total.set(str(int(a0) * int(y0)))
        else:
            saturday_only_adults_total.set('')
            y0 = '0'
        y1 = sunday_only_adults.get()
        if y1 != '':
            sunday_only_adults_total.set(str(int(a1) * int(y1)))
        else:
            sunday_only_adults_total.set('')
            y1 = '0'
        y2 = monday_only_adults.get()
        if y2 != '':
            monday_only_adults_total.set(str(int(a2) * int(y2)))
        else:
            monday_only_adults_total.set('')
            y2 = '0'
        y3 = saturday_breakfast_only_adults.get()
        if y3 != '':
            saturday_breakfast_only_adults_total.set(str(int(a3) * int(y3)))
        else:
            saturday_breakfast_only_adults_total.set('')
            y3 = '0'
        y4 = saturday_lunch_only_adults.get()
        if y4 != '':
            saturday_lunch_only_adults_total.set(str(int(a4) * int(y4)))
        else:
            saturday_lunch_only_adults_total.set('')
            y4 = '0'
        y5 = saturday_dinner_only_adults.get()
        if y5 != '':
            saturday_dinner_only_adults_total.set(str(int(a5) * int(y5)))
        else:
            saturday_dinner_only_adults_total.set('')
            y5 = '0'
        y6 = saturday_bf_and_lunch_adults.get()
        if y6 != '':
            saturday_bf_and_lunch_adults_total.set(str(int(a6) * int(y6)))
        else:
            saturday_bf_and_lunch_adults_total.set('')
            y6 = '0'
        y7 = saturday_lunch_and_dinner_adults.get()
        if y7 != '':
            saturday_lunch_and_dinner_adults_total.set(str(int(a7) * int(y7)))
        else:
            saturday_lunch_and_dinner_adults_total.set('')
            y7 = '0'
        y8 = sunday_breakfast_only_adults.get()
        if y8 != '':
            sunday_breakfast_only_adults_total.set(str(int(a8) * int(y8)))
        else:
            sunday_breakfast_only_adults_total.set('')
            y8 = '0'
        y9 = sunday_lunch_only_adults.get()
        if y9 != '':
            sunday_lunch_only_adults_total.set(str(int(a9) * int(y9)))
        else:
            sunday_lunch_only_adults_total.set('')
            y9 = '0'
        y10 = sunday_dinner_only_adults.get()
        if y10 != '':
            sunday_dinner_only_adults_total.set(str(int(a10) * int(y10)))
        else:
            sunday_dinner_only_adults_total.set('')
            y10 = '0'
        y11 = sunday_bf_and_lunch_adults.get()
        if y11 != '':
            sunday_bf_and_lunch_adults_total.set(str(int(a11) * int(y11)))
        else:
            sunday_bf_and_lunch_adults_total.set('')
            y11 = '0'
        y12 = sunday_lunch_and_dinner_adults.get()
        if y12 != '':
            sunday_lunch_and_dinner_adults_total.set(str(int(a12) * int(y12)))
        else:
            sunday_lunch_and_dinner_adults_total.set('')
            y12 = '0'

        y13 = monday_breakfast_only_adults.get()
        if y13 != '':
            monday_breakfast_only_adults_total.set(str(int(a13) * int(y13)))
        else:
            monday_breakfast_only_adults_total.set('')
            y13 = '0'
        y14 = monday_lunch_only_adults.get()
        if y14 != '':
            monday_lunch_only_adults_total.set(str(int(a14) * int(y14)))
        else:
            monday_lunch_only_adults_total.set('')
            y14 = '0'

        try:
            r1 = int(y) * int(a) + int(y0) * int(a0) + int(y1) * int(a1) + int(y2) * int(a2) + int(y3) * int(a3) + int(
                y4) * int(
                a4) + int(y5) * int(a5) + int(y6) * int(a6) + int(y7) * int(a7) + int(y8) * int(a8)
            r2 = int(y9) * int(a9) + int(y10) * int(a10) + int(y11) * int(a11) + int(y12) * int(a12) + int(y13) * int(
                a13) + int(y14) * int(a14)
            total2 = r1 + r2
            total_adults.set(str(total2))

        except:
            total_adults.set("")

    all_days_adults.trace('w', tot2)
    saturday_only_adults.trace('w', tot2)
    sunday_only_adults.trace('w', tot2)
    monday_only_adults.trace('w', tot2)

    saturday_breakfast_only_adults.trace('w', tot2)
    saturday_lunch_only_adults.trace('w', tot2)
    saturday_dinner_only_adults.trace('w', tot2)
    saturday_bf_and_lunch_adults.trace('w', tot2)
    saturday_lunch_and_dinner_adults.trace('w', tot2)

    sunday_breakfast_only_adults.trace('w', tot2)
    sunday_lunch_only_adults.trace('w', tot2)
    sunday_dinner_only_adults.trace('w', tot2)
    sunday_bf_and_lunch_adults.trace('w', tot2)
    sunday_lunch_and_dinner_adults.trace('w', tot2)
    monday_breakfast_only_adults.trace('w', tot2)
    monday_lunch_only_adults.trace('w', tot2)

    # Scroll between boxes using keyboard keys

    def f1(event):
        e8.focus()

    e7.bind('<Down>', f1)

    def f2(event):
        e9.focus()

    e8.bind('<Down>', f2)

    def f3(event):
        e10.focus()

    e9.bind('<Down>', f3)

    def f4(event):
        e11.focus()

    e10.bind('<Down>', f4)

    def f5(event):
        e12.focus()

    e11.bind('<Down>', f5)

    def f6(event):
        e13.focus()

    e12.bind('<Down>', f6)

    def f7(event):
        e14.focus()

    e13.bind('<Down>', f7)

    def f8(event):
        e15.focus()

    e14.bind('<Down>', f8)

    def f9(event):
        e16.focus()

    e15.bind('<Down>', f9)

    def f10(event):
        e17.focus()

    e16.bind('<Down>', f10)

    def f11(event):
        e18.focus()

    e17.bind('<Down>', f11)

    def f12(event):
        e19.focus()

    e18.bind('<Down>', f12)

    def f13(event):
        e20.focus()

    e19.bind('<Down>', f13)

    def f14(event):
        e21.focus()

    e20.bind('<Down>', f14)

    def f15(event):
        e22.focus()

    e21.bind('<Down>', f15)

    def f16(event):
        e24.focus()

    e22.bind('<Down>', f16)
    e22.bind('<Right>', f16)

    def g1(event):
        e7.focus()

    e7.bind('<Up>', g1)

    def g2(event):
        e7.focus()

    e8.bind('<Up>', g2)

    def g3(event):
        e8.focus()

    e9.bind('<Up>', g3)

    def g4(event):
        e9.focus()

    e10.bind('<Up>', g4)

    def g5(event):
        e10.focus()

    e11.bind('<Up>', g5)

    def g6(event):
        e11.focus()

    e12.bind('<Up>', g6)

    def g7(event):
        e12.focus()

    e13.bind('<Up>', g7)

    def g8(event):
        e13.focus()

    e14.bind('<Up>', g8)

    def g9(event):
        e14.focus()

    e15.bind('<Up>', g9)

    def g10(event):
        e15.focus()

    e16.bind('<Up>', g10)

    def g11(event):
        e16.focus()

    e17.bind('<Up>', g11)

    def g12(event):
        e17.focus()

    e18.bind('<Up>', g12)

    def g13(event):
        e18.focus()

    e19.bind('<Up>', g13)

    def g14(event):
        e19.focus()

    e20.bind('<Up>', g14)

    def g15(event):
        e20.focus()

    e21.bind('<Up>', g15)

    def g16(event):
        e21.focus()

    e22.bind('<Up>', g16)

    def h1(event):
        e25.focus()

    e24.bind('<Down>', h1)

    def h2(event):
        e26.focus()

    e25.bind('<Down>', h2)

    def h3(event):
        e27.focus()

    e26.bind('<Down>', h3)

    def h4(event):
        e28.focus()

    e27.bind('<Down>', h4)

    def h5(event):
        e29.focus()

    e28.bind('<Down>', h5)

    def h6(event):
        e30.focus()

    e29.bind('<Down>', h6)

    def h7(event):
        e31.focus()

    e30.bind('<Down>', h7)

    def h8(event):
        e32.focus()

    e31.bind('<Down>', h8)

    def h9(event):
        e33.focus()

    e32.bind('<Down>', h9)

    def h10(event):
        e34.focus()

    e33.bind('<Down>', h10)

    def h11(event):
        e35.focus()

    e34.bind('<Down>', h11)

    def h12(event):
        e36.focus()

    e35.bind('<Down>', h12)

    def h13(event):
        e37.focus()

    e36.bind('<Down>', h13)

    def h14(event):
        e38.focus()

    e37.bind('<Down>', h14)

    def h15(event):
        e39.focus()

    e38.bind('<Down>', h15)

    def k1(event):
        e22.focus()

    e24.bind('<Left>', k1)
    e24.bind('<Up>', k1)

    def k2(event):
        e24.focus()

    e25.bind('<Up>', k2)

    def k3(event):
        e25.focus()

    e26.bind('<Up>', k3)

    def k4(event):
        e26.focus()

    e27.bind('<Up>', k4)

    def k5(event):
        e27.focus()

    e28.bind('<Up>', k5)

    def k6(event):
        e28.focus()

    e29.bind('<Up>', k6)

    def k7(event):
        e29.focus()

    e30.bind('<Up>', k7)

    def k8(event):
        e30.focus()

    e31.bind('<Up>', k8)

    def k9(event):
        e31.focus()

    e32.bind('<Up>', k9)

    def k10(event):
        e32.focus()

    e33.bind('<Up>', k10)

    def k11(event):
        e33.focus()

    e34.bind('<Up>', k11)

    def k12(event):
        e34.focus()

    e35.bind('<Up>', k12)

    def k13(event):
        e35.focus()

    e36.bind('<Up>', k13)

    def k14(event):
        e36.focus()

    e37.bind('<Up>', k14)

    def k15(event):
        e37.focus()

    e38.bind('<Up>', k15)

    def k16(event):
        e38.focus()

    e39.bind('<Up>', k16)

    photo = PhotoImage(file="home.png")
    photoimage = photo.subsample(11, 11)

    def back():

        root.destroy()
        win.state(newstate='normal')

    o = Button(root, image=photoimage, text='Home', compound=TOP, font=('Comic Sans MS', 12), bg='#A2A2CD',
               command=back, cursor='hand2')
    o.place(x=10, y=10)

    def on_closing_2():
        msg = messagebox.askquestion('Exit Application', 'Are you sure you want to qui?', icon='warning')
        if msg == 'yes':
            root.destroy()
            win.state(newstate='normal')

    img = Image.open('IMG_20220908_124140.jpg')
    img = img.resize((274, 193), Image.Resampling.LANCZOS)
    d = ImageTk.PhotoImage(img)
    d1 = Label(root, image=d)
    d1.place(x=1071, y=48)

    root.state('zoomed')
    root.protocol("WM_DELETE_WINDOW", on_closing_2)
    win.state(newstate='iconic')
    root.mainloop()


def _open_3():
    root = Toplevel()
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

    myLabel = Label(root, text="KOOTHAN SIVANTHI - 2022", font=('Comic Sans MS', 22, 'bold'), justify='center')
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
        msg = messagebox.askquestion('Exit Application', 'Are you sure you want to qui?', icon='warning')
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


dat = dt.datetime.now()
win.title('Vembar')

photo1 = PhotoImage(file="right-arrow.png")
photoimage = photo1.subsample(11, 11)

myLabel = Label(win, text="KOOTHAN SIVANTHI - 2022", font=('Comic Sans MS', 22, 'bold'), justify='center')
myLabel.place(x=475, y=0)

date = Label(win, text=f"{dat : %d %B %Y}", font=('Comic Sans MS', 19, 'bold'))
date.place(x=918, y=4)

b1 = Button(win, image=photoimage, width=250, text="Room           ", font=('Cosmic Sans MS', 23), command=_open,
            compound=RIGHT, cursor='hand2',
            bg='#A2A2CD')
b1.place(x=596, y=197)

b2 = Button(win, image=photoimage, width=250, text="Nankodai       ", font=('Cosmic Sans MS', 23), command=_open_2,
            compound=RIGHT, cursor='hand2',
            bg='#A2A2CD')
b2.place(x=596, y=310)

b3 = Button(win, image=photoimage, width=250, text="Pirandhapillai ", font=('Cosmic Sans MS', 23), command=_open_3,
            compound=RIGHT,
            bg='#A2A2CD', cursor='hand2')
b3.place(x=596, y=423)


def on_closing_3():
    msg = messagebox.askquestion('Exit Application', 'Are you sure you want to quit?', icon='warning')
    if msg == 'yes':
        win.destroy()


img = Image.open('IMG_20220908_124140.jpg')
img = img.resize((450, 400), Image.Resampling.LANCZOS)
d = ImageTk.PhotoImage(img)
d1 = Label(win, image=d)
d1.place(x=893, y=140)

win.protocol("WM_DELETE_WINDOW", on_closing_3)
win.state('zoomed')

win.mainloop()
