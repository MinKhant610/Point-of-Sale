import tkinter as tk
from tkinter import ttk

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

    global coffee_images
    coffee_images = []
    for i in range(1, 7):
        image = tk.PhotoImage(file=f'images/coffee{i}.gif')
        coffee_images.append(image)

    global cake_images 
    cake_images = []
    for i in range(1, 7):
        image = tk.PhotoImage(file=f'images/cake{i}.gif')
        cake_images.append(image)

    global juice_images
    juice_images = []
    for i in range(1, 7):
        image = tk.PhotoImage(file=f'images/juice{i}.gif')
        juice_images.append(image)
        
    global fruit_images
    fruit_images = []
    for i in range(1, 7):
        image = tk.PhotoImage(file=f'images/fruit{i}.gif')
        fruit_images.append(image)

    coffee_btn1 = tk.Button(food_item_frame, image=coffee_images[0], width=104, height=104, bd=2)
    coffee_btn1.grid(row=0, column=0, pady=2)

    coffee_btn2 = tk.Button(food_item_frame, image=coffee_images[1], width=104, height=104, bd=2)
    coffee_btn2.grid(row=0, column=1, pady=2)

    coffee_btn3 = tk.Button(food_item_frame, image=coffee_images[2], width=104, height=104, bd=2)
    coffee_btn3.grid(row=0, column=2, pady=2)

    coffee_btn4 = tk.Button(food_item_frame, image=coffee_images[3], width=104, height=104, bd=2)
    coffee_btn4.grid(row=0, column=3, pady=2)

    coffee_btn5 = tk.Button(food_item_frame, image=coffee_images[4], width=104, height=104, bd=2)
    coffee_btn5.grid(row=0, column=4, pady=2)

    coffee_btn6 = tk.Button(food_item_frame, image=coffee_images[5], width=104, height=104, bd=2)
    coffee_btn6.grid(row=0, column=5, pady=2)

    # cake
    cake_btn1 = tk.Button(food_item_frame, image=cake_images[0], width=104, height=104, bd=2)
    cake_btn1.grid(row=1, column=0, pady=2)

    cake_btn2 = tk.Button(food_item_frame, image=cake_images[1], width=104, height=104, bd=2)
    cake_btn2.grid(row=1, column=1, pady=2)
    
    cake_btn3 = tk.Button(food_item_frame, image=cake_images[2], width=104, height=104, bd=2)
    cake_btn3.grid(row=1, column=2, pady=2)
    
    cake_btn4 = tk.Button(food_item_frame, image=cake_images[3], width=104, height=104, bd=2)
    cake_btn4.grid(row=1, column=3, pady=2)
    
    cake_btn5 = tk.Button(food_item_frame, image=cake_images[4], width=104, height=104, bd=2)
    cake_btn5.grid(row=1, column=4, pady=2)
    
    cake_btn6 = tk.Button(food_item_frame, image=cake_images[5], width=104, height=104, bd=2)
    cake_btn6.grid(row=1, column=5, pady=2)

    # juice 
    juice_btn1 = tk.Button(food_item_frame, image=juice_images[0], width=104, height=104, bd=2)
    juice_btn1.grid(row=2, column=0, pady=2)

    juice_btn2 = tk.Button(food_item_frame, image=juice_images[1], width=104, height=104, bd=2)
    juice_btn2.grid(row=2, column=1, pady=2)
    
    juice_btn3 = tk.Button(food_item_frame, image=juice_images[2], width=104, height=104, bd=2)
    juice_btn3.grid(row=2, column=2, pady=2)
    
    juice_btn4 = tk.Button(food_item_frame, image=juice_images[3], width=104, height=104, bd=2)
    juice_btn4.grid(row=2, column=3, pady=2)
    
    juice_btn5 = tk.Button(food_item_frame, image=juice_images[4], width=104, height=104, bd=2)
    juice_btn5.grid(row=2, column=4, pady=2)
    
    juice_btn6 = tk.Button(food_item_frame, image=juice_images[5], width=104, height=104, bd=2)
    juice_btn6.grid(row=2, column=5, pady=2)
    
    # fruit 
    fruit_btn1 = tk.Button(food_item_frame, image=fruit_images[0], width=104, height=104, bd=2)
    fruit_btn1.grid(row=3, column=0, pady=2)

    fruit_btn2 = tk.Button(food_item_frame, image=fruit_images[1], width=104, height=104, bd=2)
    fruit_btn2.grid(row=3, column=1, pady=2)
    
    fruit_btn3 = tk.Button(food_item_frame, image=fruit_images[2], width=104, height=104, bd=2)
    fruit_btn3.grid(row=3, column=2, pady=2)
    
    fruit_btn4 = tk.Button(food_item_frame, image=fruit_images[3], width=104, height=104, bd=2)
    fruit_btn4.grid(row=3, column=3, pady=2)
    
    fruit_btn5 = tk.Button(food_item_frame, image=fruit_images[4], width=104, height=104, bd=2)
    fruit_btn5.grid(row=3, column=4, pady=2)
    
    fruit_btn6 = tk.Button(food_item_frame, image=fruit_images[5], width=104, height=104, bd=2)
    fruit_btn6.grid(row=3, column=5, pady=2)

    return food_item_frame