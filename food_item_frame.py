import tkinter as tk
from ttkbootstrap import ttk

def foodItemFrame(data_frame):
    custom_font=('Helvetica', 14, 'bold')
    food_item_frame = tk.LabelFrame(
        data_frame,
        bd=3,
        width=450,
        height=300,
        padx=5,
        pady=5,
        relief='ridge',
        bg='#8face1',
        font=custom_font,
        text='Items'
    )
    food_item_frame.pack(side='right')
    return food_item_frame