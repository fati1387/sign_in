from tkinter import *
from tkinter import messagebox
import data

win = Tk()
win.title('Login Form')
win.geometry('530x280')
win.configure(bg='#ff0000')

db = data.Database('c:/project3/database.db')

#=======func===========
def sign_up():
    fname = ent_fname.get()
    lname = ent_lname.get()
    email = ent_email.get()
    password = ent_password.get()
    if len(email)== 0 or len(password) == 0:
        messagebox.showerror('Error', 'Email and Password are required!')
        return
    else:
        db.insert(fname, lname, email, password)
        messagebox.showinfo('Success', 'User added successfully!')
        clear()

def sign_in():
    email = ent_email.get()
    password = ent_password.get()
    if len(email)== 0 or len(password) == 0:
        messagebox.showerror('Error', 'Email and Password are required!')
        return
    else:
        data = db.find_user(email, password)
        if data:
            messagebox.showinfo('Welcome', f'{data[0]} {data[1]}, welcome!')
            clear()
        else:
            messagebox.showerror('Error', 'Invalid email or password.')
        

def clear():
    ent_fname.delete(0, END)
    ent_lname.delete(0, END)
    ent_email.delete(0, END)
    ent_password.delete(0, END)
    ent_fname.focus_set()

#=======widget===========
'''label'''
lbl_fname = Label(win, text='Fname', font='cambria 16 bold', bg='#00ff00')
lbl_fname.place(x=120,y=20)

lbl_lname = Label(win, text='Lname', font='cambria 16 bold', bg='#00ff00')
lbl_lname.place(x=120,y=60)

lbl_email = Label(win, text='Email', font='cambria 16 bold', bg='#00ff00')
lbl_email.place(x=120,y=100)

lbl_password = Label(win, text='Password', font='cambria 16 bold', bg='#00ff00')
lbl_password.place(x=90,y=140)

lbl_star1 = Label(win, text='*', font='cambria 16 bold', bg='#00ff00', fg='red')
lbl_star1.place(x=100,y=100)

lbl_star2 = Label(win, text='*', font='cambria 16 bold', bg='#00ff00', fg='red')
lbl_star2.place(x=70,y=140)

'''entry'''
ent_fname = Entry(win, font='cambria 14 bold', bg='#ffccff', width=16)
ent_fname.place(x=200,y=20)

ent_lname = Entry(win, font='cambria 14 bold', bg='#ffccff', width=16)
ent_lname.place(x=200,y=60)
ent_email = Entry(win, font='cambria 14 bold', bg='#ffccff', width=16)
ent_email.place(x=200,y=100)
ent_password = Entry(win, font='cambria 14 bold', bg='#ffccff', width=16)
ent_password.place(x=200,y=140)

'''button'''
btn_sign_up = Button(win, text='sign up', font='cambria 14 bold', bg='#ffccff', width=11, command=sign_up)
btn_sign_up.place(x=130,y=190)

btn_sign_in = Button(win, text='sign in', font='cambria 14 bold', bg='#ffccff', width=11, command=sign_in)
btn_sign_in.place(x=280,y=190)
win.mainloop()
