import tkinter as tk
from tkinter import ttk

# Main window
window = tk.Tk()
window.title("Modern Calculator")
window.geometry("340x460")
window.resizable(False, False)

# Styling
style = ttk.Style(window)
style.theme_use('default')

# Configure button style
style.configure("TButton",
    font=("Segoe UI", 14),
    padding=10,
    relief="flat",
    borderwidth=0,
    background="#f0f0f0",
    foreground="#333"
)

style.map("TButton",
    background=[("active", "#e0e0e0")],
    foreground=[("disabled", "#888")]
)

# Expression storage
expression = ""

# Entry widget
entry_var = tk.StringVar()
entry = ttk.Entry(window, textvariable=entry_var, font=('Segoe UI', 26), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipadx=5, ipady=10, sticky="nsew")

# Event handlers
def press(symbol):
    global expression
    expression += str(symbol)
    entry_var.set(expression)

def calculate(event=None):
    global expression
    try:
        result = str(eval(expression))
        entry_var.set(result)
        expression = result
    except:
        entry_var.set("Error")
        expression = ""

def clear(event=None):
    global expression
    expression = ""
    entry_var.set("")

# Button layout
buttons = [
    ('7', 1, 0, "#FFD966"), ('8', 1, 1, "#FFD966"), ('9', 1, 2, "#FFD966"), ('/', 1, 3, "#F4CCCC"),
    ('4', 2, 0, "#FFE599"), ('5', 2, 1, "#FFE599"), ('6', 2, 2, "#FFE599"), ('*', 2, 3, "#F4CCCC"),
    ('1', 3, 0, "#B6D7A8"), ('2', 3, 1, "#B6D7A8"), ('3', 3, 2, "#B6D7A8"), ('-', 3, 3, "#F4CCCC"),
    ('0', 4, 0, "#A4C2F4"), ('.', 4, 1, "#A4C2F4"), ('=', 4, 2, "#76A5AF"), ('+', 4, 3, "#F4CCCC"),
    ('C', 5, 0, "#E06666"),
]

# Create buttons
for (text, row, col, color) in buttons:
    if text == '=':
        btn = ttk.Button(window, text=text, command=calculate)
    elif text == 'C':
        btn = ttk.Button(window, text=text, command=clear)
        btn.grid(row=row, column=col, columnspan=4, sticky="nsew", padx=5, pady=5, ipadx=5)
        btn.configure(style="TButton")
        btn.configure(style="TButton")
        btn.configure(style="TButton")
        btn.configure(style="TButton")
        window.grid_rowconfigure(row, weight=1)
        continue
    else:
        btn = ttk.Button(window, text=text, command=lambda t=text: press(t))

    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    btn_style = ttk.Style()
    style_name = f"{text}.TButton"
    btn_style.configure(style_name, background=color, foreground="black", font=("Segoe UI", 14), borderwidth=1, relief="flat")
    btn.configure(style=style_name)

# Make layout expandable
for i in range(6):
    window.grid_rowconfigure(i, weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

# Keyboard bindings
window.bind("<Return>", calculate)
window.bind("<BackSpace>", lambda e: clear())
window.bind("<Escape>", lambda e: clear())
window.bind("<Key>", lambda e: press(e.char) if e.char in "0123456789+-*/.=" else None)

window.mainloop()
