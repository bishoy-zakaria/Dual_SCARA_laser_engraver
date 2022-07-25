import tkinter as tk
from tkinter import ttk
import datetime as dt
from tkinter import filedialog as fd
import System_Simulation
import start
import Hard_Ware

window = tk.Tk()
window.title('laserEngraving')
window.resizable(False, False)
window.geometry('1000x700+250+50')

#global variables
file_link =0
error1 =0
error2 =0
error3 =0
error4 =0
best_solution=0

var=tk.IntVar()


def minimum_error_solution():
    global error1,error2,error3,error4,min_solution
    min=0
    data=[error1,error2,error3,error4]
    min=data[0]
    for n in range(4):
        if data[n]<min:
            min= data[n]
    for m in range(4):
        if data[m]== min:
            min_solution= m+1
    return min_solution
    

def select_file():
    global file_link,file_path_label
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    file_link = filename
    file_path_label.config(text = file_link)

def Delete_obj():
    file_button.place_forget() 
    start_initialization_order_button.place_forget() 
    stop_initialization_order_button.place_forget() 
    start_simulation_order_button.place_forget()
    main_button.place_forget()
    start_order_button.place_forget()
    version_main_label_1.place_forget()
    version_main_label_2.place_forget()
    initializing_label.place_forget()
    simulation_label.place_forget()
    error_1_label.place_forget()
    error_1_val_label.place_forget()
    error_2_label.place_forget()
    error_2_val_label.place_forget()
    error_3_label.place_forget()
    error_3_val_label.place_forget()
    error_4_label.place_forget()
    error_4_val_label.place_forget()
    pb.place_forget()
    start_label.place_forget()
    R1.place_forget()
    R2.place_forget()
    R3.place_forget()
    R4.place_forget()

    
def main_window():
    Delete_obj()
    
    initialization_button.place(x=50,y=220)
    simulation_button.place(x=50,y=300)
    start_button.place(x=50,y=380)
    
    date_label.place(x=500,y=10)
    file_path_label.place(x=660,y=10)
    
    version_main_label_1.place(x=500,y=250)
    version_main_label_2.place(x=450,y=310)

def initialization_window():

   Delete_obj()
   
   initializing_label.place(x=400,y=250)
   stop_initialization_order_button.place(x=700,y=350)
   start_initialization_order_button.place(x=500,y=350)
   main_button.place(x=300,y=350)


def start_initialization_order():
    x=0
    Hard_Ware.System_init()


def stop_initialization_order():
    x=0
    Hard_Ware.Init_End()


def simulation_window():
    Delete_obj()
    
    simulation_label.place(x=450,y=150)
    error_1_label.place(x=300,y=300)
    error_1_val_label.place(x=380,y=300)
    error_2_label.place(x=300,y=350)
    error_2_val_label.place(x=380,y=350)
    error_3_label.place(x=300,y=400)
    error_3_val_label.place(x=380,y=400)
    error_4_label.place(x=300,y=450)
    error_4_val_label.place(x=380,y=450)
    
    file_button.place(x=300,y=500)
    main_button.place(x=500,y=500)
    start_simulation_order_button.place(x=700,y=500)
    
    

def start_simulation_order():
    global file_link,error1,error2,error3,error4  
    buffer=0
    pb.place(x=375,y=230)
    progress(25)
    buffer=list(System_Simulation.System_Simulation(file_link))
    progress(System_Simulation.progress)
    error1=buffer[0]
    error2=buffer[1]
    error3=buffer[2]
    error4=buffer[3]
    error_1_val_label.config(text = error1)
    error_2_val_label.config(text = error2)
    error_3_val_label.config(text = error3)
    error_4_val_label.config(text = error4)
    
def start_window():
    global best_solution
    Delete_obj()
    
    start_label.place(x=500,y=150)
    main_button.place(x=400,y=500)
    start_order_button.place(x=600,y=500)
    R1.place(x=400,y=300)
    R2.place(x=400,y=350)
    R3.place(x=400,y=400)
    R4.place(x=400,y=450)
   

def start_order():
    global best_solution,file_link
    pb.place(x=375,y=230)
    best_solution=var.get()
    start.System_Start(file_link,best_solution)
    progress(start.progress)




def progress(val):
    if pb['value'] < 100:
        pb['value'] = val



#**** labels *******
date = dt.datetime.now()
# Create Label to display the Date
date_label = tk.Label(window, text=f"{date:%A, %B %d, %Y} |", font="Calibri, 12")
file_path_label = tk.Label(window, text="", font="Calibri, 12")

version_main_label_1 = tk.Label(window, text="LASER", font="Calibri, 40")
version_main_label_2 = tk.Label(window, text="ENGRAVER", font="Calibri, 40")

initializing_label = tk.Label(window, text="INITIALIZING", font="Calibri, 40")
simulation_label = tk.Label(window, text="SIMULATION", font="Calibri, 30")
error_1_label = tk.Label(window, text="error1:", font="Calibri, 16")
error_1_val_label = tk.Label(window, text="", font="Calibri, 16")
error_2_label = tk.Label(window, text="error2:", font="Calibri, 16")
error_2_val_label = tk.Label(window, text="", font="Calibri, 16")
error_3_label = tk.Label(window, text="error3:", font="Calibri, 16")
error_3_val_label = tk.Label(window, text="", font="Calibri, 16")
error_4_label = tk.Label(window, text="error4:", font="Calibri, 16")
error_4_val_label = tk.Label(window, text="", font="Calibri, 16")
start_label = tk.Label(window, text="START", font="Calibri, 30")

    
#**** Buttons ******
file_button = tk.Button(
    window,
    text='Open File',height=3,width=20,
    command=select_file)


initialization_button = tk.Button(
    window,
    text='initialize',height=3,width=20,
    command=initialization_window)

start_initialization_order_button = tk.Button(
    window,
    text='start',height=3,width=20,
    command=start_initialization_order)

stop_initialization_order_button = tk.Button(
    window,
    text='stop',height=3,width=20,
    command=stop_initialization_order)
  
simulation_button = tk.Button(
    window,
    text='simulation',height=3,width=20,
    command=simulation_window)

start_simulation_order_button = tk.Button(
    window,
    text='start',height=3,width=20,
    command=start_simulation_order)

start_button = tk.Button(
    window,
    text='start',height=3,width=20,
    command=start_window) 

main_button = tk.Button(
    window,
    text='main menu',height=3,width=20,
    command=main_window)  

start_order_button = tk.Button(
    window,
    text='start',height=3,width=20,
    command=start_order)  

#progress bar
pb = ttk.Progressbar(
    window,
    orient='horizontal',
    mode='determinate',
    length=400
)

#radio button
R1 = tk.Radiobutton(window, text="Solution 1", variable=var, value=1)
R2 = tk.Radiobutton(window, text="Solution 2", variable=var, value=2)
R3 = tk.Radiobutton(window, text="Solution 3", variable=var, value=3)
R4 = tk.Radiobutton(window, text="Solution 4", variable=var, value=4)

'''
pg= PhotoImage(file="back.png")
my_label=tk.Label(window,image=pg)
'''
main_window()
window.mainloop()