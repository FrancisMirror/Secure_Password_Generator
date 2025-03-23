import tkinter as tk
import random
import string
import pyperclip
import os
import sys

# Función para que el icono funcione dentro del .exe generado por PyInstaller
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # Carpeta temporal de PyInstaller
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# ----------------------
# Password generation logic
# ----------------------
def generate_password():
    length = length_slider.get()
    characters = ""

    if var_upper.get():
        characters += string.ascii_uppercase
    if var_lower.get():
        characters += string.ascii_lowercase
    if var_numbers.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation

    if not characters:
        result.set("Select at least one option")
        return

    password = "".join(random.choice(characters) for _ in range(length))
    result.set(password)

# ----------------------
# Copy to clipboard
# ----------------------
def copy_password():
    password = result.get()
    if password and password != "Select at least one option":
        pyperclip.copy(password)
        result.set("Password copied!")

# ----------------------
# Main interface
# ----------------------
window = tk.Tk()
window.title("Secure Password Generator")
window.geometry("400x500")
window.configure(bg="black")
window.iconbitmap(resource_path("icono.ico"))

# Symbol + Title
title_symbol = tk.Label(window, text="🔐", font=("Arial", 20), fg="#00ee00", bg="black")
title_symbol.pack(pady=(15, 0))

title_text = tk.Label(window, text="Secure Password Generator", font=("Arial", 16, "bold"), bg="black", fg="white")
title_text.pack(pady=(0, 15))

# Length slider
tk.Label(window, text="Length", bg="black", fg="white").pack()
length_slider = tk.Scale(window, from_=4, to=40, orient="horizontal", bg="black", fg="#00ee00", highlightbackground="black")
length_slider.set(12)
length_slider.pack(pady=10)

# Checkboxes
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

tk.Checkbutton(window, text="Include Uppercase", variable=var_upper, bg="black", fg="white", selectcolor="black").pack(anchor="w", padx=20)
tk.Checkbutton(window, text="Include Lowercase", variable=var_lower, bg="black", fg="white", selectcolor="black").pack(anchor="w", padx=20)
tk.Checkbutton(window, text="Include Numbers", variable=var_numbers, bg="black", fg="white", selectcolor="black").pack(anchor="w", padx=20)
tk.Checkbutton(window, text="Include Symbols", variable=var_symbols, bg="black", fg="white", selectcolor="black").pack(anchor="w", padx=20)

# Generate button
tk.Button(window, text="Generate Password", command=generate_password, bg="#00ee00", fg="black", font=("Arial", 12, "bold")).pack(pady=20)

# Result display
result = tk.StringVar()
tk.Entry(window, textvariable=result, font=("Courier", 12), justify="center", width=30).pack(pady=10)

# Copy button
tk.Button(window, text="📋 Copy to Clipboard", command=copy_password, bg="gray", fg="white").pack(pady=10)

# Run the app
window.mainloop()