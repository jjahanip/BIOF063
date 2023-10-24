import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Function to handle button clicks
def button_click(event):
    current = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif text == "C":
        entry.delete(0, tk.END)

    else:
        entry.insert(tk.END, text)

# Create a tkinter window
root = tk.Tk()
root.title("Calculator")

# Load and display a logo from a URL
logo_url = "https://www.nih.gov/sites/default/files/about-nih/2012-logo.png"  # Replace with your logo URL
response = requests.get(logo_url)
if response.status_code == 200:
    logo_data = BytesIO(response.content)
    logo_image = Image.open(logo_data)
    logo_photo = ImageTk.PhotoImage(logo_image)

    # Create a label widget to display the logo
    logo_label = tk.Label(root, image=logo_photo)
    logo_label.grid(row=0, column=0, columnspan=4)
    logo_label.image = logo_photo

# Create an entry widget for displaying the input and results
entry = tk.Entry(root, font=("Helvetica", 20))
entry.grid(row=1, column=0, columnspan=4)

# Define the calculator buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create a dictionary to store button widgets
button_widgets = {}

# Create and place the calculator buttons on the grid
row_val = 2
col_val = 0

for button_text in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=20, font=("Helvetica", 16))
    button.grid(row=row_val, column=col_val)
    col_val += 1

    if col_val > 3:
        col_val = 0
        row_val += 1

    # Store the button widget in the dictionary with the button text as the key
    button_widgets[button_text] = button

# Bind button click events to the button_click function using the dictionary
for button_text, button in button_widgets.items():
    button.bind("<Button-1>", button_click)

# Start the tkinter main loop
root.mainloop()
