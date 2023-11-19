import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.password_var.set("Generated Password")

        ttk.Label(root, text="Add Username:").grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.username_entry = ttk.Entry(root, textvariable=self.username_var)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        ttk.Label(root, text="Password Length:").grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.length_entry = ttk.Entry(root, width=5)
        self.length_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=2, column=0, columnspan=2, pady=10)

        accept_button = ttk.Button(root, text="Accept", command=self.save_password)
        accept_button.grid(row=3, column=0, columnspan=2, pady=10)

        show_passwords_button = ttk.Button(root, text="Show Passwords", command=self.show_passwords)
        show_passwords_button.grid(row=4, column=0, columnspan=2, pady=10)

        reset_button = ttk.Button(root, text="Reset", command=self.reset)
        reset_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.password_label = ttk.Label(root, textvariable=self.password_var, font=('Helvetica', 14))
        self.password_label.grid(row=6, column=0, columnspan=2, pady=10)

        self.saved_passwords = []

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            
            characters = string.ascii_letters + string.digits + string.punctuation
            generated_password = ''.join(random.choice(characters) for _ in range(length))

            self.password_var.set(f"Generated Password: {generated_password}")
        except ValueError as e:
            self.password_var.set(str(e))

    def reset(self):
        self.username_var.set("")
        self.length_entry.delete(0, "end")
        self.password_var.set("Generated Password")

    def save_password(self):
        username = self.username_var.get()
        generated_password = self.password_var.get().split(": ")[1]

        if username and generated_password:
            self.saved_passwords.append({"username": username, "password": generated_password})
            print(f"Password saved: Username: {username}, Password: {generated_password}")
        else:
            print("Cannot save. Username or Password is empty.")

    def show_passwords(self):
        passwords_window = tk.Toplevel(self.root)
        passwords_window.title("Saved Passwords")

        tree = ttk.Treeview(passwords_window, columns=("Username", "Password"), show="headings")
        tree.heading("Username", text="Username")
        tree.heading("Password", text="Password")

        for password in self.saved_passwords:
            tree.insert("", "end", values=(password["username"], password["password"]))

        tree.pack(expand=True, fill="both")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
