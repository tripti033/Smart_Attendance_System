from tkinter import*
from tkinter import ttk
from tkinter import messagebox
# loading Python Imaging Library
from PIL import ImageTk, Image
from tkinter import Label
from tkinter import Button
from tkinter import Frame
from tkinter import Entry
from tkinter import LabelFrame

import cv2 
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root      #initiazing root
        self.root.geometry("1530x638+0+0")           #size of window
        self.root.title("face Recogniton System")
        
        #============================variables====================================
        self.var_atten_id=StringVar()
        self.var_atten_roll = StringVar ( )
        self.var_atten_name = StringVar ( )
        self.var_atten_dep = StringVar ( )
        self.var_atten_time = StringVar ( )
        self.var_atten_date = StringVar ( )
        self.var_atten_attendance = StringVar ( )
                
        
        #first img
        img=Image.open('group-college-students-28690355.jpg')
        # Resize the image using resize() method
        img = img.resize((800,150))
        self.photoimg=ImageTk.PhotoImage(img) 
        f_lbl=Label(self.root , image = self.photoimg)
        f_lbl.place(x = 0 , y = 0 , width = 600 , height =150)
        
        
        #second img
        img1=Image.open('e628f03e345087d1ebea46719c31db06.png')
        # Resize the image using resize() method
        img1 = img1.resize((800,150))
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root , image = self.photoimg1)
        f_lbl.place(x =600, y = 0 , width = 800 , height =150)
        
        #bg img
        img3=Image.open('bg2.webp')  
        img3 = img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)       
        bg_img=Label( self.root , image = self.photoimg3 )
        bg_img.place( x =0, y = 150 , width = 1530 , height =710 )        
        title_lbl=Label(bg_img,text="ATTENDANCE MANAGMENT SYSTEM                                  ", font=('Times New Roman',27,'bold'),bg='white',fg='red')
        title_lbl.place(x=0,y=0,width=1530,height=45)       
        main_frame=Frame(bg_img,bd=2,bg='white')
        main_frame.place(x=7,y=53,width=1259,height=435)
        
        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text="Student's Information",font=('Times New Roman',12,'bold'))
        left_frame.place(x=10,y=2,width=650,height=429 )    
        img_left=Image.open('attan.jpg')
        img_left = img_left.resize((700,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label( left_frame, image = self.photoimg_left )
        f_lbl.place( x =5, y = 0 , width = 630 , height =90 )
        inner_frame=Frame(left_frame,bd=2,bg='white',relief=RIDGE)
        inner_frame.place(x=5,y=100,width=635,height=300)
        
        #S_NO
        SNo_label=Label(inner_frame,text="SNo:",font=('Times New Roman',12,'bold'),bg='white')
        SNo_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)  
        studentid_entry=ttk.Entry(inner_frame,textvariable=self.var_atten_id,width=15,font=('Times New Roman',13,'bold'))
        studentid_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        
        #roll_NO
        roll_label=Label(inner_frame,text="Roll Number:",font=('Times New Roman',12,'bold'),bg='white')
        roll_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)  
        roll_entry=ttk.Entry(inner_frame,textvariable=self.var_atten_roll,width=15,font=('Times New Roman',13,'bold'))
        roll_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)
        
        #name
        name_label=Label(inner_frame,text="Name:",font=('Times New Roman',12,'bold'),bg='white')
        name_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)
        name_entry=ttk.Entry(inner_frame,textvariable=self.var_atten_name,width=15,font=('Times New Roman',13,'bold'))
        name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        
        #department
        dep_label=Label(inner_frame,text="Department:",font=('Times New Roman',12,'bold'),bg='white')
        dep_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)
        dep_entry=ttk.Entry(inner_frame,textvariable=self.var_atten_dep,width=15,font=('Times New Roman',13,'bold'))
        dep_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)
        
        #time
        time_label=Label(inner_frame,text="Time:",font=('Times New Roman',12,'bold'),bg='white')
        time_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)
        time_entry=ttk.Entry(inner_frame,textvariable=self.var_atten_time,width=15,font=('Times New Roman',13,'bold'))
        time_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)
        
        #date
        date_label=Label(inner_frame,text="Date:",font=('Times New Roman',12,'bold'),bg='white')
        date_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)
        date_entry=ttk.Entry(inner_frame,textvariable=self.var_atten_date,width=15,font=('Times New Roman',13,'bold'))
        date_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)
        
        
        #attendance status
        attendance_label=Label(inner_frame,text="Attendance Status",font=('Times New Roman',11,'bold'),bg='white')
        attendance_label.grid(row=3,column=0,padx=10,sticky=W)
        attendance_combo=ttk.Combobox(inner_frame,textvariable=self.var_atten_attendance,font=('Times New Roman',11,'bold'),width=17,state="read only")
        attendance_combo["values"]=("Absent","Present")
        attendance_combo.current(0)   #current value ka index
        attendance_combo.grid(row=3,column=1,padx=2,pady=10,sticky=W)
        
        
        #button frame
        btn_frame=Frame(left_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=7,y=290,width=630,height=40)
        
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=('Times New Roman',12,'bold'),bg='blue',fg='white')
        save_btn.grid(row=0,column=0)
        
        delete_btn=Button(btn_frame,text="Export csv",command=self.exportcsv,width=15,font=('Times New Roman',12,'bold'),bg='blue',fg='white')
        delete_btn.grid(row=0,column=2)
        
        update_btn=Button(btn_frame,text="Update",width=17,font=('Times New Roman',12,'bold'),bg='blue',fg='white')
        update_btn.grid(row=0,column=1)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=('Times New Roman',12,'bold'),bg='blue',fg='white')
        reset_btn.grid(row=0,column=3)
        
        
        
        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text="student detail's",font=('Times New Roman',12,'bold'))
        right_frame.place(x=670,y=2,width=570,height=429)
        
        inner1_frame=Frame(right_frame,bd=2,bg='white',relief=RIDGE)
        inner1_frame.place(x=5,y=5,width=555,height=400)
        
        
        #==================that scroll thing=================================
        scroll_x= ttk.Scrollbar( inner1_frame , orient = HORIZONTAL )
        scroll_y= ttk.Scrollbar( inner1_frame , orient = VERTICAL )
        
        self.student_table = ttk.Treeview(inner1_frame,columns=("Student_ID","Roll no","Name","Department","Time","Date","Attendance Status" ),xscrollcommand = scroll_x.set , yscrollcommand = scroll_y.set)
        scroll_x.pack ( side = BOTTOM , fill = X )
        scroll_y.pack ( side = RIGHT , fill = Y ) 
        scroll_x.config ( command = self.student_table.xview ) 
        scroll_y.config ( command = self.student_table.yview ) 
        self.student_table.heading ( "Student_ID" , text = "Student_ID" )
        self.student_table.heading ( "Roll no" , text = "Roll no" )
        self.student_table.heading ( "Name" , text = "Name" )
        self.student_table.heading ( "Department" , text = "Semester" )
        self.student_table.heading ( "Time" , text = "Time" )
        self.student_table.heading ( "Date" , text = "Date" )
        self.student_table.heading ( "Attendance Status" , text = "Attendance Status" )
        self.student_table [ "show" ] = "headings"
        
        self.student_table.column ( "Student_ID" , width = 100)
        self.student_table.column ( "Roll no" , width = 100)
        self.student_table.column ( "Name" , width = 100)
        self.student_table.column ( "Department" , width = 100)
        self.student_table.column ( "Time" , width = 100)
        self.student_table.column ( "Date" , width = 100)
        self.student_table.column ( "Attendance Status" , width = 150)       
        self.student_table.pack ( fill = BOTH , expand = 1 )
        self.student_table.bind("<ButtonRelease>",self.get_cusor)
        
        
    #==============================fetch data==============================================
   
   
    def fetchdata(self,rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("",END,values=i)
   
   
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)
            
    
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("NO DATA","No Data Found To Export", parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerows(i)
                messagebox.showinfo('Data Exported','Your data exported to'+os.path.basename(fln)+"successfully")                                
        except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root) 
    #================get cursor==========================================
    def get_cusor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content["values"]

        self.var_atten_id.set(data[0]),
        self.var_atten_roll.set(data[1]),
        self.var_atten_name.set(data[2]),
        self.var_atten_dep.set(data[3]),
        self.var_atten_time.set(data[4]),
        self.var_atten_date.set(data[5]),
        self.var_atten_attendance.set(data[6])
    
    def reset_data(self):
        self.var_atten_id.set(""),
        self.var_atten_roll.set(""),
        self.var_atten_name.set(""),
        self.var_atten_dep.set(""),
        self.var_atten_time.set(""),
        self.var_atten_date.set(""),
        self.var_atten_attendance.set("") 
    
#====================update func========================       

if __name__== "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()