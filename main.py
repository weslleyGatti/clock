from tkinter import *
import clock as cl
import time
app = cl.App()

def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    am_pm = time.strftime("%p")

    lbl1.config(text=hour + ":" + minute + ":" + second + " " + am_pm)
    lbl1.after(1000,clock)
    lbl2.config(text = day)
    

lbl1 = Label(app, text="", font = ("Helvetica", 48), fg="green", bg="black")
lbl1.pack(pady=20)
lbl2 = Label(app, text="", font = ("Helvetica", 14))
lbl2.pack(pady=10)

clock()

#LOOP#
if __name__ == "__main__":
    app.mainloop()