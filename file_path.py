
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os
import pyperclip


win = Tk()
win.title('File path getter and copier by thk6634#1432')

win.geometry("700x350")

def open_file():
   file = filedialog.askopenfile(mode='r', filetypes=[('All', '*.*')])
   if file:
      filepath = os.path.abspath(file.name)
      Label(win, text="The file's path was successfully copied to clipboard.", font=('Aerial 11')).pack()
      pyperclip.copy(str(filepath))

      

label = Label(win, text="Click the Button to browse the Files", font=('Georgia 13'))
label.pack(pady=10)

ttk.Button(win, text="Browse", command=open_file).pack(pady=20)

win.mainloop()