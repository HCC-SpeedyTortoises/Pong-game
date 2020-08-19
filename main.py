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

# Turtle 0 Creation => Draws boundaries for the Ping Pong Game
t0 = Turtle()
t0.hideturtle()
t0.color('black'); t0.speed(50)
t0.penup(); t0.goto(0,totalY//2+ball_radius); t0.write("Press 'Space' to start", True, align="center")
t0.penup(); t0.goto(150,totalY//2+10); t0.write("PLAYER 2 : "+str(player1_score), True, align = "right")
t0.penup(); t0.goto(-150,totalY//2+10); t0.write("PLAYER 1 : "+str(player2_score), True, align = "left")
t0.penup(); t0.goto(-totalX//2,-totalY//2); t0.pendown(); t0.goto(-totalX//2,totalY//2); t0.goto(totalX//2,totalY//2); t0.goto(totalX//2,-totalY//2); t0.goto(-totalX//2,-totalY//2); 
t0.penup(); #t0.goto(-180,200); t0.pendown();t0.goto(-180, -200); t0.penup()


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
    paddle2.bk(5)

def start_game():
    global start
    start = 1

screen.onkey(paddle2_up, 'Up')
screen.onkey(paddle2_down, 'Down')

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
ball.shape('ball'); ball.speed(0)
ball.color('brown')
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

def move_ball():
  try:
    global sliderH, sliderW
    global totalX, totalY
    global ballX, ballY
    global dX, dY
    global collision
    global start
    global player1_score, player2_score

    #print(ballX, ballY)
    ball.goto(ballX, ballY)

    right_wall = totalX//2 - ball_radius
    left_wall = - totalX//2 + ball_radius
    top_wall = totalY//2 - ball_radius
    bottom_wall = - totalY//2 + ball_radius

    # bounce off walls by changing direction of ball
    if ballY > top_wall:
        dY = -dY
    if ballY < bottom_wall:
        dY = -dY  

    # hit on the paddle and bounce off by changing direction 
    if was_left_paddle_hit():
      print("left paddle was hit, bouncing")
      dX = -dX
            
    # if hit right wall, restart and give player 2 a point
    if ballX < left_wall:
            start = 0
            player2_score +=1

    # if hit right wall, restart and give player 1 a point
    if ballX > right_wall:
            start = 0
            player1_score +=1
   
    # if the game is started, change ball position by the direction it goes in
    if start == 1:
        ballX += dX
        ballY += dY
        
    # if the game is not started, put the ball in the middle
    else: 
        ballX = 0
        ballY = 0
    
    # move the ball with updates every milisecond
    screen.ontimer(move_ball,1)
    
  except Exception as e:
    print("ERROR in move_ball()!")
    print(e)

move_ball()

screen.listen()
screen.mainloop()
