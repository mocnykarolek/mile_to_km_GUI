from tkinter import *

def calculate():
    miles = input_miles.get()
    km = round(int(miles) * 1.6, 2)
    km_answer.config(text=km)


window = Tk()
window.title("mile to km converter")
window.config(padx=10, pady=10)
input_miles = Entry(width=10)
input_miles.grid(row=0, column=1)
input_miles.insert(END, "0")
input_miles.focus()

label_miles = Label(text="miles")
label_miles.grid(row=0, column=2)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

km_answer = Label(text=0)
km_answer.grid(row=1, column=1)

km_label = Label(text="km")
km_label.grid(row=1, column=2)

button = Button(text="calculate", command=calculate)
button.grid(row=2, column=1)


window.mainloop()