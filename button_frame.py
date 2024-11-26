import tkinter as tk
from tkinter import ttk
from calculate_frame import calFrame
from change_frame import changeFrame

def buttonFrame(main_frame, sub_total_input, tax_input, total_input, choice, cash_input, change_input):
    # Button Frame
    button_frame = tk.Frame(
        main_frame,
        border=3,
        width=1350,
        height=160,
        padx=4,
        pady=4,
        relief='ridge',
        bg='#8face1'
    )
    button_frame.pack(side='bottom')

    calFrame(button_frame, sub_total_input, tax_input, total_input)
    changeFrame(button_frame, choice, cash_input, change_input)

    # Remove Frame
    remove_frame = tk.Frame(
        button_frame,
        bd=3,
        width=400,
        height=140,
        pady=4,
        relief='ridge',
        bg='#ffffff'
    )
    remove_frame.grid(row=0, column=2, padx=4)

    return button_frame
