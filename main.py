import tkinter as tk
from tkinter import messagebox

# Function to parse and format the string
def parse_string():
    input_string = input_entry.get()

    # Check if the input is valid
    if not input_string:
        messagebox.showwarning("Input Error", "Please enter a valid string")
        return

    # Check if "allowableValues = ..." exists and remove it
    if "allowableValues" in input_string:
        # Remove the allowableValues = {...} part
        input_string = input_string.split('allowableValues = ')[-1]
        input_string = input_string.strip('{}')

    # Check if the input has double quotes and remove them
    if input_string.startswith('"') and input_string.endswith('"'):
        input_string = input_string[1:-1]

    # Split the input string by commas and strip spaces
    values = [val.strip() for val in input_string.split(',')]

    # Format the output string
    formatted_string = ', type="string", allowableValues = {' + ','.join(f'"{val}"' for val in values) + '}'

    # Display the result in the output box
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, formatted_string)

# Function to copy formatted output to clipboard
def copy_to_clipboard():
    formatted_text = output_text.get(1.0, tk.END).strip()  # Get the formatted text from the output box
    if formatted_text:
        window.clipboard_clear()  # Clear the clipboard
        window.clipboard_append(formatted_text)  # Append the formatted text to the clipboard
        messagebox.showinfo("Copied", "Formatted text has been copied to the clipboard")
    else:
        messagebox.showwarning("Copy Error", "No text to copy")

# GUI setup
window = tk.Tk()
window.title("String Parser")

# Input label and entry
input_label = tk.Label(window, text="Enter your allowableValues:")
input_label.pack(pady=10)

input_entry = tk.Entry(window, width=50)
input_entry.pack(pady=10)

# Parse button
parse_button = tk.Button(window, text="Parse String", command=parse_string)
parse_button.pack(pady=10)

# Output label
output_label = tk.Label(window, text="Formatted Output:")
output_label.pack(pady=10)

# Output text box
output_text = tk.Text(window, height=5, width=50)
output_text.pack(pady=10)

# Copy button
copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Start the GUI event loop
window.mainloop()
