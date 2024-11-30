import tkinter as tk
from tkinter import ttk
from receipt_frame import getReceipt
import tempfile
import os 
import subprocess

def printSlip():
    text = getReceipt()
    slip = text.get('1.0', 'end-1c')
    filename = tempfile.mktemp('.txt')
    open(filename, 'w').write(slip)
    subprocess.run(['open', filename], check=True)
    print(slip)

def removeFrame(button_frame):
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

    pay_btn = ttk.Button(remove_frame, text="Pay", style="Custom.TButton", width=10)
    pay_btn.grid(row=0, column=0, padx=5, pady=10)

    remove_btn = ttk.Button(remove_frame, text="Remove Item", style="Custom.TButton", width=10)
    remove_btn.grid(row=0, column=1, padx=5, pady=10)

    reset_btn = ttk.Button(remove_frame, text="Reset", style="Custom.TButton", width=10)
    reset_btn.grid(row=1, column=0, padx=5, pady=10)

    print_btn = ttk.Button(remove_frame, text="Print", style="Custom.TButton", width=10, command=printSlip)
    print_btn.grid(row=1, column=1, padx=5, pady=10)

    return remove_frame
