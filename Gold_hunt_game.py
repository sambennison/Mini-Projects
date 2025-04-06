import turtle 
import random

score = 0 

land = turtle.Screen()
land.bgpic("land.gif")
land.addshape("left.gif")
land.addshape("right.gif")
land.addshape("gold.gif")

hunter=turtle.Turtle()
hunter.shape("right.gif")
hunter.penup()
hunter.goto(100,-165)

scoreboard=turtle.Turtle()
scoreboard.penup()
scoreboard.goto(-240,-240)
scoreboard.write("score: ", score, align= "right", font=("Arial", 16, "bold"))
scoreboard.hideturtle()

coin=turtle.Turtle()
coin.shape("gold.gif")
coin.penup()
coin.goto(-280,280)

def right():
    hunter.shape("left.gif")
    hunter.forward(10)

def left():
    hunter.shape("right.gif")
    hunter.backward(10)

turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")
turtle.listen()

def move():
    y = coin.ycor()
    coin.sety(y-3)

while True:
    land.update()
    move()
    if coin.ycor() < -300:
        x =random.randint(-280,280)
        coin.goto(x,280) 
    if hunter.distance(coin) < 50:
        score = score + 1
        scoreboard.clear()
        scoreboard.write("score: {}".format(score), font=("Arial", 16, "bold"))
        x =random.randint(-280,280)
        coin.goto(x,280)
turtle.done()   