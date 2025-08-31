import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer_id = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer_id)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    checkmark.config(text="")
    reps = 1

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        timer.config(text="Work", fg= GREEN)
        countdown(work_sec)
    elif reps % 2 == 0:
        if reps % 8 == 0:
            timer.config(text="Break", fg= RED)
            countdown(long_break_sec)
        else:
            timer.config(text="Break", fg=PINK)
            countdown(short_break_sec)
    reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(counter):

    counter_min = math.floor(counter / 60)
    counter_sec = counter % 60
    if counter_sec < 10:
        counter_sec = f"0{counter_sec}"

    canvas.itemconfig(timer_text, text=f"{counter_min}:{counter_sec}")
    if counter > 0:
        global timer_id
        timer_id = window.after(1000, countdown, counter - 1 )
    else:
        start_timer()
        if reps % 2 == 1:
            checkmark.config(text="✔")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)


timer = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
timer.grid(column=1 , row=0)

tomato_img = PhotoImage(file="tomato.png")

canvas = Canvas(width=250, height=250, bg=YELLOW, highlightthickness=0)
canvas.create_image(115, 120, image=tomato_img)
timer_text = canvas.create_text(125, 140, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1 , row=1)

start_button = Button(text="Start",command=start_timer, highlightthickness=0)
start_button.grid(column=0 , row=2)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2 , row=2)

checkmark = Label(fg=GREEN, bg=YELLOW, highlightthickness=0)
checkmark.grid(column=1, row=3)


window.mainloop()