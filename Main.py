from tkinter import*
import tkinter as tk 
from tkinter import ttk 
import tkinter.messagebox
from PIL import ImageTk ,Image

root = Tk()

root.geometry("1400x900+0+0")
root.title("GYM Management System")
root.configure(bg='lavender')

def exit1():
    
    tkinter.messagebox.showinfo('window Title','Do you want to close')
    answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

    if answer == 'yes':
        root.destroy()

lblInfo=Label(root,font=('bold italic ',50),text="Welcome to the GYM page",fg="black",bg="lavender",bd=10,anchor='w')
lblInfo.place(x=320,y=20)

lblInfo=Label(root,font=('italic ',15),text="(Building Confidence Building Fitness).",fg="black",bg="lavender",bd=10,anchor='w')
lblInfo.place(x=550,y=100)




#Menu
variable = StringVar(root)
variable.set("EXERCISES") # default value

w = OptionMenu(root, variable, "Pushups", "Squats", "DeadLifts","Planks")
w.config(bg = 'SeaGreen1', height = 3, width = 20)
w.pack()
w.place(x=150,y=200)

#Menu 2
variable = StringVar(root)
variable.set("Packs") # default value

w = OptionMenu(root, variable, "600 PER MONTH", "6,000 FOR 6 MONTHS", "12,000 A YEAR","PERSONAL TRAINEE 2500 PM")
w.config(bg = 'Yellow', height = 3, width = 20)
w.pack()
w.place(x=600,y=200)

#Menu 3

variable = StringVar(root)
variable.set("TIME-SLOTS") # default value

w = OptionMenu(root, variable, "8AM-11AM", "12PM TO 3PM", "5PM TO 8PM")
w.config(bg = 'light blue', height = 3, width = 20)
w.pack()
w.place(x=1100,y=200)

img=ImageTk.PhotoImage(Image.open ("C://Users//ashok//Documents//New folder//gym1.jpg"))
lab=Label(image=img)
lab.pack()

#img=ImageTk.PhotoImage(Image.open ("C://Users//ashok//Documents//New folder//gym1.jpg"))

#lab=Label(image=img)
#lab.config(height = 470, width = 1100)
#lab.pack()
lab.place(x=70,y=290)


'''
lblInfo1=Label(root,font=('arial',40),text="Name :",fg="black",bg='lavender',bd=10,anchor='w')
lblInfo1.place(x=50,y=308)

lblInfo2=Label(root,font=('arial',40),text="Password  :",fg="black",bg="lavender",bd=10,anchor='w')
lblInfo2.place(x=50,y=408)

lblInfo3=Label(root,font=('arial',40),text="E-mail  :",fg="black",bg="lavender",bd=10,anchor='w')
lblInfo3.place(x=50,y=508)

lblInfo4=Label(root,font=('arial',40),text="Contact No     :",fg="black",bg="lavender",bd=10,anchor='w')
lblInfo4.place(x=50,y=608)

#========================= BUTTON ===================================================================

entry1=Entry(root,font=('arial',24,'bold'),bd=10,insertwidth=8,bg="white",justify='left')
entry1.place(x=420,y=320)

entry2=Entry(root,font=('arial',24,'bold'),bd=10,insertwidth=8,bg="white",justify='left')
entry2.place(x=420,y=420)

entry3=Entry(root,font=('arial',24,'bold'),bd=10,insertwidth=8,bg="white",justify='left')
entry3.place(x=420,y=520)

entry4=Entry(root,font=('arial',24,'bold'),bd=10,insertwidth=8,bg="white",justify='left')
entry4.place(x=420,y=620)
'''


button2 = Button(root,font=('bold italic',20),text="Sing In",bg="white",fg="blue",height=1,width=10)
button2.place(x=1200,y=400)

button2 = Button(root,font=('bold italic',20),text="Sign Up",bg="white",fg="blue",height=1,width=10)
button2.place(x=1200,y=550)

button2 = Button(root,font=('bold italic',20),text="EXIT",bg="white",fg="blue",height=1,width=10,command = exit1)
button2.place(x=1200,y=700)


root.mainloop()
