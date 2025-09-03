import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for x in range(0,nr_letters)]
    password_list += [random.choice(symbols) for x in range(0,nr_symbols)]
    password_list += [random.choice(numbers) for x in range(0,nr_numbers)]

    random.shuffle(password_list)

    password = ''.join(password_list)

    password_entry.insert(0,password)

    pyperclip.copy(password)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password():
    website = (website_entry.get()).title()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="OOPS!", message="Data File not found!")
    else:
        if website in data:
            messagebox.showinfo(title=f"{website}", message=f"Email: {data[website]["email"]}\n "
                                                        f"Password: {data[website]["password"]}")
        else:
            messagebox.showwarning(title="OOPS!", message="No details for the website found!")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = (website_entry.get()).title()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email" : email,
            "password" : password,
    }}

    if website == "" or password == "":
        messagebox.showwarning(title="OOPS!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"You have entered:\n Email: {email}\n "
                                                                   f"Password: {password}\n Is it ok?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    #Read old data
                    data = json.load(file)

            except FileNotFoundError:
                with open("data.json", "w") as file:
                    # Saving new data
                    json.dump(obj=new_data, fp=file, indent=4)

            else:
                #Update old data with new data
                data.update(new_data)
                with open("data.json", "w") as file:
                    #Saving new data
                    json.dump(obj=data, fp=file, indent=4)

            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                email_entry.insert(0, "abc@gmail.com")
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

img = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100,100,image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=30)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = Button(text="Search", width=20, command=search_password)
search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=56)
email_entry.insert(0, "abc@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", width=20, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=50, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()