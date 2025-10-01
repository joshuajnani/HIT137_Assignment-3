from transformers import pipeline
from PIL import Image
import tkinter as tk
from tkinter import ttk, filedialog
from text_to_image import TextToImageGenerator

# Initialize background remover pipeline
pipe = pipeline("image-segmentation", model="briaai/RMBG-1.4", trust_remote_code=True)

# Create the main application window
root = tk.Tk()
root.title("Basic Tkinter GUI")
root.geometry("500x500")

# Create tabs
Tabs = ttk.Notebook(root)

# TAB1
tab1 = ttk.Frame(Tabs)

# Dropdown menu for input type
label = ttk.Label(tab1, text='Choose input type:')
label.pack(pady=20)
inputChoice = ['Text', 'Image']
dropdownChoice = ttk.Combobox(tab1, values=inputChoice)
dropdownChoice.pack()

# Destroy function to get rid of widgets when swapping
def destroyer(widget):
    widget.destroy()

# Initiate widget names
fileButton = None
textBox = None
filepath = None

# File selector
def openFile():
    global filepath
    filepath = filedialog.askopenfilename()
    label1.config(text=filepath)

# Function to swap widgets depending on input type
def inputSelector():
    global fileButton, textBox
    inputType = dropdownChoice.get()
    if inputType == "Text":
        if fileButton is not None and fileButton.winfo_exists():
            destroyer(fileButton)
        if textBox is None or not textBox.winfo_exists():
            textBox = tk.Text(tab1, height=10, width=50)
            textBox.pack(before=label3)
    elif inputType == "Image":
        if textBox is not None and textBox.winfo_exists():
            destroyer(textBox)
        if fileButton is None or not fileButton.winfo_exists():
            fileButton = tk.Button(tab1, text="Browse", command=openFile)
            fileButton.pack(before=label3)

# Confirm input type button
button = tk.Button(tab1, text="Confirm", command=inputSelector)
button.pack()

# Label to show selected file path
label1 = ttk.Label(tab1, text=filepath)
label1.pack(pady=20)

# Dropdown menu for AI choice
label3 = ttk.Label(tab1, text='Choose Processing Option:')
label3.pack(pady=20)
aiChoice = ['Text to Image', 'Background Remover']
dropdownAI = ttk.Combobox(tab1, values=aiChoice)
dropdownAI.pack()

# Output display widgets
backRemove = None
textImage = None
image1 = None

# AI processing function
def AI_Selector():
    global backRemove, textImage, image1
    aiSelect = dropdownAI.get()
    inputType = dropdownChoice.get()

    if aiSelect == "Text to Image" and inputType == "Text":
        if backRemove is not None and backRemove.winfo_exists():
            destroyer(backRemove)
        if textBox is not None and textBox.winfo_exists():
            prompt = textBox.get("1.0", tk.END).strip()
            if prompt:
                generator = TextToImageGenerator()
                output_path = generator.generate_image(prompt)
                if textImage is None or not textImage.winfo_exists():
                    image1 = tk.PhotoImage(file=output_path)
                    textImage = tk.Label(tab1, image=image1)
                    textImage.image = image1
                    textImage.pack()

    elif aiSelect == "Background Remover" and inputType == "Image":
        if textImage is not None and textImage.winfo_exists():
            destroyer(textImage)
        if filepath:
            image = Image.open(filepath).convert("RGB")
            result = pipe(image)  # result is already a PIL.Image
            output_path = "background_removed.png"
            result.save(output_path)
            image1 = tk.PhotoImage(file=output_path)
            backRemove = tk.Label(tab1, image=image1)
            backRemove.image = image1
            backRemove.pack()

# Confirm AI choice button
button = tk.Button(tab1, text="Confirm", command=AI_Selector)
button.pack(pady=20)

# TAB2
tab2 = ttk.Frame(Tabs)
with open("OOP.txt", "r") as file:
    oop = file.read()
label = ttk.Label(tab2, text="Explanation of OOP")
label.pack(pady=20)
label = ttk.Label(tab2, text=oop)
label.pack(pady=20)

# TAB3
tab3 = ttk.Frame(Tabs)
with open("AI_Models.txt", "r") as file:
    aiModels = file.read()
label = ttk.Label(tab3, text='Choice of AI Models')
label.pack(pady=20)
label = ttk.Label(tab3, text=aiModels)
label.pack(pady=20)

# Add tabs to notebook
Tabs.add(tab1, text='Tab 1')
Tabs.add(tab2, text='Tab 2')
Tabs.add(tab3, text='Tab 3')
Tabs.pack(expand=1, fill='both')

# Start the Tkinter event loop
root.mainloop()