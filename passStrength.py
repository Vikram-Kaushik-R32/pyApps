import tkinter as tk
from tkinter import messagebox
import string
import math

# Function to check password strength
def check_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    # Calculate password strength score
    score = 0
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    # Determine strength level
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, score

# Function to estimate time to crack the password
def estimate_crack_time(password):
    length = len(password)
    combinations = 1

    if any(char.islower() for char in password):
        combinations *= len(string.ascii_lowercase)
    if any(char.isupper() for char in password):
        combinations *= len(string.ascii_uppercase)
    if any(char.isdigit() for char in password):
        combinations *= len(string.digits)
    if any(char in string.punctuation for char in password):
        combinations *= len(string.punctuation)

    # Assume 100 billion attempts per second (modern GPUs can do this)
    attempts_per_second = 100e9
    total_combinations = combinations ** length
    seconds = total_combinations / attempts_per_second

    return seconds

# Function to handle the check button click
def on_check_click():
    password = password_entry.get()
    strength, score = check_password_strength(password)
    crack_time_seconds = estimate_crack_time(password)
    crack_time_years = crack_time_seconds / (365 * 24 * 3600)

    result_text = f"Password Strength: {strength} (Score: {score}/5)\n"
    if crack_time_years > 1e9:
        result_text += "Estimated Time to Crack: More than a billion years"
    else:
        result_text += f"Estimated Time to Crack: {crack_time_years:.2e} years"

    result_label.config(text=result_text)

# Create the main application window
root = tk.Tk()
root.title("Password Strength Checker")

# Create and place the widgets
tk.Label(root, text="Enter Password:").grid(row=0, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show='*', width=30)
password_entry.grid(row=0, column=1, padx=10, pady=10)

check_button = tk.Button(root, text="Check Strength", command=on_check_click)
check_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Start the main application loop
root.mainloop()
