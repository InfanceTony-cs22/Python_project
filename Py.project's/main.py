from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        # first image
        img1=Image.open(r"C:\Users\Infance Tony\Desktop\Py.project's\clg2.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1) 

        # f_lbl=frame label
        f_lbl=Label(self.root,image=self.photoimg1) 
        f_lbl.place(x=0,y=0,width=500,height=130)  

        # second image
        img2=Image.open(r"C:\Users\Infance Tony\Desktop\Py.project's\clg.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2) 

        # f_lbl=frame label
        f_lbl=Label(self.root,image=self.photoimg2) 
        f_lbl.place(x=500,y=0,width=500,height=130)   

        # third image
        img3=Image.open(r"C:\Users\Infance Tony\Desktop\Py.project's\clg3.jpg")
        img3=img3.resize((500,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3) 

        # f_lbl=frame label
        f_lbl=Label(self.root,image=self.photoimg3) 
        f_lbl.place(x=1000,y=0,width=550,height=130) 

         # background image
        img4=Image.open(r"C:\Users\Infance Tony\Desktop\Py.project's\bg.jpg")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4) 

        # f_lbl=frame label
        bg_img=Label(self.root,image=self.photoimg4) 
        bg_img.place(x=0,y=130,width=550,height=710) 


        #title label

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)   

        # student button
        img5=Image.open(r"C:\Users\Infance Tony\Desktop\Py.project's\r.jpeg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5) 

        # button
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)  

        b1_1=Button(bg_img,text="Student Detail's",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=200,width=220,height=110) 

        # detect face button
        img6=Image.open(r"C:\Users\Infance Tony\Desktop\Py.project's\clg.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6) 

        # button
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)  

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=200,width=220,height=110) 


         # Attendance face button
        img7=Image.open(r"C:\Users\Infance Tony\Desktop\Py.project's\clg.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7) 

        # button
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)  

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=200,width=220,height=110) 


         # help face button
        img8=Image.open(r"C:\Users\Infance Tony\Desktop\Py.project's\clg.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8) 

        # button
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)  

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=200,width=220,height=110) 


        # train face button
        img9=Image.open(r"C:\Users\Infance Tony\Desktop\Py.project's\clg.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9) 

        # button
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)  

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=110) 


        # Developer face button
        img10=Image.open(r"C:\Users\Infance Tony\Desktop\Py.project's\clg.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10) 

        # button
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)  

        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=110)



        # exit face button
        img11=Image.open(r"C:\Users\Infance Tony\Desktop\Py.project's\clg.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11) 

        # button
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)  

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=110)  














if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()