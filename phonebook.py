import io
import base64
import tkinter as tk
from tkinter import *

def f_init_window():
    root.title("Phonebook")
    root.resizable(0, 0)
    
    # a little more than width and height of image
    w = 520
    h = 580

    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()

    x = (sw - w)/2
    y = (sh - h)/2 - 40

    # use width x height + x_offset + y_offset (no spaces!)
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))

def f_main_frame():
    main_frame = tk.Frame(root)
    main_frame.grid(row = 1, pady = (20, 20))
    return main_frame

def f_add(event):
    add_frame = main_frame
    
    label_heading = Label(add_frame, text = "Add New Contact", font=(16))
    label_heading.grid(row = 0, column = 0, columnspan=2)
    
    label_first_name = Label(add_frame, text = "First Name")
    label_first_name.grid(row = 1, column = 0, padx=(0, 30))
    entry_first_name = Entry(add_frame)
    entry_first_name.grid(row = 1, column = 1)

    label_last_name = Label(add_frame, text = "Last Name")
    label_last_name.grid(row = 2, column = 0, padx=(0, 30))
    entry_last_name = Entry(add_frame)
    entry_last_name.grid(row = 2, column = 1)
    
    label_mobile = Label(add_frame, text = "Mobile")
    label_mobile.grid(row = 3, column = 0, padx=(0, 30))
    entry_mobile = Entry(add_frame)
    entry_mobile.grid(row = 3, column = 1)

    label_phone = Label(add_frame, text = "Phone")
    label_phone.grid(row = 4, column = 0, padx=(0, 30))
    entry_phone = Entry(add_frame)
    entry_phone.grid(row = 4, column = 1)

    label_address = Label(add_frame, text = "Address")
    label_address.grid(row = 5, column = 0, padx=(0, 30))
    entry_address = Entry(add_frame)
    entry_address.grid(row = 5, column = 1)

    label_email = Label(add_frame, text = "Email")
    label_email.grid(row = 6, column = 0, padx=(0, 30))
    entry_email = Entry(add_frame)
    entry_email.grid(row = 6, column = 1)

    label_additional1 = Label(add_frame, text = "Additional1")
    label_additional1.grid(row = 7, column = 0, padx=(0, 30))
    entry_additional1 = Entry(add_frame)
    entry_additional1.grid(row = 7, column = 1)

    label_additional2 = Label(add_frame, text = "Additional2")
    label_additional2.grid(row = 8, column = 0, padx=(0, 30))
    entry_additional2 = Entry(add_frame)
    entry_additional2.grid(row = 8, column = 1)

    label_group = Label(add_frame, text = "Group")
    label_group.grid(row = 9, column = 0, padx=(0, 30))
    entry_group = Entry(add_frame)
    entry_group.grid(row = 9, column = 1)

    label_remarks = Label(add_frame, text = "Remarks")
    label_remarks.grid(row = 10, column = 0, padx=(0, 30))
    entry_remarks = Entry(add_frame)
    entry_remarks.grid(row = 10, column = 1)

def f_search(event):
    print("test")

def f_list(event):
    print("test")

def f_group(event):
    print("test")

def f_favorite(event):
    print("test")
   
def f_toolbar():
    toolbar = tk.Frame(root)
    toolbar.grid(row = 0)
    
    image1 = tk.PhotoImage(file = 'images/contact_add.gif')
    image2 = tk.PhotoImage(file = 'images/contact_search.gif')
    image3 = tk.PhotoImage(file = 'images/contact_list.gif')
    image4 = tk.PhotoImage(file = 'images/contact_group.gif')
    image5 = tk.PhotoImage(file = 'images/contact_favorite.gif')
        
    label1 = Label(toolbar, image = image1)
    label1.image = image1 # keep a reference!
    label1.grid(row = 0, column = 0)
    
    label2 = Label(toolbar, image = image2)
    label2.image = image2 # keep a reference!
    label2.grid(row = 0, column = 1)
    
    label3 = Label(toolbar, image = image3)
    label3.image = image3 # keep a reference!
    label3.grid(row = 0, column = 2)
    
    label4 = Label(toolbar, image = image4)
    label4.image = image4 # keep a reference!
    label4.grid(row = 0, column = 3)
    
    label5 = Label(toolbar, image = image5)
    label5.image = image5 # keep a reference!
    label5.grid(row = 0, column = 4)
    
    label1.bind('<Button-1>', f_add)
    label2.bind('<Button-1>', f_search)
    label3.bind('<Button-1>', f_list)
    label4.bind('<Button-1>', f_group)
    label5.bind('<Button-1>', f_favorite)

root = tk.Tk()
f_init_window()
main_frame = f_main_frame()
f_toolbar()
root.mainloop()
