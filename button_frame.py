import tkinter as tk
from tkinter import ttk
from calculate_frame import calFrame
from change_frame import changeFrame
from remove_frame import removeFrame

def buttonFrame(main_frame, sub_total_input, tax_input, total_input, choice, cash_input, change_input, operator):
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
    removeFrame(button_frame, choice, cash_input, change_input, operator,
    sub_total_input, tax_input, total_input)

    return button_frame
