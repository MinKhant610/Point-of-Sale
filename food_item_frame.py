import tkinter as tk
from tkinter import ttk

def addItem(item_name, item_cost):
    global record, text, sub_total, tax, total
    tax_cost = 5 
    
    record.insert('', tk.END, values=(item_name, '1', str(item_cost)))
    text.insert(tk.END, f'{item_name}\t\t\t1\t\t\t{item_cost}\n')
    
    total_cost = 0
    for child in record.get_children():
        total_cost += float(record.item(child, 'values')[2])
    
    sub_total.set(f'Ks {total_cost:.2f}')
    tax.set(f'Ks {(total_cost * tax_cost / 100):.2f}')
    total.set(f'Ks {(total_cost + (total_cost * tax_cost / 100)):.2f}')


def foodItemFrame(data_frame, pos_record, text_, sub_total_input, tax_input, total_input):
    global record, text
    global sub_total, total
    global tax
    record = pos_record
    text = text_ 
    sub_total = sub_total_input
    tax = tax_input
    total = total_input
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

    coffee_btn1 = tk.Button(food_item_frame, image=coffee_images[0], width=104, height=104, bd=2, command=lambda:addItem('Coffee1', 1500))
    coffee_btn1.grid(row=0, column=0, pady=2)

    coffee_btn2 = tk.Button(food_item_frame, image=coffee_images[1], width=104, height=104, bd=2, command=lambda:addItem('Coffee2', 1500))
    coffee_btn2.grid(row=0, column=1, pady=2)

    coffee_btn3 = tk.Button(food_item_frame, image=coffee_images[2], width=104, height=104, bd=2, command=lambda:addItem('Coffee3', 2000))
    coffee_btn3.grid(row=0, column=2, pady=2)

    coffee_btn4 = tk.Button(food_item_frame, image=coffee_images[3], width=104, height=104, bd=2, command=lambda:addItem('Coffee4', 6500))
    coffee_btn4.grid(row=0, column=3, pady=2)

    coffee_btn5 = tk.Button(food_item_frame, image=coffee_images[4], width=104, height=104, bd=2, command=lambda:addItem('Coffee5', 6500))
    coffee_btn5.grid(row=0, column=4, pady=2)

    coffee_btn6 = tk.Button(food_item_frame, image=coffee_images[5], width=104, height=104, bd=2, command=lambda:addItem('Coffee6', 4500))
    coffee_btn6.grid(row=0, column=5, pady=2)

    # cake
    cake_btn1 = tk.Button(food_item_frame, image=cake_images[0], width=104, height=104, bd=2, command=lambda:addItem('Cake1', 1500))
    cake_btn1.grid(row=1, column=0, pady=2)

    cake_btn2 = tk.Button(food_item_frame, image=cake_images[1], width=104, height=104, bd=2, command=lambda:addItem('Cake2', 5500))
    cake_btn2.grid(row=1, column=1, pady=2)
    
    cake_btn3 = tk.Button(food_item_frame, image=cake_images[2], width=104, height=104, bd=2, command=lambda:addItem('Cake3', 9500))
    cake_btn3.grid(row=1, column=2, pady=2)
    
    cake_btn4 = tk.Button(food_item_frame, image=cake_images[3], width=104, height=104, bd=2, command=lambda:addItem('Cake4', 8500))
    cake_btn4.grid(row=1, column=3, pady=2)
    
    cake_btn5 = tk.Button(food_item_frame, image=cake_images[4], width=104, height=104, bd=2, command=lambda:addItem('Cake5', 4500))
    cake_btn5.grid(row=1, column=4, pady=2)
    
    cake_btn6 = tk.Button(food_item_frame, image=cake_images[5], width=104, height=104, bd=2, command=lambda:addItem('Cake6', 7500))
    cake_btn6.grid(row=1, column=5, pady=2)

    # juice 
    juice_btn1 = tk.Button(food_item_frame, image=juice_images[0], width=104, height=104, bd=2, command=lambda:addItem('Juice1', 1500))
    juice_btn1.grid(row=2, column=0, pady=2)

    juice_btn2 = tk.Button(food_item_frame, image=juice_images[1], width=104, height=104, bd=2, command=lambda:addItem('Juice2', 1500))
    juice_btn2.grid(row=2, column=1, pady=2)
    
    juice_btn3 = tk.Button(food_item_frame, image=juice_images[2], width=104, height=104, bd=2, command=lambda:addItem('Juice3', 4500))
    juice_btn3.grid(row=2, column=2, pady=2)
    
    juice_btn4 = tk.Button(food_item_frame, image=juice_images[3], width=104, height=104, bd=2, command=lambda:addItem('Juice4', 2500))
    juice_btn4.grid(row=2, column=3, pady=2)
    
    juice_btn5 = tk.Button(food_item_frame, image=juice_images[4], width=104, height=104, bd=2, command=lambda:addItem('Juice5', 5500))
    juice_btn5.grid(row=2, column=4, pady=2)
    
    juice_btn6 = tk.Button(food_item_frame, image=juice_images[5], width=104, height=104, bd=2, command=lambda:addItem('Juice6', 5500))
    juice_btn6.grid(row=2, column=5, pady=2)
    
    # fruit 
    fruit_btn1 = tk.Button(food_item_frame, image=fruit_images[0], width=104, height=104, bd=2, command=lambda:addItem('Fruit1', 2000))
    fruit_btn1.grid(row=3, column=0, pady=2)

    fruit_btn2 = tk.Button(food_item_frame, image=fruit_images[1], width=104, height=104, bd=2, command=lambda:addItem('Fruit2', 2000))
    fruit_btn2.grid(row=3, column=1, pady=2)
    
    fruit_btn3 = tk.Button(food_item_frame, image=fruit_images[2], width=104, height=104, bd=2, command=lambda:addItem('Fruit3', 3000))
    fruit_btn3.grid(row=3, column=2, pady=2)
    
    fruit_btn4 = tk.Button(food_item_frame, image=fruit_images[3], width=104, height=104, bd=2, command=lambda:addItem('Fruit4', 3000))
    fruit_btn4.grid(row=3, column=3, pady=2)
    
    fruit_btn5 = tk.Button(food_item_frame, image=fruit_images[4], width=104, height=104, bd=2, command=lambda:addItem('Fruit5', 1000))
    fruit_btn5.grid(row=3, column=4, pady=2)
    
    fruit_btn6 = tk.Button(food_item_frame, image=fruit_images[5], width=104, height=104, bd=2, command=lambda:addItem('Fruit1', 2000))
    fruit_btn6.grid(row=3, column=5, pady=2)

    return food_item_frame