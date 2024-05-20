import tkinter as tk
import time
import random

def get_random_color():
    """Generates a random color in hex format."""
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def update_time():
    """Updates the time displayed on the clock."""
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)  # update every second

def change_color():
    """Changes the background color of the clock."""
    new_color = get_random_color()
    clock_label.config(bg=new_color)
    root.after(30000, change_color)  # change color every 30 seconds

# Set up the main application window
root = tk.Tk()
root.title("Digital Clock with Random Color Change")

# Create and configure the clock label
clock_label = tk.Label(root, font=('Arial', 48), fg='white', bg='black')
clock_label.pack(expand=True)

# Initialize the time and color change functions
update_time()
change_color()

# Start the tkinter event loop
root.mainloop()

