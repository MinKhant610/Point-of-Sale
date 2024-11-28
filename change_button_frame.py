import tkinter as tk 
from tkinter import ttk

def changeButtonFrame(data_frame_left_cover):
    custom_font = ('Helvetica', 16, 'bold')
    change_button_frame = tk.Frame(
        data_frame_left_cover,
        bd=3,
        width=300,
        height=460,
        pady=5,
        relief='ridge',
        bg='#8face1'
    )
    change_button_frame.pack(side='left', padx=4)

    buttons = [
        ('7', 0, 0), ('8', 0, 1), ('9', 0, 2),
        ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
        ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
        ('0', 3, 0), ('.', 3, 1), ('C', 3, 2),
    ]

    for text, row, col in buttons:
        tk.Button(change_button_frame, text=text, width=4,
        font=custom_font, height=5, padx=3,
        ).grid(row=row, column=col, padx=3, pady=3)

    return change_button_frame