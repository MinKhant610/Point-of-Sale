import tkinter as tk
from tkinter import ttk
from receipt_frame import getReceipt
from receipt_frame import getPosRecord
from change_frame import getCostEntry
import tempfile
import os 
import subprocess

def printSlip():
    text = getReceipt()
    slip = text.get('1.0', 'end-1c')
    filename = tempfile.mktemp('.txt')
    open(filename, 'w').write(slip)
    subprocess.run(['open', filename], check=True)

def payment():
    global choice_, cash, change
    cost = getCostEntry()
    if choice_.get() == 'Cash':
        cost.focus
        cash.set('')
    elif choice_.get() == '':
        cash.set('0')
        change.set('')

def giveChange():
    global cash, change
    if cash.get() == '0':
        change.set('')
        payment()
    pos_record = getPosRecord()
    item_cost = 0 
    tax = 5 
    get_cash = float(cash.get())

    for child in pos_record.get_children():
        item_cost += float(pos_record.item(child, 'values')[2])
    
    change.set(str(f'Ks {get_cash - (item_cost + ((item_cost * tax)/100))}'))

def clearDisplay():
    global op, change, cash
    global sub_total, tax, total
    operator = ''
    change.set('')
    cash.set('')
    sub_total.set('')
    tax.set('')
    total.set('')
    pos_record = getPosRecord() 
    for child in pos_record.get_children():
        pos_record.delete(child)

def removeItem():
    pass 
    

def removeFrame(button_frame, choice, cash_input, change_input, operator, sub_total_input, tax_input, total_input):
    global choice_, cash, change, op, sub_total, total, tax 
    op = operator
    sub_total = sub_total_input
    total = total_input
    tax = tax_input
    choice_ = choice
    cash = cash_input
    change = change_input
    custom_font = ('Helvetica', 16, 'normal')
    style = ttk.Style()
    style.configure(
        "Custom.TButton",
        background="#8face1",
        foreground="black",
        font=custom_font,
    )

    remove_frame = tk.Frame(
        button_frame,
        bd=3,
        width=400,
        height=140,
        pady=4,
        relief="ridge",
        bg="#8face1",
    )
    remove_frame.grid(row=0, column=2, padx=4)

    pay_btn = ttk.Button(remove_frame, text="Pay", style="Custom.TButton", width=10, command=giveChange)
    pay_btn.grid(row=0, column=0, padx=5, pady=10)

    remove_btn = ttk.Button(remove_frame, text="Remove Item", style="Custom.TButton", width=10)
    remove_btn.grid(row=0, column=1, padx=5, pady=10)

    reset_btn = ttk.Button(remove_frame, text="Reset", style="Custom.TButton", width=10, command=clearDisplay)
    reset_btn.grid(row=1, column=0, padx=5, pady=10)

    print_btn = ttk.Button(remove_frame, text="Print", style="Custom.TButton", width=10, command=printSlip)
    print_btn.grid(row=1, column=1, padx=5, pady=10)

    return remove_frame
