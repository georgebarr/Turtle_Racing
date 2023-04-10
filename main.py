from turtle import Turtle, Screen
import random, os

os.system('cls' if os.name == 'nt' else 'clear')
# Clears the terminal history for the user

screen = Screen()
screen.setup(width=500, height=400)

with open('streak.txt', 'r') as file:
    streak = int(file.read())
    file.close()

colors = ['red', 'orange', 'black', 'green', 'blue', 'purple']

prediction = screen.textinput(title="Make a prediction",
                              prompt="Which turtle is going to win the race? (Red, orange, black, green, blue,"
                                     " or purple): ").lower()

while prediction not in colors:
    prediction = screen.textinput(title="Make a prediction",
                                  prompt="Which turtle is going to win the race? (Red, orange, black, green, blue,"
                                         " or purple): ").lower()

y_positions = [-70, -40, -10, 20, 50, 80]
list_turtles = []

for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    new_turtle.goto(x=-230, y=y_positions[turtle])
    list_turtles.append(new_turtle)

race_occurring = False

if prediction:
    race_occurring = True

while race_occurring:

    for turtle in list_turtles:
        if turtle.xcor() > 230:
            race_occurring = False
            winner = turtle.pencolor()

            if prediction == winner:
                print(f"Your prediction was correct! The {winner} turtle won the race!")
                streak += 1
            else:
                print(f"Unfortunately, your prediction was incorrect. The {winner} turtle won the race.")
                streak = 0

            with open('streak.txt', 'w') as file:
                file.write(str(streak))
                file.close()

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
