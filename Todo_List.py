import tkinter as tk
from tkinter import ttk, messagebox

TODO_FILE = "todo.txt"
BG_COLOR = "#F0F0F0"  # Light gray background color
BUTTON_COLOR = "#4CAF50"  # Green color for buttons
TEXT_COLOR = "#000000"  # Black text color
LISTBOX_COLOR = "#FFFFFF"  # White color for the listbox

def view_todo_list():
    try:
        with open(TODO_FILE, "r") as file:
            tasks = file.readlines()
            return tasks
    except FileNotFoundError:
        return []

def add_task(task_entry, tree, root):
    task = task_entry.get()
    if task:
        with open(TODO_FILE, "a") as file:
            file.write(f"{task}\n")
        
        # Show the table if it's not visible
        if not tree.winfo_ismapped():
            tree.pack(expand=True, fill=tk.BOTH)
        
        tree.insert("", tk.END, values=(len(tree.get_children()) + 1, task))
        task_entry.delete(0, tk.END)  # Clear the entry widget
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def mark_as_done(tree):
    selected_task_index = tree.selection()
    if selected_task_index:
        for item in selected_task_index:
            done_task = tree.item(item, "values")[1]
            tasks = view_todo_list()
            tasks.remove(f"{done_task}\n")
            with open(TODO_FILE, "w") as file:
                file.writelines(tasks)
            tree.delete(item)
        messagebox.showinfo("Task Completed", "Selected task(s) marked as done.")
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as done.")

def update_task(task_entry, tree):
    selected_task_index = tree.selection()
    if selected_task_index:
        for item in selected_task_index:
            updated_task = task_entry.get()
            if updated_task:
                tasks = view_todo_list()
                old_task = tree.item(item, "values")[1]
                tasks.remove(f"{old_task}\n")
                tasks.append(f"{updated_task}\n")
                with open(TODO_FILE, "w") as file:
                    file.writelines(tasks)
                tree.item(item, values=(tree.item(item, "values")[0], updated_task))
                task_entry.delete(0, tk.END)
                messagebox.showinfo("Task Updated", "Task successfully updated.")
            else:
                messagebox.showwarning("Warning", "Please enter a task.")
    else:
        messagebox.showwarning("Warning", "Please select a task to update.")

def create_gui():
    root = tk.Tk()
    root.title("To-Do List App")
    root.configure(bg=BG_COLOR)

    # Create and set up the entry widget
    task_entry = tk.Entry(root, width=30, bg=LISTBOX_COLOR, fg=TEXT_COLOR)
    task_entry.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.X, expand=True)

    # Create and set up buttons
    add_button = ttk.Button(root, text="Add Task", cursor="hand2", command=lambda: add_task(task_entry, tree, root))
    add_button.pack(pady=10, padx=5, side=tk.LEFT, fill=tk.X, expand=True)
    
    done_button = ttk.Button(root, text="Mark as Done", cursor="hand2", command=lambda: mark_as_done(tree))
    done_button.pack(pady=10, padx=5, side=tk.LEFT, fill=tk.X, expand=True)

    update_button = ttk.Button(root, text="Update Task", cursor="hand2", command=lambda: update_task(task_entry, tree))
    update_button.pack(pady=10, padx=5, side=tk.LEFT, fill=tk.X, expand=True)

    # Create and set up the table (Treeview widget)
    columns = ("Index", "Task")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    tree.heading("Index", text="Index")
    tree.heading("Task", text="Task")
    tree["displaycolumns"] = ("Index", "Task")
    tree.column("Index", anchor=tk.CENTER, width=50)
    tree.column("Task", anchor=tk.CENTER, width=200)
    tree.pack_forget()  # Hide the table initially

    # Configure row and column weights for flexibility
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Configure themed button style
    style = ttk.Style()
    style.configure('TButton', background=BUTTON_COLOR, foreground=TEXT_COLOR, font=('Helvetica', 10))

    root.mainloop()

if __name__ == "__main__":
    create_gui()
