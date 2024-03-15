from tkinter import *

def toBox2():
    select = list(box1.curselection())
    select.reverse()
    for i in select:
        box2.insert(END, box1.get(i))
        box1.delete(i)
    n = box2.size()
    lab2.config(text = str(n))
def toBox1():
    select = list(box2.curselection())
    select.reverse()
    for i in select:
        box1.insert(END, box2.get(i))
        box2.delete(i)
    n = box2.size()
    lab2.config(text = str(n))


root = Tk()
root.title("Покупки")
root.geometry("370x170")



box1 = Listbox(selectmode = EXTENDED)
box1.grid(row = 0, column = 0, rowspan = 6, padx = 5)

products = ["КАВА", "ЧАЙ", "СОК", "ВОДА", "ПЕПСІ", "КОЛА", "ФАНТА", "ЛИМОНАД", "СПРАЙТ"]
for p in products:
    box1.insert(END, p)
btn1 = Button(text = ">>>>", command = toBox2)
btn1.grid(row = 0, column = 1)
btn2 = Button(text = "<<<<", command = toBox1)
btn2.grid(row = 1, column = 1)
lab1 = Label(text = "кількість покупок")
lab1.grid(row = 2, column = 1)
lab2 = Label(text = "")
lab2.grid(row = 3, column = 1)
box2 = Listbox(selectmode = EXTENDED)
box2.grid(row = 0, column = 2, rowspan = 6)


root.mainloop()