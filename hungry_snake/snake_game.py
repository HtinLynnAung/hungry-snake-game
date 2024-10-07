# This Hungry Snake game tutorial is coded by HtinLinAung(LeoKrypto)
# Date: 7.10.2024

# import required modules
import turtle
import time
import random
import winsound

# set constants
delay = 0.1
score = 0
paused = False

# create a window screen
window = turtle.Screen()
window.title("Hungry Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# food in the game
food = turtle.Turtle()
colors = random.choice(["red", "green"])
shapes = random.choice(["circle", "square"])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0", align="center", font=("arial", 36, "normal"))

# Pause text display turtle
pause_turtle = turtle.Turtle()
pause_turtle.speed(0)
pause_turtle.color("white")
pause_turtle.penup()
pause_turtle.hideturtle()
pause_turtle.goto(0, 0)

# create pause function
def toggle_pause():
    global paused
    paused = not paused
    if paused:
        pause_turtle.clear()
        pause_turtle.write("PAUSE", align="center", font=('candara', 24, "normal"))
    else:
        pause_turtle.clear()


# assign the keys for direction
def move_up():
    if head.direction != "Down":
        head.direction = "Up"

def move_left():
    if head.direction != "Right":
        head.direction = "Left"

def move_down():
    if head.direction != "Up":
        head.direction = "Down"

def move_right():
    if head.direction != "Left":
        head.direction = "Right"

def move():
    if head.direction == "Up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "Down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "Right":
        x = head.xcor()
        head.setx(x+20)
    if head.direction == "Left":
        x = head.xcor()
        head.setx(x-20)

window.listen()
window.onkeypress(move_up, "Up")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
window.onkeypress(move_down, "Down")
window.onkeypress(toggle_pause, "space")

segments = []


# Main Gameplay
while True:
    window.update()

    if not paused:
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            winsound.PlaySound("wallhit.wav", winsound.SND_ASYNC)
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            colors = random.choice(["red", "green"])
            shapes = random.choice(["square", "circle"])
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("arial", 36, "normal"))

        if head.distance(food) < 20:
            x = random.randint(-270, 270)
            y = random.randint(-270, 270)
            food.goto(x, y)

            # adding segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("orange")
            new_segment.penup()
            segments.append(new_segment)
            delay -= 0.001
            score += 10
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("arial", 36, "normal"))

        # checking for collisions between head and body segemnts
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
        move()
        for segment in segments:
            if segment.distance(head) < 20:
                winsound.PlaySound("wallhit.wav", winsound.SND_ASYNC)
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "Stop"
                colors = random.choice(["red", "green"])
                shapes = random.choice(["square", "circle"])
                for segment in segments:
                    segment.goto(1000, 1000)
                segments.clear()

                score = 0
                delay = 0.1
                pen.clear()
                pen.write("Score:  {}".format(score), align="center", font=("arial", 36, "normal"))
        time.sleep(delay)
