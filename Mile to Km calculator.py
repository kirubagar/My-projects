import tkinter

"""function for mile to km conversion logic"""

def conversion():
    miles = float (user_input.get())
    km = miles * 1.60934
    result_label.config(text=f"{km:.2f}")

#window
window = tkinter.Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=150)
window.config(padx=10, pady=20)

#entry
user_input = tkinter.Entry(width=8)
print(user_input.get())
user_input.grid(row=0, column=1)


#label
my_label = tkinter.Label(text= "Miles", font=("Arial", 14, "bold"))
my_label.grid(row=0, column=2)

km_label = tkinter.Label(text="Km",font=("Arial", 14, "bold"))
km_label.grid(column=2, row=1)

equal_label = tkinter.Label(text = "is equal to", font=("Arial", 14, "bold"))
equal_label.grid(column=0, row=1)

result_label = tkinter.Label(text="0", font=("Arial", 14, "bold"))
result_label.grid(column=1, row=1)


#button
button = tkinter.Button(text= "calculate",width=10, command=conversion)
button.grid(column=1, row=2)


window.mainloop()