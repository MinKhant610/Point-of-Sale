import tkinter as tk 
from ttkbootstrap import ttk
from time import strftime
from datetime import datetime
import tempfile
import os

# color code 
# 40DF4B
# FFB200
# dd0329
class POS:
    def __init__(self, root):
        self.root = root
        self.root.title('Mocha Mojo - Point of Sale')
        self.root.geometry('1380x780+0+0')
        self.root.configure(bg='#dd0329')
        self.input_value = True

        # Variables
        self.coffee_images = []
        for i in range(1, 7):
            image = tk.PhotoImage(f'images/coffee{i}.gif')
            self.coffee_images.append(image)

        self.cake_images = []
        for i in range(1, 7):
            image = tk.PhotoImage(f'images/cake{i}.gif')
            self.cake_images.append(image)

        self.juice_images = []
        for i in range(1, 7):
            image = tk.PhotoImage(f'images/juice{i}.gif')
            self.juice_images.append(image)
        
        self.fruit_images = []
        for i in range(1, 7):
            image = tk.PhotoImage(f'images/fruit{i}.gif')
            self.fruit_images.append(image)
        
        global operator
        operator = ''
        change_input = tk.StringVar()
        cash_input = tk.StringVar() 
        tax_input = tk.StringVar() 
        sub_total = tk.StringVar()
        choice = tk.StringVar()
        
        # Layout
        main_frame = tk.Frame(self.root, bg='#dd0329')
        main_frame.grid(padx=8, pady=5)

        button_frame = tk.Frame(
            main_frame,
            border=3,
            width=1350,
            height=160,
            padx=4,
            pady=4,
            relief='ridge',
            bg='#dd0329'
        )

        button_frame.pack(side='bottom')

        data_frame = tk.Frame(
            main_frame,
            border=3,
            width=1300,
            height=400,
            padx=5,
            pady=5,
            relief='ridge',
            bg='#dd0329'
        )

        data_frame.pack(side='bottom')

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
            bg='#dd0329'
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

        food_item_frame = tk.LabelFrame(
            data_frame,
            bd=3,
            width=450,
            height=300,
            padx=5,
            pady=5,
            relief='ridge',
            bg='#dd0329',
            font=custom_font,
            text='Items'
        )
        food_item_frame.pack(side='right')

        cal_frame = tk.Frame(
            button_frame,
            bd=3,
            width=432,
            height=140,
            relief='ridge',
            bg='#ffffff'
        )
        cal_frame.grid(row=0, column=0, padx=4)

        change_frame = tk.Frame(
            button_frame,
            bd=3,
            width=500,
            height=140,
            pady=2,
            relief='ridge',
            bg='#ffffff'
        )
        change_frame.grid(row=0, column=1, padx=4)

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

        
        



def main():
    root = tk.Tk()
    pos = POS(root)
    root.mainloop()

if __name__ == '__main__':
    main()