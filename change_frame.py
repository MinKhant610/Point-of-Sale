import tkinter as tk
from tkinter import ttk 

def changeFrame(button_frame, choice, cash_input, change_input):
    custom_font=('Helvetica', 18, 'bold')
    global cost_entry
    change_frame = tk.Frame(
        button_frame,
        bd=3,
        width=500,
        height=140,
        pady=2,
        relief='ridge',
        bg='#8face1'
    )
    change_frame.grid(row=0, column=1, padx=4)

    method_of_payment = tk.Label(change_frame, text='Method of Payment', font=custom_font, foreground='white', bg='#8face1')

    cost = tk.Label(change_frame, text='Cost', font=custom_font,foreground='white', bg='#8face1')

    change = tk.Label(change_frame, text='Change', font=custom_font, foreground='white', bg='#8face1') 

    payment_entry = ttk.Combobox(change_frame, font=custom_font,
    width=30, state='readonly', textvariable=choice, justify='right')
    payment_entry['values'] = ('', 'Cash', 'K Pay', 'Wave', 'CB Pay', 'AYA Pay')
    payment_entry.current(0)

    cost_entry = tk.Entry(change_frame, font=custom_font, width=30, 
    textvariable=cash_input, justify='right')

    change_entry = tk.Entry(change_frame, font=custom_font, width=30, 
    textvariable=change_input, justify='right')

    method_of_payment.grid(row=0, column=0, padx=5, pady=2)
    cost.grid(row=1, column=0, padx=5, pady=2)
    change.grid(row=2, column=0, padx=5, pady=2)

    payment_entry.grid(row=0, column=1, padx=5, pady=5)
    cost_entry.grid(row=1, column=1, padx=5, pady=5)
    change_entry.grid(row=2, column=1, padx=5, pady=5)

    return change_frame

def getCostEntry():
    global cost_entry
    return cost_entry
