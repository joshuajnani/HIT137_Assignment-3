import tkinter as tk
from tkinter import ttk, filedialog
from transformers import pipeline
# Import Python Imaging Library for image manipulation and saving
from PIL import Image
# Import text to image generation class
from text_to_image import TextToImageGenerator
# Import background remover loader function
from background_remover import load_background_remover
# Initialize background remover pipeline
pipe = load_background_remover()
# Create the main application window
root = tk.Tk()
root.title("Basic Tkinter GUI")
root.geometry("500x800")
#ttk Styling
style = ttk.Style()
style.theme_use("clam") 
#Custom Styles
style.configure("TLabelFrame", font=("Arial", 11, "bold"), padding=10)
style.configure("TLabel", font=("Arial", 10))
style.configure("TButton", font=("Arial", 10, "bold"), padding=6)
style.configure("TCombobox", padding=5)
style.configure("TNotebook.Tab", font=("Arial", 10, "bold"), padding=[10, 5])

# Create tabs
Tabs = ttk.Notebook(root)

# TAB1
tab1 = ttk.Frame(Tabs)
# Row to keep input section inline
input_row = ttk.Frame(tab1)
input_row.pack(fill="x", padx=10, pady=6)

# Dropdown menu for input type
label5 = ttk.Label(input_row, text='Choose input type:')
label5.pack(side='left',padx =(0,8), pady=20)
title_label = tk.Label(tab1, text="File Processing Application", 
                       font=("Arial", 16, "bold"), fg="#2c3e50")
title_label.pack(before= label5, pady=15)
inputChoice = ['Text', 'Image']
dropdownChoice = ttk.Combobox(input_row, values=inputChoice)
dropdownChoice.pack(side='left')

# Destroy function to get rid of widgets when swapping
def destroyer(widget):
    widget.destroy()

# Initiate widget names
filepath = tk.StringVar(value="No file selected")
textBox = None
file_path = None
# File selector
def openFile():
    global filepath, file_path
    path = filedialog.askopenfilename()
    if path:
        filepath.set(path)
    file_path = path
#File Selection
#Frame to structure file selection
file_frame = ttk.LabelFrame(tab1, text="File Selection")
file_frame.pack(fill='x', padx=10, pady=10)
#Initiate widget names
file_label = None
fileButton = None

# Function to swap widgets depending on input type
def inputSelector():
    global fileButton, textBox, file_label
    inputType = dropdownChoice.get()
    if inputType == "Text":
        if fileButton is not None and fileButton.winfo_exists():
            destroyer(fileButton)
            destroyer(file_label)
            file_frame.pack_forget()
        if textBox is None or not textBox.winfo_exists():
            textBox = tk.Text(tab1, height=10, width=50)
            textBox.pack(after=input_row)
    elif inputType == "Image":
        if textBox is not None and textBox.winfo_exists():
            destroyer(textBox)
        if fileButton is None or not fileButton.winfo_exists():
            file_frame.pack(after=input_row, fill='x', padx=10, pady=10)
            file_label = tk.Label(file_frame, textvariable=filepath, width=50, anchor="w")
            file_label.pack(side="left", padx=5, pady=5)
            fileButton = ttk.Button(file_frame, text="Browse File", command=openFile)
            fileButton.pack(side="right", padx=5, pady=5)

# Confirm input type button
button3 = tk.Button(input_row, text="Confirm", command=inputSelector)
button3.pack(side='left')
# Row to keep AI section inline
ai_row = ttk.Frame(tab1)
ai_row.pack(fill="x", padx=10, pady=6)

# Dropdown menu for AI choice
label3 = ttk.Label(ai_row, text='Choose Processing Option:')
label3.pack(side = 'left', pady=20)
aiChoice = ['Text to Image', 'Background Remover']
dropdownAI = ttk.Combobox(ai_row, values=aiChoice)
dropdownAI.pack(side='left')

# Output display widgets
backRemove = None
textImage = None
image1 = None
errorLabel = None
# AI processing function
def AI_Selector():
    global backRemove, textImage, image1, filepath, file_path, errorLabel
    aiSelect = dropdownAI.get()
    inputType = dropdownChoice.get()

    # Text to image generation
    if aiSelect == "Text to Image" and inputType == "Text":
        # Remove the background remover image if it exists
        if backRemove is not None and backRemove.winfo_exists():
            destroyer(backRemove)
        if errorLabel is not None and errorLabel.winfo_exists():
            destroyer(errorLabel)
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
                    textImage = tk.Label(output_frame, image=image1)
                    textImage.image = image1
                    textImage.pack()
    # Image background removal
    elif aiSelect == "Background Remover" and inputType == "Image":
        # Remove the generated image from text to image, if it exists
        if textImage is not None and textImage.winfo_exists():
            destroyer(textImage)
        if errorLabel is not None and errorLabel.winfo_exists():
            destroyer(errorLabel)
        # Continue if a file has been selected
        if filepath:
            # Open the image and convert to RGB
            image = Image.open(file_path).convert("RGB")
            # Remove the background of the image using the ai model from the segmentation pipeline
            result = pipe(image)
            # Save the image
            output_path = "background_removed.png"
            result.save(output_path)
            # Display the processed image
            image1 = tk.PhotoImage(file=output_path)
            backRemove = tk.Label(output_frame, image=image1)
            backRemove.image = image1
            backRemove.pack()
    elif aiSelect == "Background Remover" and inputType == "Text":
        if backRemove is not None and backRemove.winfo_exists():
            destroyer(backRemove)
        if textImage is not None and textImage.winfo_exists():
            destroyer(textImage)
        errorLabel = tk.Label(output_frame, text = "Cannot use Background Remover with Text")
        errorLabel.pack()
    elif aiSelect == "Text to Image" and inputType == "Image":
        if backRemove is not None and backRemove.winfo_exists():
            destroyer(backRemove)
        if textImage is not None and textImage.winfo_exists():
            destroyer(textImage)
        errorLabel = tk.Label(output_frame, text = "Cannot use Text to Image with Image")
        errorLabel.pack()
# Confirm AI choice button
button = tk.Button(ai_row, text="Confirm", command=AI_Selector)
button.pack(side='left', pady=20)

#Output Section
output_frame = ttk.LabelFrame(tab1, text="Output")
output_frame.pack(fill='both', expand=True, padx=10, pady=10)

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
Tabs.add(tab1, text='Home')
Tabs.add(tab2, text='Explanation of OOP')
Tabs.add(tab3, text='Choice of AI Models')
Tabs.pack(expand=1, fill='both')

# Start the Tkinter event loop
root.mainloop()