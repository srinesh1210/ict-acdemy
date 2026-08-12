from tkinter import *
def show_name():  #it is a function used to show name in terminal 
    name=entry.get()  #get function is used to acces the name in the box
    print(f"hello,{name}!")
root=Tk()  #it is a root tk form
root.title("srinesh")  #
Label1=Label(root,text="enter your name:")
label2=Label(root,text="enter you roll no:")
Label1.pack()
Label2.pack()

entry=Entry(root)
entry.pack()
button=Button(root,text="submit",command=show_name)
button.pack()
root.mainloop()
