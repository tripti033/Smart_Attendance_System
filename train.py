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
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


class Train:
    def __init__(self,root):
        self.root=root      #initiazing root
        self.root.geometry("1530x638+0+0")           #size of window
        self.root.title("face Recogniton System")
        
        title_lbl=Label(self.root,text="TRAIN DATA SET                           ", font=('Times New Roman',34,'bold'),bg='white',fg='red')
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        img_top=Image.open('face_header_sd.jpg')
        # Resize the image using resize() method
        img_top = img_top.resize((1530,325))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label( self.root, image = self.photoimg_top )
        f_lbl.place( x =0, y = 45, width = 1530 , height =300 )
        
        
        img_below=Image.open('men.jpg')
        # Resize the image using resize() method
        img_below = img_below.resize((1530,325))
        self.photoimg_below=ImageTk.PhotoImage(img_below)
        f_lbl=Label( self.root, image = self.photoimg_below )
        f_lbl.place( x =0, y = 400, width = 1400 , height =250 )
        
        
        b2=Button ( self.root ,text="TRAIN DATA            ",command=self.train_classifier, cursor='heart', font=('Times New Roman',35,'bold'),bg='dark blue',fg='white' )
        b2.place ( x = 0 , y = 350 , width = 1530 , height = 65 )
        
    def train_classifier(self):
        speak("training the data!") 
        data_dir=("data")    
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #gear scale image
            imagenp=np.array(img,"uint8")    #uint8=datatype
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imagenp)
            ids.append(id)

            cv2.imshow("Training",imagenp)
            cv2.waitKey(1)==13
        ids=np.array(ids)  
        speak("data trained mam!")   
        
        #==========================train classifier and save=========================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data set completed!!")







if __name__== "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()