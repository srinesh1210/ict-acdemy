from tkinter import *
root = Tk()
root.title("Traffic Light Simulation")
root.geometry("250x400")
canvas = Canvas(root, width=150, height=250, bg="white")
canvas.pack()

red_light = canvas.create_oval(40, 20, 110, 90, fill="grey")
yellow_light = canvas.create_oval(40, 100, 110, 170, fill="grey")
green_light = canvas.create_oval(40, 180, 110, 250, fill="grey")
def red_on():
    canvas.itemconfig(red_light, fill="red")  
    canvas.itemconfig(yellow_light, fill="grey")
    canvas.itemconfig(green_light, fill="grey")
def yellow_on():
    canvas.itemconfig(red_light, fill="grey")
    canvas.itemconfig(yellow_light, fill="yellow")
    canvas.itemconfig(green_light, fill="grey")
def green_on():
    canvas.itemconfig(red_light, fill="grey")
    canvas.itemconfig(yellow_light, fill="grey")
    canvas.itemconfig(green_light, fill="green")
Button(root, text="Red", width=10, command=red_on).pack(pady=10)
Button(root, text="Yellow", width=10, command=yellow_on).pack(pady=10)    
Button(root, text="Green", width=10, command=green_on).pack(pady=10)
root.mainloop()
