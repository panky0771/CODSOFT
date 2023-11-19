import tkinter as tk
from tkinter import ttk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stylish Calculator")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        # Entry for displaying the result
        result_entry = ttk.Entry(root, textvariable=self.result_var, font=('Helvetica', 18), justify="right", state="readonly", width=20)
        result_entry.grid(row=0, column=0, columnspan=4, sticky="nsew", ipadx=8, ipady=8)

        # Style for the buttons
        style = ttk.Style()
        style.configure("TButton", font=('Helvetica', 12), padding=5)

        # Buttons for digits and operations
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', 'AC'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            ttk.Button(root, text=button, command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configure row and column weights for flexibility
        for i in range(1, 6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def button_click(self, button):
        current_text = self.result_var.get()

        if button.isdigit() or button == '.':
            # Append digit or decimal point
            if current_text == '0':
                self.result_var.set(button)
            else:
                self.result_var.set(current_text + button)
        elif button == '=':
            # Evaluate the expression
            try:
                result = eval(current_text)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif button == 'C':
            # Backspace
            if len(current_text) > 1:
                self.result_var.set(current_text[:-1])
            else:
                self.result_var.set("0")
        elif button == 'AC':
            # All Clear
            self.result_var.set("0")
        else:
            # Append operator
            self.result_var.set(current_text + button)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
