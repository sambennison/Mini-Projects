import turtle 
import random

segment = []
grass = turtle.Screen()
grass.bgpic("grass.gif")
grass.addshape("head_up.gif")
grass.addshape("head_down.gif")
grass.addshape("head_left.gif")
grass.addshape("head_right.gif")
grass.addshape("body.gif")

snake = turtle.Turtle()
snake.penup()
snake.goto(0, 0)
snake.setheading(90)
snake.shape("head_up.gif")

food = turtle.Turtle()
food.penup()
food.speed(500)
food.color("red")
food.shape("circle")
food.goto(100, 10)
#score 
score = turtle.Turtle()
score.penup()
score.hideturtle()
score.speed(500)
score.goto(0, 250)
score.write("Score: ", align="center", font=("Arial", 16, "normal"))
point = 0
def move():
    snake.forward(2)
def up():
    if snake.heading() != 270:
        snake.setheading(90)
        snake.shape("head_up.gif")
def down():
    if snake.heading() != 90:
        snake.setheading(270)
        snake.shape("head_down.gif")
def left():
    if snake.heading() != 0:
        snake.setheading(180)
        snake.shape("head_left.gif")
def right():
    if snake.heading() != 180:
        snake.setheading(0)
        snake.shape("head_right.gif")

turtle.onkeypress(up, "w")
turtle.onkeypress(down, "s")
turtle.onkeypress(left, "a")
turtle.onkeypress(right, "d")
turtle.listen()

while True:
    grass.update()

    if snake.xcor()>290 or snake.xcor()<-290 or snake.ycor()>290 or snake.ycor()<-290:
        grass.bgpic("game_over.gif")
        food.hideturtle()
        break

    for i in range(len(segment)):
        if snake.distance(segment[i]) < 10:
            grass.bgpic("game_over.gif")
            food.hideturtle()
            break

    if snake.distance(food) < 10:      
        x = random.randint(-285, 285)
        y = random.randint(-285, 285)
        food.goto(x, y)
        point = point + 1
        score.clear()
        score.write("Score: {}".format(point), align="center", font=("Arial", 16, "normal"))
        body = turtle.Turtle()
        body.penup()
        body.shape("body.gif")
        segment.append(body)

    for i in range(len(segment)-1, 0, -1):
        x = segment[i-1].xcor()
        y = segment[i-1].ycor()
        segment[i].goto(x, y)
    
    if len(segment) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segment[0].goto(x, y)

    move()