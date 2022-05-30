import tkinter


window = tkinter.Tk()

# Set window's title and default minimum size.
window.title('NguNgi PuPi')
window.minsize(width=400, height=750)
window.config(padx=60, pady=40)

# Label component.
my_label = tkinter.Label(text='they/them 😌💅🏻', font=('Arial', 24, 'bold'))

# In Tkinter, we have to specify how a component will be laid out
# in a window using a geometry management mechanicsm before it actually
# shows up. The 3 geometry managers are pack(), place(), and grid(); only
# one type of manager can be used within a single application.
my_label.grid(row=0, column=0)


# Button component.
def button_clicked():
    print("Clickity Clack, Go Back To Yo' Fuckin' Work!")
    my_label.config(text=input.get())


button = tkinter.Button(text='Try clicking me...', command=button_clicked)
button.grid(row=1, column=1)

new_button = tkinter.Button(text='Weee ~ !')
new_button.grid(row=0, column=2)

# Entry component (Tkinter input field).
input = tkinter.Entry(width=10)
input.grid(row=3, column=3)

# For the Tk module to work, Tk.mainloop() method must be at
# the end of the script.
window.mainloop()
