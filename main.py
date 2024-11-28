import tkinter as tk 
from tkinter import ttk
from time import strftime
from datetime import datetime
from button_frame import buttonFrame
from food_item_frame import foodItemFrame
from data_frame_left_cover import dataFrameLeftCover
import tempfile
import os


# color code 
#dd0329
#8face1
#e0f1ff
#667799

class POS:
    def __init__(self, root):
        self.root = root
        self.root.title('Mocha Mojo - Point of Sale')
        self.root.geometry('1380x780+0+0')
        self.root.configure(bg='#8face1')
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
        sub_total_input = tk.StringVar()
        total_input = tk.StringVar()
        choice = tk.StringVar()
        
        # Layout
        main_frame = tk.Frame(self.root, bg='#8face1')
        main_frame.grid(padx=8, pady=5)

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
        dataFrameLeftCover(data_frame)
        #food item frame is data frame right cover
        foodItemFrame(data_frame)

        

        



def main():
    root = tk.Tk()
    pos = POS(root)
    style = ttk.Style()
    root.mainloop()

if __name__ == '__main__':
    main()