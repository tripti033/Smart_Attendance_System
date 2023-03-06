from tkinter import*
# loading Python Imaging Library
from PIL import ImageTk, Image
from tkinter import Label
from tkinter import Button
from tkinter import Frame
from tkinter import Entry
from tkinter import LabelFrame



class developer:
    def __init__(self,root):
        self.root=root      #initiazing root
        self.root.geometry("1530x638+0+0")           #size of window
        self.root.title("face Recogniton System")
        
        title_lbl=Label(self.root,text="DEVELOPER                          ", font=('Times New Roman',34,'bold'),bg='white',fg='red')
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        img_top=Image.open('dev.jpg')
        # Resize the image using resize() method
        img_top = img_top.resize((1530,720))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label( self.root, image = self.photoimg_top )
        f_lbl.place( x =0, y = 45, width = 1530 , height =720 )

        main_frame=Frame(f_lbl,bd=2,bg='white')
        main_frame.place(x=30,y=10,width=1200,height=550)
        
        img_top1=Image.open('302064546_474199514291450_5249937029090454900_n.jpg')
        # Resize the image using resize() method
        img_top1 = img_top1.resize((200,200))
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        f_lbl=Label( main_frame, image = self.photoimg_top1 )
        f_lbl.place( x =550, y = 0, width = 200 , height =200 )
        
        dep_label=Label(main_frame,text="hello my name is tripti",font=('Times New Roman',20,'bold'),bg='white')
        dep_label.place(x=0,y=5)
        dep_label1=Label(main_frame,text="From igdtuw",font=('Times New Roman',20,'bold'),bg='white')
        dep_label1.place(x=0,y=40)
        dep_label1=Label(main_frame,text=" A Frontend Developer and Ui Designer ,who ",font=('Times New Roman',20,'bold'),bg='white')
        dep_label1.place(x=0,y=80)
        
        dep_label1=Label(main_frame,text=" always ready for adapt and learn new things. ",font=('Times New Roman',20,'bold'),bg='white')
        dep_label1.place(x=0,y=115)
        
        
        dep_label1=Label(main_frame,text="I'm Frontend Developer and Ui Designer ,who always ready for adapt and learn new things.",font=('Times New Roman',20,'bold'),bg='white')
        dep_label1.place(x=0,y=200)
        dep_label1=Label(main_frame,text=" Currently in second year Btech ECE-AI from IGDTUW,Delhi. Programing languges that ,",font=('Times New Roman',20,'bold'),bg='white')
        dep_label1.place(x=0,y=235)
        dep_label1=Label(main_frame,text=" I know are Java,Python,C/C++,and Javascript focusing in solving real world problem .",font=('Times New Roman',20,'bold'),bg='white')
        dep_label1.place(x=0,y=270)
        


if __name__== "__main__":
    root = Tk()
    obj = developer(root)
    root.mainloop()