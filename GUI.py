import tkinter as tk
from tkinter import ttk, filedialog
from transformers import pipeline
# Import Python Imaging Library for image manipulation and saving
from PIL import Image
# Import text to image generation class
from text_to_image import TextToImageGenerator
# Import background remover loader function
from background_remover import load_background_remover
pipe = load_background_remover()

# Initialize background remover pipeline

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

    # Text to image generation
    if aiSelect == "Text to Image" and inputType == "Text":
        # Remove the background remover image if it exists
        if backRemove is not None and backRemove.winfo_exists():
            destroyer(backRemove)
        # Check if the text input box exists and retrieve the prompt
        if textBox is not None and textBox.winfo_exists():
            prompt = textBox.get("1.0", tk.END).strip()
            # Continue if the prompt is not empty
            if prompt:
                generator = TextToImageGenerator()
                output_path = generator.generate_image(prompt)
                # Display the generated image if it's not already shown
                if textImage is None or not textImage.winfo_exists():
                    image1 = tk.PhotoImage(file=output_path)
                    textImage = tk.Label(tab1, image=image1)
                    textImage.image = image1
                    textImage.pack()
    # Image background removal
    elif aiSelect == "Background Remover" and inputType == "Image":
        # Remove the generated image from text to image, if it exists
        if textImage is not None and textImage.winfo_exists():
            destroyer(textImage)
        # Continue if a file has been selected
        if filepath:
            # Open the image and convert to RGB
            image = Image.open(filepath).convert("RGB")
            # Remove the background of the image using the ai model from the segmentation pipeline
            result = pipe(image)
            # Save the image
            output_path = "background_removed.png"
            result.save(output_path)
            # Display the processed image
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