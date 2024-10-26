import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Catch-A-Turtle Game")
wn.bgcolor("lightblue")

# Game configuration
spot_color = "pink"
turtle_size = 2
turtle_shape = "circle"
score = 0
timer_up = False

# Initialize turtle objects
spot = turtle.Turtle()
spot.shape(turtle_shape)
spot.shapesize(turtle_size)
spot.fillcolor(spot_color)
spot.penup()  # Prevent the turtle from drawing lines
spot.hideturtle()  # Hide the turtle for initial setup

# Score writer turtle
score_writer = turtle.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(0, 260)  # Position for score display
font_setup = ("Arial", 20, "normal")

# Countdown timer writer turtle
counter_writer = turtle.Turtle()
counter_writer.penup()
counter_writer.hideturtle()
counter_writer.goto(0, -260)  # Position for timer display

# Function to update score
def update_score():
    global score
    score += 1
    score_writer.clear()  # Clear previous score
    score_writer.write(f"Score: {score}", font=font_setup, align="center")

# Function to change position of the turtle
def change_position():
    new_xpos = random.randint(-200, 200)
    new_ypos = random.randint(-200, 200)
    spot.goto(new_xpos, new_ypos)
    spot.showturtle()  # Show the turtle when moving

# Function to handle turtle click
def spot_clicked(x, y):
    global timer_up
    if not timer_up:
        update_score()
        change_position()

# Countdown function
def countdown(time_left):
    global timer_up
    if time_left > 0:
        counter_writer.clear()  # Clear previous time
        counter_writer.write(f"Time left: {time_left}", font=font_setup, align="center")
        wn.ontimer(lambda: countdown(time_left - 1), 1000)  # Call countdown every second
    else:
        timer_up = True
        spot.hideturtle()  # Hide the turtle when time runs out
        counter_writer.clear()
        counter_writer.write("Time's up!", font=font_setup, align="center")

# Start the game
def start_game():
    global score, timer_up
    score = 0
    timer_up = False
    change_position()  # Initial position
    countdown(30)  # 30 seconds countdown
    spot.onclick(spot_clicked)  # Only register clicks on the spot turtle

# Set up the game
start_game()

# Keep the window open
wn.mainloop()
