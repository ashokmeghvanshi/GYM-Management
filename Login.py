from tkinter import*
import tkinter.messagebox

root = Tk()

root.geometry("1400x900+0+0")
root.title("Project Gym Management")
root.configure(bg='light grey')

def exit1():
    
    tkinter.messagebox.showinfo('window Title','Do you want to close')
    answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

    if answer == 'yes':
        root.destroy()

lblInfo=Label(root,font=('bold italic ',50),text="Login Page",fg="black",bg="peach puff",bd=10,anchor='w')
lblInfo.place(x=525,y= 40)

lblInfo1=Label(root,font=('arial',40),text="Username:",fg="black",bg="lavender",bd=10,anchor='w')
lblInfo1.place(x=50,y=308)

lblInfo2=Label(root,font=('arial',40),text="Password:",fg="black",bg="lavender",bd=10,anchor='w')
lblInfo2.place(x=50,y=408)

#========================= BUTTON ===================================================================

entry1=Entry(root,font=('arial',24,'bold'),bd=10,insertwidth=8,bg="white",justify='left')
entry1.place(x=420,y=320)

entry2=Entry(root,font=('arial',24,'bold'),bd=10,insertwidth=8,bg="white",justify='left')
entry2.place(x=420,y=420)

button1 = Button(root,font=('bold italic',20),text="Submit",bg="white",fg="black",height=1,width=10)
button1.place(x=625,y=500)


root.mainloop()
