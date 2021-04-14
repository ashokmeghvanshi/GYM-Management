#importing libraries
from tkinter import*
import tkinter as tk 
from tkinter import ttk 
import tkinter.messagebox
from PIL import ImageTk ,Image
import sqlite3

#Class GYM1
class GYM1(): 

    def __init__(self, top):
        self.mOffsets = Toplevel(top) # Toplevel is used to represent pop up window
        self.mOffsets.geometry("1400x900+0+0") # defining dimensions of window
        self.mOffsets.title("Project Gym Management")
        self.mOffsets.configure(bg='light grey') #used to change the color, also config

        def exit1():
            
            tkinter.messagebox.showinfo('Message','Do you want to go HOME') # showing message box
            answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

            if answer == 'yes':
                root.destroy()

        lblInfo=Label(self.mOffsets,font=('bold italic ',50),text="Login Page",fg="black",bg="peach puff",bd=10,anchor='w') # label used to print text in GUI
        lblInfo.place(x=525,y= 40)

        lblInfo1=Label(self.mOffsets,font=('arial',40),text="Username:",fg="black",bg="lavender",bd=10,anchor='w') #anchor is used as a relative positioning i.e E,W,NW etc
        lblInfo1.place(x=50,y=308)

        lblInfo2=Label(self.mOffsets,font=('arial',40),text="Password:",fg="black",bg="lavender",bd=10,anchor='w')
        lblInfo2.place(x=50,y=408)

        #========================= Data fetch from user===============================================================
    

        entry1=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=LoginName,bd=10,insertwidth=8,bg="white",justify='left')
        entry1.place(x=420,y=320)

        entry2=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=LoginPass,bd=10,insertwidth=8,bg="white",justify='left')
        entry2.place(x=420,y=420)

        #========================Button==================================
        button1 = Button(self.mOffsets,font=('bold italic',20),text="Login",bg="white",fg="black",height=1,width=10,command=UserLogin)
        button1.place(x=625,y=500)

        button2 = Button(self.mOffsets,font=('bold italic',20),text="HOME",bg="yellow2",fg="blue",height=1,width=10,command = CALL4) # command use for calling exit function
        button2.place(x=1200,y=700)

        
#==============================================Registration Form=====================================================    
#class GYM2      
class GYM2():

    def __init__(self, top):
        self.mOffsets = Toplevel(top)  # Toplevel is used to represent pop up window
        self.mOffsets.geometry("1400x900+0+0")# defining dimensions of window
        self.mOffsets.title("Project Gym Management")
        self.mOffsets.configure(bg='light grey')#used to change the color, also config


        def exit1():
                
                tkinter.messagebox.showinfo('window Title','Do you want to close')# showing message box
                answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

                if answer == 'yes':
                    root.destroy()
                    
        lblInfo=Label(self.mOffsets,font=('bold italic ',50),text="GYM MANAGEMENT SYSTEM",fg="black",bg="purple1",bd=10,anchor='w')# label used to print text in GUI
        lblInfo.place(x=320,y=20)

        lblInfo=Label(self.mOffsets,font=('bold italic ',40),text="REGISTRATION FORM",fg="black",bg="cyan3",bd=10,anchor='w')#anchor is used as a relative positioning i.e E,W,NW etc
        lblInfo.place(x=400,y=150)

        lblInfo1=Label(self.mOffsets,font=('arial',40),text="Name :",fg="black",bg='lavender',bd=10,anchor='w')
        lblInfo1.place(x=50,y=308)

        lblInfo2=Label(self.mOffsets,font=('arial',40),text="Password  :",fg="black",bg="lavender",bd=10,anchor='w')
        lblInfo2.place(x=50,y=408)

        lblInfo3=Label(self.mOffsets,font=('arial',40),text="E-mail  :",fg="black",bg="lavender",bd=10,anchor='w')
        lblInfo3.place(x=50,y=508)

        lblInfo4=Label(self.mOffsets,font=('arial',40),text="Contact No     :",fg="black",bg="lavender",bd=10,anchor='w')
        lblInfo4.place(x=50,y=608)

        #========================= BUTTON ===================================================================

        entry1=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Name1,bd=10,insertwidth=8,bg="white",justify='left')# justify for positioning left or right
        entry1.place(x=420,y=320)

        entry2=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Pass1,bd=10,insertwidth=8,bg="white",justify='left')
        entry2.place(x=420,y=420)

        entry3=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Email1,bd=10,insertwidth=8,bg="white",justify='left')
        entry3.place(x=420,y=520)

        entry4=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Cont1,bd=10,insertwidth=8,bg="white",justify='left')
        entry4.place(x=420,y=620)

        button1 = Button(self.mOffsets,font=('bold italic',20),text="Submit",bg="white",fg="blue",height=1,width=20,command=Insert)
        button1.place(x=1005,y=500)


        button2 = Button(self.mOffsets,font=('bold italic',20),text="No",bg="white",fg="blue",height=1,width=20,command = CALL4)
        button2.place(x=1005,y=600)

        button3 = Button(self.mOffsets,font=('bold italic',20),text="HOME",bg="yellow2",fg="blue",height=1,width=10,command = CALL4) # command use for calling exit function
        button3.place(x=1200,y=700)


#Class GYM3
class GYM3(): 

    def __init__(self, top):
        self.mOffsets = Toplevel(top) # Toplevel is used to represent pop up window
        self.mOffsets.geometry("1400x900+0+0") # defining dimensions of window
        self.mOffsets.title("Project Gym Management")
        self.mOffsets.configure(bg='light grey') #used to change the color, also config
                
        def exit1():#exit1 function
            
            tkinter.messagebox.showinfo('window Title','Do you want to close') # showing information
            answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

            if answer == 'yes':
                root.destroy()# it is used to close the window or GUI

        lblInfo=Label(self.mOffsets,font=('bold italic ',50),text="Welcome to the GYM page",fg="black",bg="lavender",bd=10,anchor='w')
        lblInfo.place(x=320,y=20)

        lblInfo=Label(self.mOffsets,font=('italic ',15),text="(Building Confidence Building Fitness).",fg="black",bg="lavender",bd=10,anchor='w')
        lblInfo.place(x=550,y=100)


        #Menu
        variable = StringVar(self.mOffsets)# variable object declaration
        variable.set("EXERCISES") # default value , opening text of menu

        w = OptionMenu(self.mOffsets, variable, "Pushups", "Squats", "DeadLifts","Planks")
        w.config(bg = 'SeaGreen1', height = 3, width = 20)
        w.pack()# used to do the element positioning in GUI, GEOMETRY MANAGER
        w.place(x=150,y=200)

        #Menu 2
        variable = StringVar(self.mOffsets)#variable object declaration
        variable.set("Packs") # default value, opening text of menu

        w = OptionMenu(self.mOffsets, variable, "600 PER MONTH", "6,000 FOR 6 MONTHS", "12,000 A YEAR","PERSONAL TRAINEE 2500 PM")
        w.config(bg = 'Yellow', height = 3, width = 20)
        w.pack()# used to do the element positioning in GUI, GEOMETRY MANAGER
        w.place(x=600,y=200)

        #Menu 3

        variable = StringVar(self.mOffsets)# variable object declaration
        variable.set("TIME-SLOTS") # default value, opening text of menu

        w = OptionMenu(self.mOffsets, variable, "8AM-11AM", "12PM TO 3PM", "5PM TO 8PM")
        w.config(bg = 'light blue', height = 3, width = 20)
        w.pack()# used to do the element positioning in GUI, GEOMETRY MANAGER
        w.place(x=1100,y=200)

        canvas = tkinter.Canvas(self.mOffsets, width = 500,height = 250)
        img=ImageTk.PhotoImage(Image.open ("C:/Users/ashok/Documents/New folder/gym1.jpg"))# inserting photo
        #lab=Label(self.mOffsets,image=img)# plotting the text in GUI
        #lab.config(height = 470, width = 1100)
        #lab.pack()
        canvas.create_image(135, 20, anchor = NW,image = img)
        canvas.pack()
        canvas.place(x=70,y=290)


        button1 = Button(self.mOffsets,font=('bold italic',20),text="Logout",bg="white",fg="blue",height=1,width=10,command = CALL4)
        button1.place(x=1200,y=400)

        button2 = Button(self.mOffsets,font=('bold italic',20),text="EXIT",bg="white",fg="blue",height=1,width=10,command = exit1)
        button2.place(x=1200,y=700)

#Class GYM3
class GYM4(): 

    def __init__(self, top):
        self.mOffsets = Toplevel(top) # Toplevel is used to represent pop up window
        self.mOffsets.geometry("1400x900+0+0") # defining dimensions of window
        self.mOffsets.title("Project Gym Management")
        self.mOffsets.configure(bg='light grey') #used to change the color, also config
            
        def exit1():
            
            tkinter.messagebox.showinfo('window Title','Do you want to close')
            answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

            if answer == 'yes':
                root.destroy()

        lblInfo=Label(self.mOffsets,font=('bold italic ',50),text="Project Gym Management",fg="black",bg="peach puff",bd=10,anchor='w')
        lblInfo.place(x=400,y= 40)

        lblInfo1=Label(self.mOffsets,font=('arial',40),text="Exit User",fg="black",bg="lavender",bd=10,anchor='w')
        lblInfo1.place(x=400,y=308)

        lblInfo2=Label(self.mOffsets,font=('arial',40),text="New User",fg="black",bg="lavender",bd=10,anchor='w')
        lblInfo2.place(x=850,y=308)

        #========================= BUTTON ===================================================================

        button1 = Button(self.mOffsets,font=('bold italic',20),text="Sign In",bg="white",fg="black",height=1,width=10,command=CALL1)
        button1.place(x=430,y=500)

        button2 = Button(self.mOffsets,font=('bold italic',20),text="Sign Up",bg="white",fg="black",height=1,width=10,command=CALL2)
        button2.place(x=880,y=500)

        button3 = Button(self.mOffsets,font=('bold italic',20),text="EXIT",bg="white",fg="blue",height=1,width=10,command = exit1)
        button3.place(x=1270,y=720)


            
#===================================================function call===============================================
    
def CALL1():
    gym = GYM1(root) # creating gym object of class GYM1 AND passing object of tikinter class

def CALL2():
    gym = GYM2(root)# creating gym object of class GYM2 AND passing object of tikinter class

def CALL3():
    gym = GYM3(root)# creating gym object of class GYM2 AND passing object of tikinter class

def CALL4():
    gym = GYM4(root)
#==============================================================main menu=====================================   
root = Tk() # creating object of class tkinter
root.geometry("1400x900+0+0")
root.title("GYM Management System")
root.configure(bg='lavender')


#==========================================create table =========================================================
db=sqlite3.connect('GYM.db')#here we are creating database
cursor=db.cursor() # cursor is a object that execute sqlite querries
cursor.execute("CREATE TABLE IF NOT EXISTS GYMDATA(FirstName TEXT NOT NULL,Password TEXT NOT NULL,Email TEXT NOT NULL PRIMARY KEY,Contact TEXT NOT NULL)")
db.commit()#closing the transaction in database, no further processing after this

#========================================insert data in table ==========================================================

Name1=StringVar()# creating Name1 variable
Pass1=StringVar()# creating Pass1 variable
Email1=StringVar()# creating Email1 variable
Cont1=StringVar()# creating Cont1 variable

def Insert():

  Name2=Name1.get()# data is getting fetched by get() function
  Pass2=Pass1.get()
  Email2=Email1.get()
  Contact2=Cont1.get()
  
  ins=sqlite3.connect('GYM.db')
          
  if Name2=='' or Pass2=='' or Email2=='' or Contact2=='':
      tkinter.messagebox.askretrycancel("Error Message", "Please Complete The Registration Form And Try again?")
      CALL2()
  else:
      with ins:
          cursor=ins.cursor()
          cursor.execute('INSERT INTO GYMDATA(FirstName,Password,Email,Contact) VALUES(?,?,?,?)',( Name2,Pass2,Email2,Contact2))
          db.close()#close play same role as commit
          tkinter.messagebox.showinfo("New Message", "You are Successfull Complete The Registration Press OK") 
          CALL4()
  
#============================================user login check======================================================
LoginName=StringVar()# creating Name1 variable
LoginPass=StringVar()# creating Pass1 variable

def UserLogin():

  NL=LoginName.get()# data is getting fetched by get() function
  LP=LoginPass.get()
  ins=sqlite3.connect('GYM.db')
  if NL=='' or LP=='':
      tkinter.messagebox.askretrycancel("Error Message", "Please Enter Username And Password And Try again?")
      CALL1()
  else:
      with ins:
          cursor=ins.cursor()
          cursor.execute('SELECT * FROM GYMDATA WHERE Email=? AND Password=?',(NL,LP))
          data=cursor.fetchall()
          if len(data)!=0:
              CALL3()
          else:
              #tkinter.messagebox.showinfo('window Title','Invalid Username And Password')# showing message box
              #answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')
              #if answer == 'yes':
              #    root.destroy()
              tkinter.messagebox.askretrycancel("Error Message", "Invalid Username And Password And Try again?")
              CALL1()
          db.close()
          #close play same role as commit
#===================================main menu ====================================================================

def exit1():
        
    tkinter.messagebox.showinfo('window Title','Do you want to close')
    answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

    if answer == 'yes':
        root.destroy()

lblInfo=Label(root,font=('bold italic ',50),text="Project Gym Management",fg="black",bg="peach puff",bd=10,anchor='w')
lblInfo.place(x=400,y= 40)

lblInfo1=Label(root,font=('arial',40),text="Please Click on Enter Button Below",fg="black",bg="lavender",bd=10,anchor='w')
lblInfo1.place(x=400,y=308)
#========================= BUTTON ===================================================================

button1 = Button(root,font=('bold italic',20),text="<== Enter ==>",bg="white",fg="black",height=1,width=15,command=CALL4)
button1.place(x=430,y=500)

button2 = Button(root,font=('bold italic',20),text="EXIT",bg="white",fg="blue",height=1,width=10,command = exit1)
button2.place(x=1270,y=720)



root.mainloop()#Closing GUI 
