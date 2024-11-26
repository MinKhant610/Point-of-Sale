import tkinter as tk
from ttkbootstrap import ttk

def dataFrameLeftCover(data_frame):
    custom_font=('Helvetica', 14, 'bold')
    data_frame_left_cover = tk.LabelFrame(
        data_frame,
        border=3,
        pady=2,
        width=800,
        height=300,
        relief='ridge',
        text='Point of Sale',
        font=custom_font,
        bg='#8face1'
    )
    
    data_frame_left_cover.pack(side='left', padx=5)

    chage_button_frame = tk.Frame(
        data_frame_left_cover,
        bd=3,
        width=300,
        height=460,
        pady=5,
        relief='ridge',
        bg='#ffffff'
    )
    chage_button_frame.pack(side='left', padx=4)

    recipt_frame = tk.Frame(
        data_frame_left_cover,
        bd=3,
        width=200,
        height=400,
        pady=5,
        padx=1,
        relief='ridge',
        bg='#ffffff'
    )
    recipt_frame.pack(side='right')
    
    return data_frame_left_cover