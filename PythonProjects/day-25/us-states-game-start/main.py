import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
states_list = data.state.to_list()
user_score = 0
guessed_states = []

while len(guessed_states) < 50:
    user_input = str.title(screen.textinput(title=f"{user_score}/50 Guess the state", prompt="What's another state's name? or type Exit"))

    if user_input in states_list:
        guessed_states.append(user_input)
        state_data = data[data.state == user_input]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())
        user_score += 1

    if user_input == "Exit":
        to_guess = [state_name for state_name in states_list if state_name not in guessed_states ]
        to_guess_series = pd.Series(data=to_guess, name="States")
        to_guess_series.to_csv("States to learn.csv")
        break



