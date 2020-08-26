from turtle import *
from random import randint, random


start = 0
coordX =0
coordY=0

sliderH, sliderW = 60,20

totalX, totalY = 400, 400
ballX, ballY = 0.0, 0.0
ball_radius = 10

# player 1 is on the left, player 2 is on the right
player1_score = 0
player2_score = 0

dX = random() +1 #randint(1,2)
dY = random() +1 #randint(1,2)  

# Screen initia
screen = Screen()                        
screen.setup(totalX+50,totalY+50)
#screen.screensize(totalX,totalY)
#screen.title("Ping Pong Game!")
#print ('Screen size:', screen.screensize())
screen.bgcolor(' light green')

# Turtle 0 Creation => Draws boundaries for the Ping Pong Game and draws circles (which give extra points)
t0 = Turtle()
t0.hideturtle()
t0.color('black'); t0.speed(50)
t0.penup(); t0.goto(0,totalY//2+ball_radius); t0.write("Press 'Space' to start", True, align="center")
t0.penup(); t0.goto(150,totalY//2+10); t0.write("PLAYER 2 : ", True, align = "right")
t0.penup(); t0.goto(-150,totalY//2+10); t0.write("PLAYER 1 : ", True, align = "left")
t0.penup(); t0.goto(-totalX//2,-totalY//2); t0.pendown(); t0.goto(-totalX//2,totalY//2); t0.goto(totalX//2,totalY//2); t0.goto(totalX//2,-totalY//2); t0.goto(-totalX//2,-totalY//2); 
t0.penup(); #t0.goto(-180,200); t0.pendown();t0.goto(-180, -200); t0.penup()

# draw a circle
t0.goto(100,100)
t0.pendown()
t0.color("yellow")
t0.fillcolor("yellow")
t0.begin_fill()
t0.circle(10)
t0.end_fill()

# test
t0.penup
t0.goto(50,50)
t0.pendown()
for i in range(4):
  t0.fd(100)
  t0.left(90)

# Turtle 1 Creation => Acts as a slider controlled by 'Up' & 'Down' key
paddle1 = Turtle()
paddle1.hideturtle()
screen.register_shape("line", ((-sliderW//2,-sliderH//2), (-sliderW//2,sliderH//2), (sliderW//2,sliderH//2), (sliderW//2,-sliderH//2)))
paddle1.shape('line')
paddle1.speed(0)
paddle1.color('white')
paddle1.setheading(90) # face east at beginning
paddle1.penup(); paddle1.goto(-totalX//2 + 10, 0);
paddle1.showturtle()



def paddle1_up():
    #print ('paddle1 position:',paddle1.pos())
    paddle1.fd(5)

def paddle1_down():
    paddle1.bk(5)

def start_game():
    global start
    start = 1

screen.onkey(paddle1_up, 'W')
screen.onkey(paddle1_down, 'S')
 
# Turtle 2 Creation => Acts as a slider controlled by 'W' & 'S' key
paddle2 = Turtle()
paddle2.hideturtle()
screen.register_shape("line", ((-sliderW//2,-sliderH//2), (-sliderW//2,sliderH//2), (sliderW//2,sliderH//2), (sliderW//2,-sliderH//2)))
paddle2.shape('line')
paddle2.speed(0)
paddle2.color('white')
paddle2.setheading(90) # face east at beginning
paddle2.penup(); paddle2.goto(-totalX//2 + 390, 0);
paddle2.showturtle()


def paddle2_up():
    #print ('paddle2 position:',paddle2.pos())
    paddle2.fd(5)

def paddle2_down():
    paddle2.bk(5 )

def start_game():
    global start
    start = 1

screen.onkey(paddle2_up, 'Up')
screen.onkey(paddle2_down, 'Down')

# Create a turtle for each player's score. Move them to the correct positions.
p1_score_turtle = Turtle()
p1_score_turtle.hideturtle()

p1_score_turtle.penup()
p1_score_turtle.goto(-90,210)
p1_score_turtle.pendown()


p2_score_turtle = Turtle()
p2_score_turtle.hideturtle()

p2_score_turtle.penup()
p2_score_turtle.goto(155,210)
p2_score_turtle.pendown()


def start_game():
    global start
    start = 1
    print(ballX,ballY)

def pause_game():
    global pause
    print("game is paused")
    print ('ball position:',ball.pos()) # what does position exactly refer to here?
    print("test")
    dX = ballX
    dY = ballY
    #screen.ontimer(move_ball,0)
    #global sliderH, sliderW 
    #sliderH, sliderW = 0,0
    #global totalX, totalY
    #totalX, totalY=0,0
    #global ballX, ballY
    print("tesball")
    print(dX, dY)
    print("test3")
    coordX = dX
    coordY = dY
    print(coordX, coordY)
    #global dX, dY
    #dX, dY=0,0 
    #global collision
    #collision=0
    #global start
    #start=0
    #print("direction:" ,dX,dY)
    
# screen.onkey(function, key: when 'key' is pressed, run function 'function'
screen.onkey(pause_game,'p')
screen.onkey(start_game, ' ')

# define the ball shape with the coordinates of the corners of a polygon
screen.register_shape("ball",[
  (-ball_radius, 0),
  (0, -ball_radius),
  (ball_radius, 0),
  (0, ball_radius)
])

# Turtle 2 Creation => Acts as the ping pong ball 
ball = Turtle()
ball.shape('turtle'); ball.speed(0.5)
ball.color('darkGreen')
#ball.shapesize(ball_radius, ball_radius)
ball.penup(); ball.goto(ballX,ballY);paddle1.setheading(90)
#print ('Ball size:', ball.turtlesize())

def was_left_paddle_hit():
    sliderX, sliderY = paddle1.pos()
    paddle1_bottom = sliderY - sliderH//2
    paddle1_top = (sliderY + sliderH//2)
    paddle1_right = -totalX//2 + sliderW
    
    return (ballY >= paddle1_bottom 
        and ballY <= paddle1_top 
        and ballX <= paddle1_right + ball_radius)

def was_right_paddle_hit():
    sliderX, sliderY = paddle2.pos()
    paddle1_bottom = sliderY - sliderH//2
    paddle1_top = (sliderY + sliderH//2)
    paddle1_left = totalX//2 - sliderW
    
    return (ballY >= paddle1_bottom 
        and ballY <= paddle1_top 
        and ballX >= paddle1_left - ball_radius)
  
last_paddle_hit = 0

# number of times each player pushed the ball into the edge of a collectable object
times_p1_hit_edge = 0
times_p2_hit_edge = 0

ball_edge_status = "no"

def move_ball():
  try:
    global sliderH, sliderW
    global totalX, totalY
    global ballX, ballY
    global dX, dY
    global collision
    global start
    global player1_score, player2_score
    global last_paddle_hit
    global times_p1_hit_edge
    global times_p2_hit_edge
    global ball_edge_status

    right_wall = totalX//2 - ball_radius
    left_wall = - totalX//2 + ball_radius
    top_wall = totalY//2 - ball_radius
    bottom_wall = - totalY//2 + ball_radius

    ball.goto(ballX, ballY)

    # Check if the ball is on the edge of a collectable object
    if 50 < ball.ycor() < 150 and 49.9 <= ball.xcor() <= 50.9: 
      # x is approx 50
      ball_edge_status = "yes"
    elif 50 < ball.ycor() < 150 and 149.9 <= ball.xcor() <=  150.9: 
      # x is approx 150
      ball_edge_status = "yes"
    elif 50 < ball.xcor() < 150 and 49.9 <= ball.ycor() <= 50.9: 
      # y is approx 50
      ball_edge_status = "yes"
    elif 50 < ball.xcor() < 150 and 149.9 <= ball.ycor() <=  150.9: 
      # y is approx 150
      ball_edge_status = "yes"

    # bounce off walls by changing direction of ball
    if ballY > top_wall:
        dY = -dY
    if ballY < bottom_wall:
        dY = -dY  

    # hit on the paddle and bounce off by changing direction 
    if was_left_paddle_hit():
      print("left paddle was hit, bouncing")
      dX = -dX
      last_paddle_hit = 1

    # hit on the paddle and bounce off by changing direction 
    if was_right_paddle_hit():
      print("right paddle was hit, bouncing")
      dX = -dX
      last_paddle_hit = 2   
    
    # if hit left wall, restart and give player 2 a point
    if ballX < left_wall:
            start = 0
            player2_score +=1
            p2_score_turtle.clear()
            p2_score_turtle.write(player2_score, align = "left")

    # if hit right wall, restart and give player 1 a point
    if ballX > right_wall:
            start = 0
            player1_score +=1
            p1_score_turtle.clear()
            p1_score_turtle.write(player1_score, align = "left")
   
    # if the game is started, change ball position by the direction it goes in
    if start == 1:
        ballX += dX
        ballY += dY
        
    # if the game is not started, put the ball in the middle
    else: 
        ballX = 0
        ballY = 0
    
# if the ball is on the edge
    if ball_edge_status == "yes":
      if last_paddle_hit == 1:
        times_p1_hit_edge += 1
      elif last_paddle_hit == 2:
        times_p2_hit_edge += 1
      # if times_p1_hit_edge is even
      if times_p1_hit_edge % 2 == 0:
        player1_score += 1
        p1_score_turtle.clear()
        p1_score_turtle.write(player1_score, align = "left")
      # if times_p2_hit_edge is even
      elif times_p2_hit_edge % 2 == 0:
        player2_score += 1
        p2_score_turtle.clear() 
        p2_score_turtle.write(player2_score, align = "left")

    # move the ball with updates every milisecond
    screen.ontimer(move_ball,1)

  except Exception as e:
    print("ERROR in move_ball()!")
    print(e)

move_ball()

screen.listen()
screen.mainloop()


