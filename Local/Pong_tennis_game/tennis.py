import turtle

# Constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
PADDLE_MOVE_DISTANCE = 20
BALL_SPEED = 5
WINNING_SCORE = 12

# Setup screen
ground = turtle.Screen()
ground.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
ground.bgpic("court.png")
ground.tracer(0)  # Turn off automatic updates for smoother animation
ground.addshape("left.gif")
ground.addshape("right.gif")
ground.addshape("ball.gif")

# Left player setup
leftplayer = turtle.Turtle()
leftplayer.penup()
leftplayer.shape("left.gif")
leftplayer.goto(-400, -200)

# Right player setup
rightplayer = turtle.Turtle()
rightplayer.penup()
rightplayer.shape("right.gif")
rightplayer.goto(400, -200)

# Ball setup
ball = turtle.Turtle()
ball.penup()
ball.shape("ball.gif")
ball.dx = BALL_SPEED
ball.dy = -BALL_SPEED

# Score display
leftpen = turtle.Turtle()
leftpen.penup()
leftpen.hideturtle()
leftpen.goto(-400, 250)
leftpen.color("white")
leftscore = 0
leftpen.write(f"Left player: {leftscore}", font=("Arial", 24, "normal"))

rightpen = turtle.Turtle()
rightpen.penup()
rightpen.hideturtle()
rightpen.goto(100, 250)
rightpen.color("white")
rightscore = 0
rightpen.write(f"Right player: {rightscore}", font=("Arial", 24, "normal"))

# Player movement functions
def leftplayerup():
    if leftplayer.ycor() < SCREEN_HEIGHT // 2 - 50:
        leftplayer.sety(leftplayer.ycor() + PADDLE_MOVE_DISTANCE)

def leftplayerdown():
    if leftplayer.ycor() > -SCREEN_HEIGHT // 2 + 50:
        leftplayer.sety(leftplayer.ycor() - PADDLE_MOVE_DISTANCE)

def rightplayerup():
    if rightplayer.ycor() < SCREEN_HEIGHT // 2 - 50:
        rightplayer.sety(rightplayer.ycor() + PADDLE_MOVE_DISTANCE)

def rightplayerdown():
    if rightplayer.ycor() > -SCREEN_HEIGHT // 2 + 50:
        rightplayer.sety(rightplayer.ycor() - PADDLE_MOVE_DISTANCE)

# Key bindings
ground.listen()
ground.onkeypress(leftplayerup, "w")
ground.onkeypress(leftplayerdown, "s")
ground.onkeypress(rightplayerup, "Up")
ground.onkeypress(rightplayerdown, "Down")

# Game loop
def game_loop():
    global leftscore, rightscore

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball collision with top and bottom walls
    if ball.ycor() > SCREEN_HEIGHT // 2 - 10 or ball.ycor() < -SCREEN_HEIGHT // 2 + 10:
        ball.dy *= -1

    # Ball collision with paddles
    if ball.distance(rightplayer) < 50 and ball.xcor() > 380:
        ball.dx *= -1
    if ball.distance(leftplayer) < 50 and ball.xcor() < -380:
        ball.dx *= -1

    # Ball out of bounds
    if ball.xcor() > SCREEN_WIDTH // 2:
        leftscore += 1
        leftpen.clear()
        leftpen.write(f"Left player: {leftscore}", font=("Arial", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -SCREEN_WIDTH // 2:
        rightscore += 1
        rightpen.clear()
        rightpen.write(f"Right player: {rightscore}", font=("Arial", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Check for winning condition
    if leftscore == WINNING_SCORE:
        leftpen.goto(0, 0)
        leftpen.color("red")
        leftpen.write("Left player wins!", align="center", font=("Arial", 24, "normal"))
        return
    if rightscore == WINNING_SCORE:
        rightpen.goto(0, 0)
        rightpen.color("red")
        rightpen.write("Right player wins!", align="center", font=("Arial", 24, "normal"))
        return

    # Update the screen and schedule the next frame
    ground.update()
    ground.ontimer(game_loop, 20)

# Start the game loop
game_loop()
ground.mainloop()