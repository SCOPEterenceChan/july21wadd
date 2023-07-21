from tkinter import Tk, Canvas
frame=Tk()
canvas=Canvas(bg='black',height=350,width=300)

canvas.create_rectangle(50, 60, 240, 160, fill='red',
                        outline='blue')
canvas.create_text(100, 100, text='A wonderful story',
                   anchor='nw', font='TkMenuFont', fill='green')
canvas.create_line(100, 115, 195, 115)
canvas.pack()
frame.mainloop()
