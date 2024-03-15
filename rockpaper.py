# from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk  # Import Image and ImageTk modules from PIL

# The main application window
root = tk.Tk()
root.title("Display Image with Tkinter")

# Background image file
image_path = "Rock.png"
image = Image.open(image_path)
# Resize the image to fit the window
resized_image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
tk_image = ImageTk.PhotoImage(resized_image)
# Create a label widget to display the resized image
label = tk.Label(root, image=tk_image)
label.pack(fill=tk.BOTH, expand=True)  # Fill the entire window with the image

#lets play label
b=tk.Button(root,text="L e t s   P l a y!",bd=0,bg="plum",fg="#BDFCC9",font=("Bold",25),width=25,)
b.place(x=983,y=650)



# Run the Tkinter event loop
root.mainloop()
