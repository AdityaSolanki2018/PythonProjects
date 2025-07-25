import pandas
import turtle


# Screen Setup
screen = turtle.Screen()
screen.title("Guess The State Game")
screen.setup(width=800,height=600)
image = "./Guess_The_State_Game/blank_states_img.gif"
screen.addshape(image)
screen.title("Guess The State Game")
turtle.shape(image)

# Initialize turtle Object


# Load CSV
data = pandas.read_csv("./Guess_The_State_Game/50_states.csv")
state_list = data.state.to_list()

# Initialize a list to keep track of guessed states
guessed_states = []

# Main Game Loop
while(len(guessed_states) < 50):
    user_guess =  screen.textinput(title=f"{len(guessed_states)}/50 Guessed Correct",prompt="Enter A State Name")
    if user_guess.title() in state_list:
        state_data = data[data.state == user_guess.title()]
        x_cor = state_data.x.item()
        y_cor = state_data.y.item()
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_cor,y_cor)
        t.write(user_guess, font=("Arial", 10, "normal"))
        guessed_states.append(user_guess.title())
    else:
        if user_guess == "Exit":
            missing_states = [state for state in state_list if state not in guessed_states]
            missing_states_df = pandas.DataFrame(missing_states)
            missing_states_df.to_csv("states_to_learn.csv", index=False)
            break
        else:
            print("Wrong Guess! Try Again.")

if len(guessed_states) == 50:
    print("Congratulations! You've guessed all the states correctly.")
