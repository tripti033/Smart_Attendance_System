# Import
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import sqlite3
import os
from main import Face_Recognition_System

# FRAME

root = Tk()
root=root      #initiazing root
root.geometry("1530x790+0+0")           #size of window
root.title("face Recogniton System")


#==============================METHODS========================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("facedb.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")       
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'tripti' AND `password` = '1982'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, password) VALUES('tripti', '1982')")
        conn.commit()

label=Label(root)
label.pack()

# Login Page
def Login():
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            att()
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")   
    cursor.close()
    conn.close()



 
#==============================VARIABLES======================================
USERNAME = StringVar()
PASSWORD = StringVar()
 
#==============================FRAMES=========================================
#bg img
img3=Image.open('bl.jpg')
img3 = img3.resize((1530,710))
photoimg3=ImageTk.PhotoImage(img3)
        
bg_img=Label( root , image = photoimg3 )
bg_img.place( x =0, y = 130 , width = 1530 , height =710 )

Top = Frame(root, bd=10,  relief=RIDGE)
Top.pack(side=TOP, fill=X)

Form = Frame(root, height=40, bd=30,bg="light blue")
Form.place(x=450,y=200,width=400,height=300)

 
#==============================LABELS=========================================
lbl_title = Label(Top, text = "LOGIN PAGE", bg="light blue", fg="black", font=('Helvetica', 64))
lbl_title.pack(fill=BOTH,expand=1)

lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15,bg="light blue")
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text = "Password:", font=('arial', 14), bd=15,bg="light blue")
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)
 
#==============================ENTRY WIDGETS==================================
username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)
 
#==============================BUTTON WIDGETS=================================
btn_login = Button(Form, text="Login", width=45, command=Login,bg="#6bc8ed")
btn_login.grid(pady=25, row=3, columnspan=2)
btn_login.bind("<Return>", Login)

def att():
    
    new_window=Toplevel(root )
    app=Face_Recognition_System(new_window)



#==============================INITIALIATION==================================
# if __name__ == '__main__':
root.mainloop()






