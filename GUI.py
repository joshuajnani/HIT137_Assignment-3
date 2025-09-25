import tkinter as tk
from tkinter import ttk
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
inputChoice = ['Text','Audio','Image','Video']
dropdownChoice = ttk.Combobox(tab1,values=inputChoice)
dropdownChoice.pack()
#Dropdown menu for AI choice
label = ttk.Label(tab1, text = 'Choose Processing Option:')
label.pack(pady=20)
aiChoice = ['TO','BE','ADDED','LATER']
dropdownAI = ttk.Combobox(tab1,values=aiChoice)
dropdownAI.pack()
#Function to retrieve choices after a button is pressed
def my_button_action():    
        type = dropdownChoice.get()
        ai = dropdownAI.get()
#Button to confirm choice and proceed
button = tk.Button(tab1, text = "Confirm", command=my_button_action)
button.pack(pady=20)

#TAB2
tab2 = ttk.Frame(Tabs)
label = ttk.Label(tab2, text = 'Explaination of OOP')
label.pack(pady=20)
#TAB3
tab3 = ttk.Frame(Tabs)
label = ttk.Label(tab3, text = 'Choice of AI Models')
label.pack(pady=20)

Tabs.add(tab1, text ='Tab 1')
Tabs.add(tab2, text ='Tab 2')
Tabs.add(tab3, text ='Tab 3')
Tabs.pack(expand = 1,fill='both')

#Start the Tkinter event loop
root.mainloop()