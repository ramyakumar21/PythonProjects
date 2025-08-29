import tkinter

def calculate():
    ans = round(float(user_input.get()) * 1.609, 3)
    output_label.config(text=ans)

window = tkinter.Tk()
window.title("Miles to Km convertor")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

user_input = tkinter.Entry()
user_input.config(width=5)
user_input.insert(string="0", index=tkinter.END)
user_input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

equal = tkinter.Label(text="is equal to")
equal.grid(column=0, row=1)

output_label = tkinter.Label(text="0")
output_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

calc = tkinter.Button(text="Calculate", command=calculate)
calc.grid(column=1, row= 2)

window.mainloop()
