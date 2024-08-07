import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to handle the generate button click
def on_generate_click():
    try:
        # Get the password length from the entry widget
        length = int(length_entry.get())
        if length < 1:
            raise ValueError("Length must be a positive integer")
        # Generate the password
        password = generate_password(length)
        # Display the password in the password entry widget
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError as ve:
        # Display an error message if the length is not valid
        messagebox.showerror("Invalid Input", str(ve))

# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Create and place the widgets
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=on_generate_click)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

tk.Label(root, text="Generated Password:").grid(row=2, column=0, padx=10, pady=10)
password_entry = tk.Entry(root)
password_entry.grid(row=2, column=1, padx=10, pady=10)

# Start the main application loop
root.mainloop()
