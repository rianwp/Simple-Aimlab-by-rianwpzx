import turtle
import random

score = 0
mini_size = 3
real_size = mini_size * 10

win = turtle.Screen()
win.title("Simple Aimlab by rianwpzx")
win.bgcolor("white")
win.setup(width=800, height=600)
win.tracer(0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_wid=mini_size, stretch_len=mini_size)
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

def button(x,y):
    global score
    global real_size
    if x <= (real_size + ball.xcor()) and x >= (ball.xcor()-real_size) and y <= (real_size + ball.ycor()) and y >= (ball.ycor()-real_size):
        ball.setx(random.randint(-350, 350))
        ball.sety(random.randint(-250, 220))
        score += 1
    pen.clear()
    pen.write("Score : {}".format(score), align="center", font=("Courier", 24, "normal"))
    
win.listen()
win.onclick(button)

while True:
    win.update()
    
    
    
    
    
    
    
        
        
    
    
    
    