from tkinter import *

root = Tk()
root.title("Login App")
root.geometry('400x400')

frame = Frame(master=root, height= 200, width=360, bg="#D9FADA")

lbl1 = Label(frame, text="Enter the length in inches", bg="#3C735F", fg="white", width=45)

length_entry= Entry(frame)

def display():
    length= int(length_entry.get())
    message= f"The length {length} inches in centimeters is {length * 2.54} \n"
    textbox.insert(END,message)
    
textbox= Text(bg="#BEBEBE", fg="black")
btn= Button(text="Convert", command=display, bg="#D9FADA")

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
length_entry.place(x=110, y=60)
btn.place(x=160, y=210)
textbox.place(y=250)

root.mainloop()