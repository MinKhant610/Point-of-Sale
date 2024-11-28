import tkinter as tk 
from tkinter import ttk 

def receiptFrame(data_frame_left_cover):
    receipt_frame = tk.Frame(
        data_frame_left_cover,
        bd=3,
        width=200,
        height=400,
        pady=5,
        padx=1,
        relief='ridge',
        bg='#ffffff'
    )
    receipt_frame.pack(side='right')

    scroll_y = tk.Scrollbar(receipt_frame, orient='vertical')
    pos_record = ttk.Treeview(receipt_frame, height=20, columns=(
        'Item', 'Qty', 'Amount'
    ), yscrollcommand=scroll_y.set)
    scroll_y.pack(side='right', fill='y')

    pos_record.heading('Item', text='Item')
    pos_record.heading('Qty', text='Qty')
    pos_record.heading('Amount', text='Amount')

    pos_record['show'] = 'headings'
    pos_record.column('Item', width=120)
    pos_record.column('Qty', width=100)
    pos_record.column('Amount', width=100)
    pos_record.pack(fill='both', expand=1)

    pos_record.bind('<ButtonRelease-1>')
    text_receipt = tk.Text(receipt_frame, width=90, height=2, font=('Helvetica', 6, 'bold'))
    text_receipt.pack()
    text_receipt.insert('end', 'Item\t\t\t\t Qty\t\t\t\t Amount\t\n')

    return receipt_frame
