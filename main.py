from turtle import *
from random import randint, random, randrange


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

paddle1_speed = 5
paddle2_speed = 5

dX = random() +1 #randint(1,2)
dY = random() +1 #randint(1,2)  

# Screen initia
screen = Screen()                        
screen.setup(totalX+50,totalY+350)
#screen.screensize(totalX,totalY)
#screen.title("Ping Pong Game!")
#print ('Screen size:', screen.screensize())
screen.bgcolor(39,)

# https://www.rapidtables.com/web/color/RGB_Color.html
# screen.bgcolor(((r, g, b))
#screen.bgcolor((50, 50, 200))


# Turtle 0 Creation => Draws boundaries for the Ping Pong Game and draws circles (which give extra points)
t0 = Turtle()
t0.hideturtle()
t0.color('black'); t0.speed(50)
t0.penup(); t0.goto(0,totalY//2+ball_radius); 
t0.write("Press 'Space' to start", True, align="center")  
t0.penup(); t0.goto(150,totalY//2+10); t0.write("PLAYER 2 : ", True, align = "right")
t0.penup(); t0.goto(-150,totalY//2+10); t0.write("PLAYER 1 : ", True, align = "left")
t0.penup(); t0.goto(-30,totalY-100); t0.write("----= RULES =----", True, align = "left")
t0.penup(); t0.goto(70,totalY-120); t0.write("- Player1 control keys are S,W ", True, align = "right")
t0.penup(); t0.goto(97 ,totalY-130); t0.write("- Player2 control keys are arrow keys", True, align = "right")
t0.penup(); t0.goto(47 ,totalY-140); t0.write("- Player with 5 points wins", True, align = "right")

t0.penup(); t0.goto(-totalX//2,-totalY//2); t0.pendown(); t0.goto(-totalX//2,totalY//2); t0.goto(totalX//2,totalY//2); t0.goto(totalX//2,-totalY//2); t0.goto(-totalX//2,-totalY//2); 
t0.penup(); #t0.goto(-180,200); t0.pendown();t0.goto(-180, -200); t0.penup()

# mango
mango = Turtle()
mango.shape("circle")
mango.color("yellow")
mango.penup()
mango.speed(0)

def teleport_mango():
  # generate random position
  mangoX = randrange(-totalX//2,totalX//2)
  mangoY = randrange(-totalY//2,totalY//2)
  # go to that position
  mango.goto(mangoX,mangoY)

def is_mango_hit():
  x_bound_left = mango.xcor() - 15
  x_bound_right = mango.xcor() + 15
  y_bound_top = mango.ycor() + 15
  y_bound_bottom = mango.ycor() - 15

  # the returned value will be True or False
  return x_bound_left <= ball.xcor() <= x_bound_right and y_bound_bottom <= ball.ycor() <= y_bound_top


# create the win turtle (writes which player won)
win_turtle = Turtle()
win_turtle.hideturtle()
win_turtle.penup()
win_turtle.goto(0,100)
win_turtle.pendown()

# Turtle 1 Creation => Acts as a slider controlled by 'Up' & 'Down' key
paddle1 = Turtle()
paddle1.hideturtle()
screen.register_shape("line", ((-sliderW//2,-sliderH//2), (-sliderW//2,sliderH//2), (sliderW//2,sliderH//2), (sliderW//2,-sliderH//2)))
paddle1.shape('line')
paddle1.speed(0)
paddle1.color((139,69,19))
# screen.bgcolor(((r, g, b))
#screen.bgcolor((50, 50, 200))
paddle1.setheading(90) # face east at beginning
paddle1.penup(); paddle1.goto(-totalX//2 + 10, 0);
paddle1.showturtle()




def paddle1_up():
    #print ('paddle1 position:',paddle1.pos())
    paddle1.fd(paddle1_speed)

def paddle1_down():
    paddle1.bk(paddle1_speed)

screen.onkey(paddle1_up, 'W')
screen.onkey(paddle1_down, 'S')
 
# Turtle 2 Creation => Acts as a slider controlled by 'W' & 'S' key
paddle2 = Turtle()
paddle2.hideturtle()
screen.register_shape("line", ((-sliderW//2,-sliderH//2), (-sliderW//2,sliderH//2), (sliderW//2,sliderH//2), (sliderW//2,-sliderH//2)))
paddle2.shape('line')
paddle2.speed(0)
paddle2.color((139,69,19))
paddle2.setheading(90) # face east at beginning
paddle2.penup(); paddle2.goto(-totalX//2 + 390, 0);
paddle2.showturtle()


def paddle2_up():
    #print ('paddle2 position:',paddle2.pos())
    paddle2.fd(paddle2_speed)

def paddle2_down():
    paddle2.bk(paddle2_speed)

def start_game():
    global start
    start = 1
    win_turtle.clear(0)

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
ball.speed(0)
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
    global paddle1_speed
    global paddle2_speed

    right_wall = totalX//2 - ball_radius
    left_wall = - totalX//2 + ball_radius
    top_wall = totalY//2 - ball_radius
    bottom_wall = - totalY//2 + ball_radius

    ball.goto(ballX, ballY)

    # bounce off walls by changing direction of ball
    if ballY > top_wall:
        dY = -dY
    if ballY < bottom_wall:
        dY = -dY  

    # hit on the paddle and bounce off by changing direction 
    if was_left_paddle_hit():
      dX = -dX
      last_paddle_hit = 1

    # hit on the paddle and bounce off by changing direction 
    if was_right_paddle_hit():
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
   
    # if a player gets 5 points, the game ends
    if player1_score == 5:
      win_turtle.write("Player 1 wins!", align = "center")
      player1_score = 0
      player2_score = 0
      p1_score_turtle.clear()
      p2_score_turtle.clear()
    elif player2_score == 5:
      win_turtle.write("Player 2 wins!", align = "center")
      player1_score = 0
      player2_score = 0
      p1_score_turtle.clear()
      p2_score_turtle.clear()

    if is_mango_hit():
      teleport_mango()
      if last_paddle_hit == 1:
        player1_score += 1
        p1_score_turtle.clear()
        p1_score_turtle.write(player1_score, align = "left")
        paddle1_speed *= 1.5
      elif last_paddle_hit == 2:
        player2_score += 1
        p2_score_turtle.clear()
        p2_score_turtle.write(player2_score, align = "left")
        paddle2_speed *= 1.5

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

