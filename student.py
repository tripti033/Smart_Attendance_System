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
import mysql.connector
import cv2

from train import speak 


class Student:
    def __init__(self,root):
        self.root=root      #initiazing root
        self.root.geometry("1530x638+0+0")           #size of window
        self.root.title("face Recogniton System")
        
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester =StringVar()
        self.va_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        
        
        #first img
        img=Image.open('group-college-students-28690355.jpg')
        # Resize the image using resize() method
        img = img.resize((500,100))
        self.photoimg=ImageTk.PhotoImage(img) 
        f_lbl=Label(self.root , image = self.photoimg)
        f_lbl.place(x = 0 , y = 0 , width = 500 , height =100)
        
        #second img
        img1=Image.open('e628f03e345087d1ebea46719c31db06.png')
        # Resize the image using resize() method
        img1 = img1.resize((500,100))
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x =500,y=0,width = 500 , height =100)
        
        #third img
        img2=Image.open('third.png')
        # Resize the image using resize() method
        img2 = img2.resize((500,100))
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root , image = self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=100)
        
        #bg img
        img3=Image.open('bg.png')
        img3 = img3.resize((1530,638))
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image = self.photoimg3)
        bg_img.place(x =0,y=100,width=1530,height=710)
       
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM        ", font=('Times New Roman',24,'bold'),bg='white',fg='red')
        title_lbl.place(x=0,y=0,width=1530,height=35)
        
        main_frame=Frame(bg_img,bd=2,bg='white')
        main_frame.place(x=5,y=45,width=1259,height=499)
        
        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text="student detail's",font=('Times New Roman',12,'bold'))
        left_frame.place(x=10,y=2,width=650,height=500)
        
        img_left=Image.open('student.webp')
        # Resize the image using resize() method
        img_left = img_left.resize((700,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(left_frame, image = self.photoimg_left)
        f_lbl.place(x =5, y = 0 , width = 630 , height =85)
        
        #current course information
        current_course_frame=LabelFrame(left_frame,bd=2,bg='white',relief=RIDGE,text="current course information",font=('Times New Roman',12,'bold'))
        current_course_frame.place(x=5,y=85,width=635,height=110)
        
        #department  
        dep_label=Label(current_course_frame,text="department",font=('Times New Roman',11,'bold'),bg='white')
        dep_label.grid(row=0,column=0,padx=10)
    
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=('Times New Roman',11,'bold'),width=17,state="read only")
        dep_combo["values"]=("select department","COE","IT","ECE","ECE-AI","MECHANICAL","CIVIL")
        dep_combo.current(0)   #curren value ka index
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
        
        
        #course
        course_label=Label(current_course_frame,text="course",font=('Times New Roman',11,'bold'),bg='white')
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=('Times New Roman',11,'bold'),width=17,state="read only")
        course_combo["values"]=("select course","FE","SE","TE","BE","LE","NE")
        course_combo.current(0)   #current value ka index
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #year
        year_label=Label(current_course_frame,text="year",font=('Times New Roman',11,'bold'),bg='white')
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=('Times New Roman',11,'bold'),width=17,state="read only")
        year_combo["values"]=("select year","1st","2nd","3rd","4th","5th","6th")
        year_combo.current(0)   #current value ka index
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        
        #semester
        semester_label=Label(current_course_frame,text="semester",font=('Times New Roman',11,'bold'),bg='white')
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=('Times New Roman',11,'bold'),width=17,state="read only")
        semester_combo["values"]=("select semester","1","2","3","4","5","6",'7','8')
        semester_combo.current(0)   #current value ka index
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #class student information
        class_student_frame=LabelFrame(left_frame,bd=2,bg='white',relief=RIDGE,text="class student information",font=('Times New Roman',11,'bold'))
        class_student_frame.place(x=5,y=195,width=635,height=280)
        
        #student id
        studentid_label=Label(class_student_frame,text="StudentID:",font=('Times New Roman',11,'bold'),bg='white')
        studentid_label.grid(row=0,column=0,padx=5,sticky=W)
        
        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.va_std_id,width=20,font=('Times New Roman',12,'bold'))
        studentid_entry.grid(row=0,column=1,padx=5,sticky=W)
        
        #student name
        studentname_label=Label(class_student_frame,text="Student Name:",font=('Times New Roman',11,'bold'),bg='white')
        studentname_label.grid(row=0,column=2,padx=5,sticky=W)
        
        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=('Times New Roman',12,'bold'))
        studentname_entry.grid(row=0,column=3,padx=5,sticky=W)
        
        #class division
        studentname_label=Label(class_student_frame,text="Class Division:",font=('Times New Roman',11,'bold'),bg='white')
        studentname_label.grid(row=1,column=0,padx=3,pady=5,sticky=W)
        
        #studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=('Times New Roman',12,'bold'))
        #studentname_entry.grid(row=1,column=1,padx=3,pady=5,sticky=W)
        
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=('Times New Roman',11,'bold'),width=17,state="read only")
        div_combo["values"]=("A","B","C")
        div_combo.current(0)   #current value ka index
        div_combo.grid(row=1,column=1,padx=3,pady=5,sticky=W)
        
        #rollno.
        roll_no_label=Label(class_student_frame,text="Roll Number:",font=('Times New Roman',11,'bold'),bg='white')
        roll_no_label.grid(row=1,column=2,padx=3,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=('Times New Roman',12,'bold'))
        roll_no_entry.grid(row=1,column=3,padx=3,pady=5,sticky=W)
        
        #gender
        gender_label=Label(class_student_frame,text="Gender:",font=('Times New Roman',11,'bold'),bg='white')
        gender_label.grid(row=2,column=0,padx=3,pady=5,sticky=W)
        
        #gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=('Times New Roman',12,'bold'))
        #gender_entry.grid(row=2,column=1,padx=3,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=('Times New Roman',11,'bold'),width=17,state="read only")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)   #current value ka index
        gender_combo.grid(row=2,column=1,padx=3,pady=5,sticky=W)
        
        #DOB
        dob_label=Label(class_student_frame,text="Date Of Birth:",font=('Times New Roman',11,'bold'),bg='white')
        dob_label.grid(row=2,column=2,padx=3,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=('Times New Roman',12,'bold'))
        dob_entry.grid(row=2,column=3,padx=3,pady=5,sticky=W)
        
        #email
        email_label=Label(class_student_frame,text="Email:",font=('Times New Roman',11,'bold'),bg='white')
        email_label.grid(row=3,column=0,padx=3,pady=5,sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=('Times New Roman',12,'bold'))
        email_entry.grid(row=3,column=1,padx=3,pady=5,sticky=W)
        
        #phone no
        phoneno_label=Label(class_student_frame,text="Phone Number:",font=('Times New Roman',11,'bold'),bg='white')
        phoneno_label.grid(row=3,column=2,padx=3,pady=5,sticky=W)
        
        phoneno_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=('Times New Roman',12,'bold'))
        phoneno_entry.grid(row=3,column=3,padx=3,pady=5,sticky=W)
        
        #address
        address_label=Label(class_student_frame,text="Address:",font=('Times New Roman',11,'bold'),bg='white')
        address_label.grid(row=4,column=0,padx=3,pady=5,sticky=W)
        
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=('Times New Roman',12,'bold'))
        address_entry.grid(row=4,column=1,padx=3,pady=5,sticky=W)
        
        #teachername
        teachername_label=Label(class_student_frame,text="Teacher's Name:",font=('Times New Roman',11,'bold'),bg='white')
        teachername_label.grid(row=4,column=2,padx=3,pady=5,sticky=W)
        
        teachername_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=('Times New Roman',12,'bold'))
        teachername_entry.grid(row=4,column=3,padx=3,pady=5,sticky=W)
        
        
        #radio buttons
        self.var_radio1= StringVar ()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take photo sample",value="yes")
        radiobtn1.grid(row=6,column=0)
        

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="no photo sample",value="no")
        radiobtn2.grid(row=6,column=1)
        
        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=7,y=190,width=615,height=39)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=('Times New Roman',12,'bold'),bg='blue',fg='white')
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=('Times New Roman',12,'bold'),bg='blue',fg='white')
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=('Times New Roman',12,'bold'),bg='blue',fg='white')
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=('Times New Roman',12,'bold'),bg='blue',fg='white')
        reset_btn.grid(row=0,column=3)
        
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame1.place(x=7,y=220,width=615,height=39)
        
        take_photo_btn=Button(btn_frame1,text="Take photo sample",command=self.generate_dataset,width=35,font=('Times New Roman',12,'bold'),bg='blue',fg='white')
        take_photo_btn.grid(row=0,column=0)
        
        update_photo_btn=Button(btn_frame1,text="Update photo sample",width=35,font=('Times New Roman',12,'bold'),bg='blue',fg='white')
        update_photo_btn.grid(row=0,column=1)
        
        
    
        
        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text="student detail's",font=('Times New Roman',12,'bold'))
        right_frame.place(x=680,y=2,width=570,height=580)
        
        img_right=Image.open('s2.webp')
        # Resize the image using resize() method
        img_right = img_right.resize((700,130))
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lbl=Label( right_frame, image = self.photoimg_right )
        f_lbl.place( x =5, y = 0 , width = 630 , height =85 )
        
        #============================search system======================
        
        search_frame=LabelFrame(right_frame,bd=2,bg='white',relief=RIDGE,text="search system",font=('Times New Roman',11,'bold'))
        search_frame.place(x=5,y=85,width=560,height=70)
        
        search_label=Label(search_frame,text="Search by:",font=('Times New Roman',13,'bold'),bg='pink')
        search_label.grid(row=0,column=0,padx=3,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=('Times New Roman',12,'bold'),width=13,state="read only")
        search_combo["values"]=("select ","roll no","phone no")
        search_combo.current(0)   #current value ka index
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
       
        search_entry=ttk.Entry(search_frame,width=15,font=('Times New Roman',12,'bold'))
        search_entry.grid(row=0,column=2,padx=3,pady=5,sticky=W) 
        
        search_btn=Button(search_frame,text="Search",width=9,font=('Times New Roman',12,'bold'),bg='blue',fg='white')
        search_btn.grid(row=0,column=3,padx=3,pady=5,sticky=W)
        
        showall_btn=Button(search_frame,text="Show All",width=9,font=('Times New Roman',12,'bold'),bg='blue',fg='white')
        showall_btn.grid(row=0,column=4,padx=3,pady=5,sticky=W)
        
        
        #===============================table frame======================================================
        table_frame=LabelFrame(right_frame,bd=2,bg='white',relief=RIDGE)
        table_frame.place(x=5,y=155,width=560,height=315)
        
        scroll_x= ttk.Scrollbar( table_frame , orient = HORIZONTAL )
        scroll_y= ttk.Scrollbar( table_frame , orient = VERTICAL )
        
        self.student_table = ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll no","gender","dob" ,"email" , "phone" , "address" , "teacher" , "photo" ),xscrollcommand = scroll_x.set , yscrollcommand = scroll_y.set)
        scroll_x.pack ( side = BOTTOM , fill = X )
        scroll_y.pack ( side = RIGHT , fill = Y ) 
        scroll_x.config ( command = self.student_table.xview )
        scroll_y.config ( command = self.student_table.yview )

        
        self.student_table.heading ( "dep" , text = "Department" )
        self.student_table.heading ( "course" , text = "Course" )
        self.student_table.heading ( "year" , text = "Year" )
        self.student_table.heading ( "sem" , text = "Semester" )
        self.student_table.heading ( "id" , text = "StudentId" )
        self.student_table.heading ( "name" , text = "Name" )
        self.student_table.heading ( "div" , text = "Division" )
        self.student_table.heading ( "roll no" , text = "Roll No" )
        self.student_table.heading ( "gender" , text = "Gender" )
        self.student_table.heading ( "dob" , text = "DOB" )
        self.student_table.heading ( "email" , text = "Email" )
        self.student_table.heading ( "phone" , text = "Phone" )
        self.student_table.heading ( "address" , text = "Address" )
        self.student_table.heading ( "teacher" , text = "Teacher" )
        self.student_table.heading ( "photo" , text = "Photo Sample Status" )
        self.student_table [ "show" ] = "headings"
        
        
        self.student_table.column ( "dep" , width = 100)
        self.student_table.column ( "course" , width = 100)
        self.student_table.column ( "year" , width = 100)
        self.student_table.column ( "sem" , width = 100)
        self.student_table.column ( "id" , width = 100)
        self.student_table.column ( "name" , width = 100)
        self.student_table.column ( "roll no" , width = 100)
        self.student_table.column ( "gender" , width = 100)
        self.student_table.column ( "div" , width = 100)
        self.student_table.column ( "dob" , width = 100)
        self.student_table.column ( "email" , width = 100)
        self.student_table.column ( "phone" , width = 100)
        self.student_table.column ( "address" , width = 100)
        self.student_table.column ( "teacher" , width = 100)
        self.student_table.column ( "photo" , width = 150)
        self.student_table.pack ( fill = BOTH , expand = 1 )
        self.student_table.bind("<ButtonRelease>",self.get_cusor)
        self.fetch_data()
        
    #====================function declaration==========================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="" :
            messagebox.showerror ( " Error " , " All Fields are required ", parent=self.root )
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username="root",password="root",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    
                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_semester.get(),
                                                                                            self.va_std_id.get(),
                                                                                            self.var_std_name.get(),
                                                                                            self.var_div.get(),
                                                                                            self.var_roll.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_teacher.get(),
                                                                                            self.var_radio1.get()
                                                                                                                                                       
                                                                                        
                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
                speak("DATA SAVED")
            except Exception as es:
                messagebox.showerror("error",f"Due To :{str(es)}",parent=self.root)
        
#================================================fetch data=============================================================================
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username="root",password="root",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
#================get cursor==========================================
    def get_cusor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    
#====================update func========================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="" :
            messagebox.showerror ( " Error " , " All Fields are required ", parent=self.root )
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update details?",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username="root",password="root",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                        
                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_semester.get(),
                                                                                        
                                                                                            self.var_std_name.get(),
                                                                                            self.var_div.get(),
                                                                                            self.var_roll.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_teacher.get(),
                                                                                            self.var_radio1.get(),
                                                                                            self.va_std_id.get()
                                    
                                      
                     ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details successfully updated!",parent=self.root)
                speak("data updated")  
                conn.commit()      
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
           
#========================delete function==================================
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete these details?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host='localhost',username="root",password="root",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully delete student details!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                
#========================reset function==================================
    def reset_data(self):
        self.var_dep.set("select department")  
        self.var_course.set("select course")
        self.var_year.set("select year")
        self.var_semester.set("select semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("select division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
#==============================generate dataset and take photo sample=================================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="" :
            messagebox.showerror ( " Error " , " All Fields are required ", parent=self.root )
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username="root",password="root",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                        
                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_semester.get(),
                                                                                        
                                                                                            self.var_std_name.get(),
                                                                                            self.var_div.get(),
                                                                                            self.var_roll.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_teacher.get(),
                                                                                            self.var_radio1.get(),
                                                                                            self.va_std_id.get()==id+1
                                    
                                      
                     ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                #=================load predefined data on face frontals from opencv=====================
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbor=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w,]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        #                                       ^font of text     ^color  ^thickness of text
                        cv2.imshow("cropped face",face)
                    if cv2.waitKey(1)==13 or int(img_id==100):
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!!")
                speak("Generating dataset completed!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)           


       
       


if __name__== "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()