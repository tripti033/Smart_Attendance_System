from email.mime import image
from time import strftime
from tkinter import*
import tkinter
from tkinter.ttk import *
# loading Python Imaging Library
from PIL import ImageTk, Image
from tkinter import Label
from tkinter import Button
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from chatbot import ChatBot
import pyttsx3
from developer_data import developer


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
class Face_Recognition_System:
    def __init__(self,root):
        
        self.root=root      #initiazing root
        self.root.geometry("1530x790+0+0")           #size of window
        self.root.title("face Recogniton System")
      
        #first img
        img=Image.open('new3.jpg')
        # Resize the image using resize() method
        img = img.resize((500,130))
        self.photoimg=ImageTk.PhotoImage(img) 
        f_lbl=Label( self.root , image = self.photoimg )
        f_lbl.place( x = 0 , y = 0 , width = 500 , height =130 )
        
        #second img
        img1=Image.open('new1.jpeg')
        # Resize the image using resize() method
        img1 = img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label( self.root , image = self.photoimg1 )
        f_lbl.place( x =500, y = 0 , width = 500 , height =130 )
        
        #third img
        img2=Image.open('new4.jpg')
        # Resize the image using resize() method
        img2 = img2.resize((500,130))
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label( self.root , image = self.photoimg2 )
        f_lbl.place( x =1000, y = 0 , width = 500 , height =130 )
     
     
        #bg img
        img3=Image.open('index.jpg')
        img3 = img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label( self.root , image = self.photoimg3 )
        bg_img.place( x =0, y = 130 , width = 1530 , height =710 )
       
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE       ", font=('Times New Roman',27,'bold'),bg='white',fg='red')
        title_lbl.place(x=0,y=0,width=1530,height=45)
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config( text= string )
            lbl.after( 1000 , time )
        lbl=Label(title_lbl,font=('Times New Roman',15,'bold'),bg='white',fg='red')
        lbl.place(x=0,y=0,width=110,height=45)
        time()
            
        
        #detect face button
        img5=Image.open('face.png')
        img5 = img5.resize((167,160))
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button ( bg_img , image = self.photoimg5, cursor='heart', command=self.face_data )
        b1.place ( x = 160 , y = 50 , width = 200 , height = 190 )
        b2=Button ( bg_img ,text="FACE DETECTOR", cursor='heart',command=self.face_data, font=('Times New Roman',15,'bold'),bg='dark blue',fg='white' )
        b2.place ( x = 160 , y = 240 , width = 200 , height = 40 )
        
        #attendance face button
        img6=Image.open('att.jpg')
        img6 = img6.resize((160,160))
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button ( bg_img , image = self.photoimg6, cursor='heart' )
        b1.place ( x = 470 , y = 50 , width = 200 , height = 190 )
        b2=Button ( bg_img ,text="ATTENDANCE",command=self.attendance_status, cursor='heart', font=('Times New Roman',15,'bold'),bg='dark blue',fg='white' )
        b2.place ( x = 470 , y = 240, width = 200 , height = 40 )

        #help button
        img7=Image.open('help.png')
        img7 = img7.resize((160,160))
        self.photoimg7=ImageTk.PhotoImage(img7)
        b1=Button ( bg_img , image = self.photoimg7, cursor='heart' ,command=self.help_desk)
        b1.place ( x = 750 , y = 50 , width = 200 , height = 190 )
        b2=Button ( bg_img ,text="HELP DESK",command=self.help_desk, cursor='heart', font=('Times New Roman',15,'bold'),bg='dark blue',fg='white' )
        b2.place ( x = 750 , y = 240, width = 200 , height = 40 )

        #student detail button
        img8=Image.open('student2.webp')
        img8 = img8.resize((160,160))
        self.photoimg8=ImageTk.PhotoImage(img8)
        b1=Button ( bg_img ,command=self.student_details, image = self.photoimg8, cursor='heart' )
        b1.place ( x = 1025 , y = 50 , width = 200 , height = 190 )
        b2=Button ( bg_img ,command=self.student_details,text="STUDENT'S DETAILS", cursor='heart', font=('Times New Roman',15,'bold'),bg='dark blue',fg='white' )
        b2.place ( x = 1025 , y = 240 , width = 200 , height = 40 )
        
        #train data button
        img9=Image.open('0x0.jpg')
        img9 = img9.resize((160,160))
        self.photoimg9=ImageTk.PhotoImage(img9)
        b1=Button ( bg_img , image = self.photoimg9, cursor='heart' ,command=self.train_data)
        b1.place ( x = 750 , y = 290 , width = 200 , height = 190 )
        b2=Button ( bg_img ,text="TRAIN DATA ",command=self.train_data, cursor='heart', font=('Times New Roman',15,'bold'),bg='dark blue',fg='white' )
        b2.place ( x = 750 , y = 480 , width = 200 , height = 40 )

        #photos button
        img10=Image.open('c95e631647c74855626aa71550958d06.jpg')
        img10 = img10.resize((160,160))
        self.photoimg10=ImageTk.PhotoImage(img10)
        b1=Button ( bg_img , image = self.photoimg10, cursor='heart',command=self.open_img )
        b1.place ( x = 1025 , y = 290 , width = 200 , height = 190 )
        b2=Button ( bg_img ,text="PHOTOS", cursor='heart',command=self.open_img, font=('Times New Roman',15,'bold'),bg='dark blue',fg='white' )
        b2.place ( x = 1025 , y = 480 , width = 200 , height = 40 )
        
         #developer button
        img11=Image.open('dev.jpg')
        img11 = img11.resize((160,160))
        self.photoimg11=ImageTk.PhotoImage(img11)
        b1=Button ( bg_img ,command=self.developer_status ,image = self.photoimg11, cursor='heart' )
        b1.place ( x = 470 , y = 290 , width = 200 , height = 190 )
        b2=Button ( bg_img ,text="DEVELOPER", command=self.developer_status ,cursor='heart', font=('Times New Roman',15,'bold'),bg='dark blue',fg='white' )
        b2.place ( x = 470 , y = 480 , width = 200 , height = 40 )
        
         #exit button
        img12=Image.open('ex.png')
        img12 = img12.resize((160,160))
        self.photoimg12=ImageTk.PhotoImage(img12)
        b1=Button ( bg_img , image = self.photoimg12,command=self.iExit, cursor='heart' )
        b1.place ( x = 160 , y = 290 , width = 200 , height = 190 )
        b2=Button ( bg_img ,text="EXIT",command=self.iExit, cursor='heart', font=('Times New Roman',15,'bold'),bg='dark blue',fg='white' )
        b2.place ( x = 160 , y = 480 , width = 200 , height = 40 )
         
#=======================photos function===================================================
    def open_img(self):
        speak("opening photos")
        os.startfile("data") 
       
    def student_details(self):
        speak("SHOWING STUDENT'S DETAILS!") 
        self.new_window=Toplevel( self.root )
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel( self.root )
        self.app=Train(self.new_window)
    def face_data(self):
        speak("OPENING FACE DETECTOR") 
        self.new_window=Toplevel( self.root )
        self.app=Face_Recognition(self.new_window)
        
    def attendance_status(self):
        speak("SHOWING ATTENDANCE STATUS") 
        self.new_window=Toplevel( self.root )
        self.app=Attendance(self.new_window)
        
    def help_desk(self):
        speak("OPENING HELP DESK!") 
        self.new_window=Toplevel( self.root )
        self.app=ChatBot(self.new_window)          
        
    def developer_status(self):
        speak("opening developer page") 
        self.new_window=Toplevel( self.root )
        self.app=developer(self.new_window)
    
    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno( " Face Recognition " , " Are you sure exit this project ",parent=self.root )
        if self.iExit > 0 :
           self.root.destroy()
        else :
           return   
if __name__== "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
    speak("THANKYOU!!")


