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
import numpy as np
import mysql.connector
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self,root):
        self.root=root      #initiazing root
        self.root.geometry("1530x638+0+0")           #size of window
        self.root.title("face Recogniton System")
       
        title_lbl=Label(self.root,text="FACE RECOGNITION      ", font=('Times New Roman',45,'bold'),bg='white',fg='red')
        title_lbl.place(x=0,y=0,width=1530,height=45) 
        b2=Button ( title_lbl ,text="EXIT",command=quit, cursor='heart', font=('Times New Roman',15,'bold'),bg='red',fg='white' )
        b2.place ( x = 1070 , y = 5 , width = 100 , height = 40 )
        img_top=Image.open('fc.jpg')
        img_top = img_top.resize((600,700))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label( self.root, image = self.photoimg_top )
        f_lbl.place( x =0, y = 55, width = 650 , height =700 )
        
        
        img_below=Image.open('re.jpg')
        # Resize the image using resize() method
        img_below = img_below.resize((600,700))
        self.photoimg_below=ImageTk.PhotoImage(img_below)
        f_lbl=Label( self.root, image = self.photoimg_below )
        f_lbl.place( x =650, y = 55, width = 650 , height =700 )
        
        b2=Button ( f_lbl ,text="FACE RECOGNITION ",command=self.face_recog, cursor='heart', font=('Times New Roman',14,'bold'),bg='dark blue',fg='white' )
        b2.place ( x = 300 , y = 500 , width = 200 , height = 40 )


#==============================attendence==========================================================

    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

                
#=============================face recognition=====================================================
    def face_recog(self):
        def  draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                conn=mysql.connector.connect(host='localhost',username="root",password="root",database="face_recognizer")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                
                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                
                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                
                
                if confidence>77:
                    cv2.putText(img,f"Student_ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll_Number:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown Face:",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,y]    

            return coord
                    
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap=cv2.VideoCapture(0)
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition ",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
      
        
        
if __name__== "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()