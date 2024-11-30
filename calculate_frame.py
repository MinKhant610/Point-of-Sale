import tkinter as tk
from tkinter import ttk

def calFrame(button_frame, sub_total_input, tax_input, total_input):
    custom_font=('Helvetica', 18, 'bold')
    cal_frame = tk.Frame(
        button_frame,
        bd=3,
        width=432,
        height=140,
        relief='ridge',
        bg='#8face1'
    )
    cal_frame.grid(row=0, column=0, padx=5)

    lbl_sub_total = tk.Label(cal_frame, text='Sub Total', font=custom_font, foreground='white', bg='#8face1')
    lbl_tax = tk.Label(cal_frame, text='Tax', font=custom_font,foreground='white', bg='#8face1')
    lbl_total = tk.Label(cal_frame, text='Total', font=custom_font, foreground='white', bg='#8face1') 

    sub_total_entry = tk.Entry(cal_frame, font=custom_font, 
    width=30, textvariable=sub_total_input, justify='right')
    tax_entry = tk.Entry(cal_frame, font=custom_font, width=30, 
    textvariable=tax_input, justify='right')
    total_entry = tk.Entry(cal_frame, font=custom_font, width=30, 
    textvariable=total_input, justify='right')

    lbl_sub_total.grid(row=0, column=0, padx=5, pady=2)
    lbl_tax.grid(row=1, column=0, padx=5, pady=2)
    lbl_total.grid(row=2, column=0, padx=5, pady=2)

    sub_total_entry.grid(row=0, column=1, padx=5, pady=4)
    tax_entry.grid(row=1, column=1, padx=5, pady=4)
    total_entry.grid(row=2, column=1, padx=5, pady=4)

    return cal_frame
