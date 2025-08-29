import tkinter

# def add(*args):
#     sum_of_numbers= 0
#     for n in args:
#         sum_of_numbers += n
#
#     return sum_of_numbers
#
#
# sum = add(2, 3, 4)
#
# print(sum)

def button_clicked():
    label.config(text="Button clicked")
    label.config(text=input.get())

window = tkinter.Tk()
window.title("GUI program")
window.minsize(width=500, height=300)

label = tkinter.Label(text="This is a label")
# label.config(text="New text")
# label["text"] = "New text"
label.grid(column=0, row=0)

button = tkinter.Button()
button.config(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button()
new_button.config(text="New Button")
new_button.grid(column=2, row=0)

input = tkinter.Entry()
input.config(width=10)
input.grid(column=3, row = 2)


window.mainloop()
