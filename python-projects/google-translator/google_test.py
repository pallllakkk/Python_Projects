from tkinter import  *
from tkinter import ttk

root = Tk()
root.title("Translator")
root.geometry("500x1000")
root.config(bg = "Teal")

lab_txt = Label(root , text = "Translastor" , font = ("Time New Roman",40,"bold"), bg = "Teal")
lab_txt.place(x=100,y=50,height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)

Sor_txt = Text(frame, font=("Time New Roman",20,"bold"),wrap = WORD)
Sor_txt.place(x=10,y=120,height=200,width=480)

root.mainloop()