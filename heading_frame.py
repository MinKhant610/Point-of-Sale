import tkinter as tk 
from tkinter import ttk
from time import strftime
from datetime import datetime

def time(lbl_current_time):
    string = strftime('%H:%M%:%S %p')
    lbl_current_time.config(text=string)
    lbl_current_time.after(1000, lambda:time(lbl_current_time))

def headingFrame(main_frame):
    mocha_frame = tk.Frame(main_frame, bd=0, width=1360, height=100, padx=4, pady=10, bg='#8face1', relief='ridge')
    mocha_frame.pack(side='top', anchor='w')

    lbl_mocha = tk.Label(
        mocha_frame,
        font=('arieal', 24, 'bold'),
        text='Mocha Mojo - POS System',
        bd=0,
        fg='white',
        bg='#8face1',
    )
    lbl_mocha.pack()

    time_frame = tk.Frame(main_frame, bd=0, width=1360, height=100, padx=4, pady=4, bg='#8face1')
    time_frame.pack(side='top', anchor='e')

    lbl_date = tk.Label(
        time_frame,
        text=f'{datetime.now():%a %d %b %Y}',
        fg='white',
        bg='#8face1',
        font=('courier', 14)
    )
    lbl_date.pack()

    lbl_current_time = tk.Label(time_frame, fg='white', bg='#8face1', font=('courier', 14, 'bold'))
    lbl_current_time.pack()
    time(lbl_current_time)

    return mocha_frame