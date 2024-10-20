import tkinter as tk
from tkinter import filedialog, Text

# Initialize the main window
root = tk.Tk()
root.title("Notepad App")

# Define the text area
text_area = Text(root, wrap="word")
text_area.pack(expand=True, fill="both")

# Function to open a file
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(1.0, file.read())

# Function to save the file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))

# Create the menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Add File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command(save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Run the application
root.mainloop()
