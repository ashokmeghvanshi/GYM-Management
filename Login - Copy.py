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

lblInfo=Label(root,font=('bold italic ',50),text="Project Gym Management",fg="black",bg="peach puff",bd=10,anchor='w')
lblInfo.place(x=400,y= 40)

lblInfo1=Label(root,font=('arial',40),text="Old User",fg="black",bg="lavender",bd=10,anchor='w')
lblInfo1.place(x=400,y=308)

lblInfo2=Label(root,font=('arial',40),text="New User",fg="black",bg="lavender",bd=10,anchor='w')
lblInfo2.place(x=850,y=308)

#========================= BUTTON ===================================================================

button1 = Button(root,font=('bold italic',20),text="Sign In",bg="white",fg="black",height=1,width=10)
button1.place(x=430,y=500)

button2 = Button(root,font=('bold italic',20),text="Sign Up",bg="white",fg="black",height=1,width=10)
button2.place(x=880,y=500)

root.mainloop()
