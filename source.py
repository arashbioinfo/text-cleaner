import tkinter as tk
import pyperclip

def clean_text():
    copied_text = pyperclip.paste()
    cleaned_text = ' '.join(copied_text.splitlines())
    pyperclip.copy(cleaned_text)
    result_label.config(text="Text cleaned and copied to clipboard! \n"
                        "[This app is made by @bioinfmatters]")

# Create the main window
window = tk.Tk()
window.title("Text Cleaner")

# Create the text label
text_label = tk.Label(window, text= "Click the button to clean text from clipboard:")
text_label.pack()

# Create the clean button
clean_button = tk.Button(window, text="Clean", command=clean_text)
clean_button.pack()

# Create the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Run the main window event loop
window.mainloop()
