from tkinter import *
import tkinter.messagebox as box
def dialog1():
    box.showinfo('info','Admin Login')
def dialog2():
    box.showinfo('info','Employee Login')
def dialog3():
    box.showinfo('info','Invalid Login')
window = Tk()
window.title('Countries Generation')
frame = Frame(window)
Label1 = Label(window,text = 'Username:')
Label1.pack(padx=15,pady= 5)
entry1 = Entry(window,bd =5)
entry1.pack(padx=15, pady=5)
u = entry1.get()
Label2 = Label(window,text = 'Password: ')
Label2.pack(padx = 15,pady=6)
entry2 = Entry(window, bd=5)
entry2.pack(padx = 15,pady=7)
p = entry2.get()
if u == 'admin' and  p == 'secret':
    btn = Button(frame, text = 'Check Login',command = dialog1)
elif u =='a' and p =='a':
    btn = Button(frame, text = 'Check Login',command = dialog2)    
else:
    btn = Button(frame, text ='Check Login', command = dialog3)
btn.pack(side = RIGHT , padx =5)
frame.pack(padx=100,pady = 19)
window.mainloop()
