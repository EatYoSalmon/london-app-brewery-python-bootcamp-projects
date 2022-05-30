import tkinter as tk


window = tk.Tk()
window.title('Mile to Km Converter')
window.config(padx=30, pady=30)

miles_input = tk.Entry(width=10)
miles_input.grid(row=0, column=1)

result = tk.Label(text='0')
result.grid(row=1, column=1)


def calculate():
    miles = float(miles_input.get())
    km = str(round(miles * 1.60934, 2))
    result.config(text=km)


calc_button = tk.Button(text='Calculate', command=calculate)
calc_button.grid(row=2, column=1)

miles_label = tk.Label(text='Miles')
miles_label.grid(row=0, column=2)

equal_label = tk.Label(text='is equal to')
equal_label.grid(row=1, column=0)

km_label = tk.Label(text='Km')
km_label.grid(row=1, column=2)

window.mainloop()
