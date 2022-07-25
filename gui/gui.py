import tkinter as tk
from tkinter import filedialog as fd
from System_Simulation import System_Simulation


#main window difinitions
window = tk.Tk()
window.title('laserEngraving')
window.resizable(False, False)
window.geometry('1000x700')

#global variables
file_link =0

#functions for tk
def select_file():
    global file_link
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    file_link = filename
  
    
       
  
    
System_Simulation(file_link)  #removable
    






#items design   
file_button = tk.Button(
    window,
    text='Open a File',
    command=select_file
)



file_button.pack(expand=True)    
    

window.mainloop()