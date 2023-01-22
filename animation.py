import tkinter

def move_lft():
    canvas.move(rect1, -3, 0)
    canvas.move(rect2, -3, 0)

def move_rght():
    canvas.move(rect1, +3, 0)
    canvas.move(rect2, +3, 0)

def move_up():
    canvas.move(rect1, 0, -3)
    canvas.move(rect2, 0, -3)

def move_dwn():
    canvas.move(rect1, 0, +3)
    canvas.move(rect2, 0, +3)

root = tkinter.Tk()
root.geometry("700x700")
canvas = tkinter.Canvas(width=600, height=600, bg='grey')
canvas.place(x=50, y=50)
rect2 = canvas.create_polygon(50, 150, 100, 100, 150, 100, 100, 150, fill='black')
rect1 = canvas.create_rectangle(50, 50, 100, 150, fill='yellow')
btn1 = tkinter.Button(bg='green', text='влево', command=move_lft)
btn1.place(x=0, y=660, width=100, height=30)
btn3 = tkinter.Button(bg='green', text='вверх', command=move_up)
btn3.place(x=150, y=660, width=100, height=30)
btn4 = tkinter.Button(bg='green', text='вниз', command=move_dwn)
btn4.place(x=300, y=660, width=100, height=30)
btn2 = tkinter.Button(bg='green', text='вправо', command=move_rght)
btn2.place(x=450, y=660, width=100, height=30)
root.mainloop()
