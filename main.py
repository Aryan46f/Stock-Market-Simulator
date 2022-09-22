import turtle as trtl
import random
import time

# set up background screen
wn = trtl.Screen()
trtl.bgcolor("lightgray")

# title question text 
title = trtl.Turtle()
title.hideturtle()
title.penup()
title.goto(-200, 0)
title.write("Which company's stocks would you like to buy?", font=('Roboto', 12, 'normal'))
title.goto(-100, -100)
title.write("1- GME, 2- AMC, 3-BBW", font=('Roboto', 12, 'normal'))

# takes user input as a variable
stock = input("Which company's stocks would you like to buy? 1- GME, 2- AMC, 3-BBW")
stock = int(stock)

# decides between which logo to display
if(stock == 1):
  logo = "gme.gif"
if(stock == 2):
  logo = "amc.gif"
if(stock == 3):
  logo = "bbw.gif"

# creates a turtle object using the logo as image and displays
wn.addshape(logo)
title.shape(logo)
title.goto(0, 300)
title.showturtle()


# create border turtle
drawer = trtl.Turtle("circle")
drawer.pensize(5)
drawer.hideturtle()

# set up turtle for border
drawer.penup()
drawer.goto(-250,200)
drawer.pendown()
drawer.pencolor("black")
drawer.fillcolor("white")
drawer.begin_fill()

# draw black border
drawer.setheading(270)
drawer.forward(300)
drawer.setheading(0)
drawer.forward(500)

# complete fill of graph background
drawer.pencolor("lightgray")
drawer.setheading(90)
drawer.forward(300)
drawer.setheading(180)
drawer.forward(500)
drawer.end_fill()
drawer.setheading(0)
drawer.pencolor("black")


# place buy button 
drawer.penup()
drawer.goto(0, -270)
drawer.fillcolor("red")
drawer.begin_fill()
drawer.circle(50)
drawer.end_fill()
drawer.goto(-20, -235)
drawer.write("BUY", font=('Arial', 15, 'normal'))

# create turtle for line graph
graph = trtl.Turtle("classic") 
graph.pensize(5)
graph.penup()
graph.hideturtle()

# set start value of stock
xpos = -250
ypos = random.randint(-50, 100)
starty = ypos
graph.goto(xpos, ypos)
graph.showturtle()

# up method for graph to go up a random amount
def up():
  graph.pencolor("green")
  graph.goto(graph.xcor() + 5, graph.ycor() + random.randint(1,10))
  time.sleep(0.1)
# down method for graph to go down a random amount
def down():
  graph.pencolor("red")
  graph.goto(graph.xcor() + 5, graph.ycor() - random.randint(1,10))
  time.sleep(0.1)

# start graph
graph.pendown()

# boolean for case that graph overshoots and fails 
failed = False

# define click method when buy button is clicked, go up 2 times
def click(x, y):
  for n in range(2):
    up()

# while graph is within bounds, always go down 
while(graph.xcor() < 250 and graph.ycor() > -95 and graph.ycor() < 200):
  # goes down automatically
  down()

  # if graph exceeds the upper bounds, it is considered a failed investment
  if(graph.ycor() > 200):
    failed = True
  
  # graph goes up when screen clicked
  wn.onscreenclick(click)

# end graph once it has reached boundary
graph.hideturtle()
title.hideturtle()
graph.penup()

# calculate profit (end - start)
profit = graph.ycor() - starty

# determine end message based on if loss/profit
if(profit > 0):
  message = "You earned"
elif(profit < 0):
  message = "You lost"
  profit = profit*-1

# write end message
drawer.goto(-75, 300)
drawer.write(message + " $" + str(profit), font=('Roboto', 15, 'normal'))

# if failed, write "you broke wall street" message
if(failed):
  drawer.goto(-170, 270)
  drawer.write("But... you broke Wall Street, caused an economic recession, and lost it all.", font=('Roboto', 8, 'normal'))

wn.mainloop()