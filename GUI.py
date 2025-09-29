
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
#Create the main application window
root = tk.Tk()
root.title("Basic Tkinter GUI") # Set the window title
root.geometry("500x500") # Set the window size (width x height)
#Create tabs
Tabs = ttk.Notebook(root)

#TAB1
tab1 = ttk.Frame(Tabs)
#Dropdown menu for input type
label = ttk.Label(tab1, text = 'Choose input type:')
label.pack(pady=20)
inputChoice = ['Text','Image']
dropdownChoice = ttk.Combobox(tab1,values=inputChoice)
dropdownChoice.pack()

#Destroy function to get rid of widgets when swapping
def destroyer(widget):
        widget.destroy()
#Initiate widget names
fileButton = None
textBox = None
#Function to swap widgets(text box or file browse button) depending what input type is chosen
def inputSelector():
        global fileButton, textBox
        inputType = dropdownChoice.get()
        if inputType == "Text":
                if fileButton is not None and fileButton.winfo_exists(): #Destroy other widget on clicking confirm, if it exists
                        destroyer(fileButton)
                if textBox is None or not textBox.winfo_exists(): #Create widget if there current widget doesn't exists
                        textBox = tk.Text(tab1,height=10, width=50)
                        textBox.pack(before=label3)
        elif inputType == "Image":
                if textBox is not None and textBox.winfo_exists():
                        destroyer(textBox)
                if fileButton is None or not fileButton.winfo_exists():
                        fileButton = tk.Button(tab1, text = "Browse", command = openFile)
                        fileButton.pack(before=label3)
        else:
                return
#Button to confirm choice for input type
button = tk.Button(tab1, text = "Confirm", command = inputSelector)
button.pack()
#File selector
filepath = None
def openFile():
        filepath = filedialog.askopenfilename()
        label1.config(text = filepath)
label1 = ttk.Label(tab1, text = filepath)
label1.pack(pady=20)
#Dropdown menu for AI choice
label3 = ttk.Label(tab1, text = 'Choose Processing Option:')
label3.pack(pady=20)
aiChoice = ['Text to Image', 'Background Remover']
dropdownAI = ttk.Combobox(tab1,values=aiChoice)
dropdownAI.pack()
#Choose what output to display
backRemove=None
textImage=None
image1=None
def AI_Selector():
        global backRemove, textImage, image1
        aiSelect = dropdownAI.get()
        if aiSelect == "Text to Image":
                if backRemove is not None and backRemove.winfo_exists(): #Destroy other widget on clicking confirm, if it exists
                        destroyer(backRemove)
                if textImage is None or not textImage.winfo_exists(): #Create widget if there current widget doesn't exists
                        image1 = tk.PhotoImage(file = "output.png")
                        textImage = tk.Label(tab1, image=image1)
                        textImage.pack()
        elif aiSelect == "Background Remover":
                if textImage is not None and textImage.winfo_exists():
                        destroyer(textImage)
                if backRemove is None or not backRemove.winfo_exists():
                        image1 = tk.PhotoImage(file = "output.png")
                        backRemove = tk.Label(tab1, image=image1)
                        backRemove.pack()
        else:
                return
#Function to retrieve choices after a button is pressed
def confirm_button_action():    
        type = dropdownChoice.get()
        ai = dropdownAI.get()
#Button to confirm choice and proceed
button = tk.Button(tab1, text = "Confirm", command=AI_Selector)
button.pack(pady=20)

#TAB2
tab2 = ttk.Frame(Tabs)
label = ttk.Label(tab2, text = 'Explaination of OOP')
label.pack(pady=20)
label = ttk.Label(tab2, text = 'insert text here')
label.pack(pady=20)
#TAB3
tab3 = ttk.Frame(Tabs)
label = ttk.Label(tab3, text = 'Choice of AI Models')
label.pack(pady=20)
label = ttk.Label(tab3, text = 'insert text here')
label.pack(pady=20)

Tabs.add(tab1, text ='Tab 1')
Tabs.add(tab2, text ='Tab 2')
Tabs.add(tab3, text ='Tab 3')
Tabs.pack(expand = 1,fill='both')

#Start the Tkinter event loop
root.mainloop()