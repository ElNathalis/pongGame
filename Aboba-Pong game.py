import turtle
sc = turtle.Screen()
sc.title("Aboba-Pong game")
sc.bgcolor("pink")
sc.setup(width=1000, height=600)

left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400,0)

right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400,0)

aboba_ball = turtle.Turtle()
aboba_ball.speed(40)
aboba_ball.shape("circle")
aboba_ball.color("yellow")
aboba_ball.penup()
aboba_ball.goto(0,0)

aboba_ball.dx = 5
aboba_ball.dy = -5

left_player = 0
right_player = 0

sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("black")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("left_player = 0   right_player = 0",
	align="center", font=("Times New Roman", 24, "italic"))

def paddle1up():
	y = left_pad.ycor()
	y += 20
	left_pad.sety(y)

def paddle1down():
	y = left_pad.ycor()
	y -= 20
	left_pad.sety(y)


def paddle2up():
	y = right_pad.ycor()
	y += 20
	right_pad.sety(y)

def paddle2down():
	y = right_pad.ycor()
	y -= 20
	right_pad.sety(y)


sc.listen()
sc.onkeypress(paddle1up, "e")
sc.onkeypress(paddle1down, "x")
sc.onkeypress(paddle2up, "Up")
sc.onkeypress(paddle2down, "Down")

while True:
	sc.update()

	aboba_ball.setx(aboba_ball.xcor() + aboba_ball.dx)
	aboba_ball.sety(aboba_ball.ycor() + aboba_ball.dy)

	if aboba_ball.ycor() > 280:
		aboba_ball.sety(280)
		aboba_ball.dy *= -1

	if aboba_ball.ycor() < -280:
		aboba_ball.sety(-280)
		aboba_ball.dy *= -1

	if aboba_ball.xcor() > 500:
		aboba_ball.goto(0,0)
		aboba_ball.dx *= -1
		left_player += 1
		sketch.clear()
		sketch.write("left_player = {}   right_player = {}".format(left_player, right_player),
			align="center", font=("Times New Roman", 24, "italic"))

	if aboba_ball.xcor() < -500:
		aboba_ball.goto(0,0)
		aboba_ball.dx *= -1
		right_player += 1
		sketch.clear()
		sketch.write("left_player = {}   right_player = {}".format(left_player, right_player),
			align="center", font=("Times New Roman", 24, "italic"))

	if (aboba_ball.xcor() > 360 and aboba_ball.xcor() < 400) and (aboba_ball.ycor() < right_pad.ycor() + 50 and aboba_ball.ycor() > right_pad.ycor() - 50):
		aboba_ball.setx(360)
		aboba_ball.dx *= -1

	if (aboba_ball.xcor() < -360 and aboba_ball.xcor() > -400) and (aboba_ball.ycor() < left_pad.ycor() + 50 and aboba_ball.ycor() > left_pad.ycor() - 50):
		aboba_ball.setx(-360)
		aboba_ball.dx *= -1



