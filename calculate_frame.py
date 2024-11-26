import tkinter as tk
from ttkbootstrap import ttk

def calFrame(button_frame, sub_total_input, tax_input, total_input):
    custom_font=('Helvetica', 14, 'bold')
    cal_frame = tk.Frame(
        button_frame,
        bd=3,
        width=432,
        height=140,
        relief='ridge',
        bg='#dd0329'
    )
    cal_frame.grid(row=0, column=0, padx=5)

    lbl_sub_total = tk.Label(cal_frame, text='Sub Total', font=custom_font, foreground='white', bg='#dd0329')
    lbl_tax = tk.Label(cal_frame, text='Tax', font=custom_font,foreground='white', bg='#dd0329')
    lbl_total = tk.Label(cal_frame, text='Total', font=custom_font, foreground='white', bg='#dd0329') 

    sub_total_entry = tk.Entry(cal_frame, font=custom_font, 
    width=24, textvariable=sub_total_input)
    tax_entry = tk.Entry(cal_frame, font=custom_font, width=24, 
    textvariable=tax_input)
    total_entry = tk.Entry(cal_frame, font=custom_font, width=24, 
    textvariable=total_input)

    lbl_sub_total.grid(row=0, column=0, padx=5, pady=2)
    lbl_tax.grid(row=1, column=0, padx=5, pady=2)
    lbl_total.grid(row=2, column=0, padx=5, pady=2)

    sub_total_entry.grid(row=0, column=1, padx=5, pady=5)
    tax_entry.grid(row=1, column=1, padx=5, pady=5)
    total_entry.grid(row=2, column=1, padx=5, pady=5)

    return cal_frame
