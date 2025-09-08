import pandas
import random
from tkinter import *
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
TIMER = 3000
new_word = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/tamil_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_word():
    global new_word, flip_card
    window.after_cancel(id=flip_card)
    new_word = random.choice(to_learn)
    canvas.itemconfig(card_image, image=front_image)
    canvas.itemconfig(title_text, text=f"{data.columns[0]}", fill="black")
    canvas.itemconfig(word_text, text=new_word[f"{data.columns[0]}"], fill="black")
    flip_card = window.after(TIMER, func=english_card)

def english_card():
    canvas.itemconfig(card_image, image=back_image)
    canvas.itemconfig(title_text, text=f"{data.columns[1]}", fill="white")
    canvas.itemconfig(word_text, text=new_word[f"{data.columns[1]}"], fill="white")

def know_word():
    global  new_word, to_learn
    to_learn.remove(new_word)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_word()

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

#language_input = Entry()

flip_card = window.after(TIMER, func=english_card)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
right_button_image = PhotoImage(file="images/right.png")
wrong_button_image = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 260, image=front_image)
title_text = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_button = Button(image=right_button_image, highlightthickness=0, command=know_word)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=next_word)
wrong_button.grid(column=0, row=1)

next_word()

window.mainloop()
