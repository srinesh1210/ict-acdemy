from tkinter import *

def submit():
    result.config(
    text=f"""
Name     : {name_entry.get()}
Roll No  : {roll_entry.get()}
Branch   : {branch_entry.get()}
Gender   : {gender.get()}
""")
    
root = Tk()
root.title("Student Registration Form")
root.geometry("400x350")
heading = Label(root,text="Student Registration Form",font=("Arial", 14, "bold"))
heading.pack(pady=10)
Label(root, text="Name").pack()
name_entry = Entry(root, width=30)
name_entry.pack()
Label(root, text="Roll No").pack()
roll_entry = Entry(root, width=30)
roll_entry.pack()
Label(root, text="Branch").pack()
branch_entry = Entry(root, width=30)
branch_entry.pack()
Label(root, text="Gender").pack()
gender = StringVar()
gender.set("male")
Radiobutton( root,text="Male",variable=gender,value="male").pack()
Radiobutton( root,text="Female",variable=gender,value="female").pack()
Button( root, text="Submit",command=submit).pack(pady=10)
result = Label(root,text="",fg ="black")
result.pack()
root.mainloop()
