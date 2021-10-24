import turtle
import random

score = 0

win = turtle.Screen()
win.title("Simple Aimlab by rianwpzx")
win.bgcolor("white")
win.setup(width=800, height=600)
win.tracer(0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_wid=3, stretch_len=3)
ball.color("black")
ball.penup()
ball.goto(0, 0)

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score : {}".format(score), align="center", font=("Courier", 24, "normal"))


def getpos(x,y):
    global score
    if x <= (30 + ball.xcor()) and x >= (ball.xcor()-30) and y <= (30 + ball.ycor()) and y >= (ball.ycor()-30):
        ball.setx(random.randint(-350, 350))
        ball.sety(random.randint(-250, 220))
        score += 1
    pen.clear()
    pen.write("Score : {}".format(score), align="center", font=("Courier", 24, "normal"))


win.listen()
win.onclick(getpos)




while True:
    win.update()
    
    
    
    
    
    
    
        
        
    
    
    
    