from tkinter import*
import tkinter.messagebox

root = Tk()

root.geometry("1400x900+0+0")
root.title("GYM Management System")
root.configure(bg='lavender')

def exit1():
    
    tkinter.messagebox.showinfo('window Title','Do you want to close')
    answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

    if answer == 'yes':
        root.destroy()

lblInfo=Label(root,font=('bold italic ',50),text="GYM MANAGEMENT SYSTEM",fg="black",bg="purple1",bd=10,anchor='w')
lblInfo.place(x=320,y=20)

lblInfo=Label(root,font=('bold italic ',40),text="REGISTRATION FORM",fg="black",bg="cyan3",bd=10,anchor='w')
lblInfo.place(x=400,y=150)

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

button1 = Button(root,font=('bold italic',20),text="Yes",bg="white",fg="blue",height=1,width=20)
button1.place(x=1005,y=500)


button2 = Button(root,font=('bold italic',20),text="No",bg="white",fg="blue",height=1,width=20,command = exit1)
button2.place(x=1005,y=600)


root.mainloop()
