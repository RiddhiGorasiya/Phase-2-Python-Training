import tkinter as tk  # another way to import tkinter
win = tk.Tk()
# widgets are added here
win.mainloop()

from tkinter import*

win = Tk() # Tk is a class
win.title("My First GUI") # title of the window
win.iconbitmap(r"C:\Users\Vaibhav Gorasiya\Pictures\Saved Pictures\gui_cogs_icon_158494.ico")
win.attributes('-alpha',1) # transparency of the window (0.0 to 1.0)
win.config(bg="lightblue")
win.geometry("600x400+100+100") # width x height + x_offset + y_offset
# win.resizable(0,0) # to disable the resizing of window (width,height

# label
win = Label(text='GeeksForGeeks.org!')
win.pack()

win.mainloop() # run the window continously

# botton
import tkinter as tk
r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()

# entry
from tkinter import *
master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()

#  checkbutton
from tkinter import *
master = Tk()
var1 = IntVar() 
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)
mainloop()

# radiobutton
from tkinter import *
root = Tk()
Radiobutton(root, text="Option 1", value=1).pack(anchor=W)
Radiobutton(root, text="Option 2", value=2).pack(anchor=W)  
mainloop()

# listbox

from tkinter import *
top = Tk()
Lb = Listbox(top)
Lb.insert(1, "python")
Lb.insert(2, "java")
Lb.insert(3, "c++")
Lb.insert(4, "c#")
Lb.insert(5, "java script")
Lb.insert(6, "Any other")
Lb.pack()
top.mainloop()

# scrollbar
from tkinter import *
root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
mylist = Listbox(root, yscrollcommand=scrollbar.set)

for line in range(100):
    mylist.insert(END, 'This is line number' + str(line))
mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)
mainloop()

# menu
from tkinter import *
root =Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
mainloop()

# combo box
import tkinter as tk
from tkinter import ttk

def select(event):
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)

root = tk.Tk()
root.title("Combobox Example")

# Create a label
label = tk.Label(root, text="Selected Item: ")
label.pack(pady=10)

# Create a Combobox widget
combo_box = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"], state='readonly')
combo_box.pack(pady=5)

# Set default value
combo_box.set("Option 1")

# Bind event to selection
combo_box.bind("<<ComboboxSelected>>", select)
root.mainloop()

scale
from tkinter import *
master = Tk()
w = Scale(master, from_=0, to=100)
w.pack()
w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()
mainloop()

# toplvel
from tkinter import *
root = Tk()
root.title('PHASE-1')
top = Toplevel()
top.title('PHASE-2')
top.mainloop()

# message box
from tkinter import *
main = Tk()
ourMessage = 'This is our Message'
messageVar = Message(main, text=ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack()
main.mainloop()

# menubutton
from tkinter import *
top = Tk()
mb = Menubutton(top, text = "Python Training")
mb.grid()
mb.menu = Menu(mb, tearoff = 0)
mb["menu"] = mb.menu
cVar = IntVar()
aVar = IntVar()
mb.menu.add_checkbutton(label='Contact', variable=cVar)
mb.menu.add_checkbutton(label='About Us', variable=aVar)
mb.pack()
top.mainloop()

# progressbar
import tkinter as tk
from tkinter import ttk
import time

def strat_progress():
    progress.start()

    for i in range(101):
        time.sleep(0.05)
        progress['value'] = i
        root.update_idletasks()
    progress.stop()

root = tk.Tk()
root.title("Progress Example")

progress = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=300, mode='determinate')
progress.pack(pady=20)

strat_button = tk.Button(root, text="Start Progress", command=strat_progress)
strat_button.pack(pady=10)
root.mainloop()

# spinbox
from tkinter import *
master = Tk()
w = Spinbox(master, from_=0, to=10)
w.pack()
mainloop()

# text
from tkinter import*
root = Tk()
T = Text(root, height=5, width=30)
T.pack()
T.insert(END, "Welcome to \nBest Website")
mainloop()