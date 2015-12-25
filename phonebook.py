import io
import base64
import tkinter as tk

root = tk.Tk()
root.title("Phonebook")

# a little more than width and height of image
w = 530
h = 580

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

x = (sw - w)/2
y = (sh - h)/2 - 40

# use width x height + x_offset + y_offset (no spaces!)
root.geometry("%dx%d+%d+%d" % (w, h, x, y))

image1 = tk.PhotoImage(file = 'images/contact_add.gif')
image2 = tk.PhotoImage(file = 'images/contact_search.gif')
image3 = tk.PhotoImage(file = 'images/contact_list.gif')
image4 = tk.PhotoImage(file = 'images/contact_group.gif')
image5 = tk.PhotoImage(file = 'images/contact_favorite.gif')

# create a white canvas
cv = tk.Canvas(bg='white')
cv.pack(side='top', fill='both', expand='yes')

# put the image on the canvas with
# create_image(xpos, ypos, image, anchor)
cv.create_image(5, 5, image=image1, anchor='nw')
cv.create_image(110, 5, image=image2, anchor='nw')
cv.create_image(215, 5, image=image3, anchor='nw')
cv.create_image(320, 5, image=image4, anchor='nw')
cv.create_image(425, 5, image=image5, anchor='nw')
root.mainloop()