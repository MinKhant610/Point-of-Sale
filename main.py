import tkinter as tk 
from tkinter import ttk
from time import strftime
from datetime import datetime
from button_frame import buttonFrame
from food_item_frame import foodItemFrame
from data_frame_left_cover import dataFrameLeftCover
from heading_frame import headingFrame
from footer_frame import footerFrame
import tempfile
import os

# color code 
#8face1 => main color 
#dd0329
#e0f1ff
#667799

class POS:
    def __init__(self, root):
        self.root = root
        self.root.title('Mocha Mojo - Point of Sale')
        self.root.geometry('1380x780+0+0')
        self.root.configure(bg='#8face1')
        self.input_value = True
        
        global operator
        global sub_total_input, tax_input, total_input
        operator = ''
        change_input = tk.StringVar()
        cash_input = tk.StringVar() 
        tax_input = tk.StringVar() 
        sub_total_input = tk.StringVar()
        total_input = tk.StringVar()
        choice = tk.StringVar()
        
        # Layout
        main_frame = tk.Frame(self.root, bg='#8face1')
        main_frame.grid(padx=8, pady=5)

        headingFrame(main_frame)
        footerFrame(main_frame)
        buttonFrame(main_frame, sub_total_input, tax_input, 
        total_input, choice, cash_input, change_input)
        
        data_frame = tk.Frame(
            main_frame,
            border=3,
            width=1300,
            height=400,
            padx=5,
            pady=5,
            relief='ridge',
            bg='#8face1'
        )

        data_frame.pack(side='bottom')

        custom_font=('Helvetica', 14, 'bold')
        frame, get_pos_record, text = dataFrameLeftCover(data_frame)
        #food item frame is data frame right cover
        foodItemFrame(
            data_frame,
            get_pos_record,
            text,
            sub_total_input,
            tax_input,
            total_input
            )



        



def main():
    root = tk.Tk()
    pos = POS(root)
    style = ttk.Style()
    root.mainloop()

if __name__ == '__main__':
    main()