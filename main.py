import turtle
import pandas


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("U.S. State Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    df_states = pandas.read_csv("50_states.csv")
    user_selected_states = {}

    for state in df_states.state:
        user_selected_states[state] = 0

    print(df_states, user_selected_states)

    while sum(user_selected_states.values()) < 50:
        user_input = screen.textinput(title="Guess The State", prompt="What's another state's name?")
        if user_input is None:
            break

        user_input = user_input.title()
        if user_selected_states.get(user_input) == 0:
            user_selected_states[user_input] = 1
            #  Trigger the turtle to move to the correct position
            single_state = df_states[df_states["state"] == user_input]
            bob = turtle.Turtle()
            bob.hideturtle()
            bob.penup()
            bob.setposition(single_state['x'].item(), single_state['y'].item())
            bob.write(user_input, True, "center")
