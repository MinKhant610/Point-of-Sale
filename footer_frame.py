import tkinter as tk 
from tkinter import ttk

def footerFrame(main_frame):
    address_frame = tk.Frame(
        main_frame,
        width=1360,
        height=160,
        padx=4,
        pady=4,
        bg='#8face1'
    )
    address_frame.pack(side='bottom', anchor='e')

    lbl_address = tk.Label(
        address_frame,
        text='https://www.mochamojo.com, 09-251989175',
        fg='white',
        bg='#8face1',
        font=('courier', 14, 'bold')
    )
    lbl_address.pack(pady=3)

    return address_frame