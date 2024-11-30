import tkinter as tk
from tkinter import ttk
from change_button_frame import changeButtonFrame
from receipt_frame import receiptFrame

def dataFrameLeftCover(data_frame, operator, cash_input, change_input):
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

    changeButtonFrame(data_frame_left_cover, operator, cash_input, change_input)

    frame, get_pos_record, text = receiptFrame(data_frame_left_cover)
    
    return data_frame_left_cover, get_pos_record, text