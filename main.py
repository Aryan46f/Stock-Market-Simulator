import turtle as trtl
import random
import time

# set up background screen
wn = trtl.Screen()
trtl.bgcolor("lightgray")

# write title question text 
title = trtl.Turtle()
title.hideturtle()
title.penup()
title.goto(-200, 0)
title.write("Which company's stocks would you like to buy?", font=('Roboto', 12, 'normal'))
title.goto(-100, -100)
title.write("1- GME, 2- AMC, 3-BBW", font=('Roboto', 12, 'normal'))

# takes user input for company
stock = 0
while(stock < 1 or stock > 3 ):
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
title.clear()
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
drawer.speed(0)
drawer.pencolor("lightgray")
drawer.setheading(90)
drawer.forward(300)
drawer.setheading(180)
drawer.forward(500)
drawer.end_fill()
drawer.setheading(0)
drawer.pencolor("black")

# graph grid lines
drawer.penup()
drawer.pencolor("lightgray")
drawer.pensize(1)
drawer.setheading(90)
drawer.goto(-230, -100)
for vert in range(10):
  drawer.pendown()
  drawer.forward(295)
  drawer.penup()
  drawer.goto(drawer.xcor()+50, -100)
drawer.goto(-250, 195)
drawer.setheading(0)
for horiz in range(6):
  drawer.pendown()
  drawer.forward(500)
  drawer.penup()
  drawer.goto(-250, drawer.ycor()-50)

# place buy button 
drawer.setheading(0)
drawer.penup()
drawer.goto(0, -250)
drawer.fillcolor("red")
drawer.begin_fill()
drawer.circle(50)
drawer.end_fill()
drawer.goto(-20, -215)
drawer.pencolor("black")
drawer.write("BUY", font=('Arial', 15, 'normal'))

# draw wealth bar
bar = trtl.Turtle("classic")
bar.hideturtle()
bar.penup()
bar.goto(-25, -350)
bar.write("MONEY", font=('Arial', 10, 'normal'))
bar.pencolor("green")
bar.goto(-250, -325)
bar.pendown()
bar.fillcolor("green")
bar.begin_fill()
bar.forward(500)
bar.setheading(90)
bar.forward(25)
bar.setheading(180)
bar.forward(500)
bar.setheading(270)
bar.forward(25)
bar.end_fill()
bar.penup()
bar.goto(250, -325)
bar.setheading(180)

# procedure to increase red area of wealth bar 
def spend():
  bar.pencolor("red")
  while(bar.ycor() > -324 and bar.ycor() < -276):
    bar.pendown()
  if(bar.ycor() < -324 and bar.ycor() > -276):
    bar.penup()
  bar.speed(0)
  bar.fillcolor("red")
  bar.setheading(180)
  bar.begin_fill()
  bar.forward(10)
  bar.setheading(90)
  bar.forward(25)
  bar.setheading(0)
  bar.forward(10)
  bar.setheading(270)
  bar.forward(25)
  bar.end_fill()
  bar.goto(bar.xcor()-10, -325)


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
  graph.speed(0)
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

# define click method when buy button is clicked, go up 2 times, decrease wealth
def click(x, y):
  for n in range(2):
    up()
  spend()
  
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

# set up ending face turtle
face = trtl.Turtle()
face.hideturtle()
face.pensize(5)

# end face procedures
def happy():
  face.penup()
  face.speed(0)
  face.goto(0, -250)
  face.pendown()
  face.pencolor("yellow")
  face.fillcolor("yellow")
  face.begin_fill()
  face.circle(50)
  face.end_fill()

  face.penup()
  face.goto(0, -230)
  face.pencolor("black")
  face.circle(25, 275)
  face.pendown()
  face.circle(25, 170)

  face.penup()
  face.goto(-10, -190)
  face.fillcolor("black")
  face.begin_fill()
  face.circle(7)
  face.end_fill()

  face.penup()
  face.goto(20, -190)
  face.fillcolor("black")
  face.begin_fill()
  face.circle(7)
  face.end_fill()


def sad():
  face.penup()
  face.speed(0)
  face.goto(0, -250)
  face.pendown()
  face.pencolor("yellow")
  face.fillcolor("yellow")
  face.begin_fill()
  face.circle(50)
  face.end_fill()

  face.penup()
  face.goto(0, -260)
  face.pencolor("black")
  face.circle(25, 120)
  face.pendown()
  face.circle(25, 120)

  face.penup()
  face.goto(-20, -190)
  face.fillcolor("black")
  face.begin_fill()
  face.circle(7)
  face.end_fill()

  face.penup()
  face.goto(10, -190)
  face.fillcolor("black")
  face.begin_fill()
  face.circle(7)
  face.end_fill()


def angry():
  face.penup()
  face.speed(0)
  face.goto(0, -250)
  face.pendown()
  face.pencolor("red")
  face.fillcolor("red")
  face.begin_fill()
  face.circle(50)
  face.end_fill()

  face.penup()
  face.goto(0, -260)
  face.pencolor("white")
  face.circle(25, 120)
  face.pendown()
  face.circle(25, 120)

  face.penup()
  face.goto(-20, -190)
  face.fillcolor("white")
  face.begin_fill()
  face.circle(7)
  face.end_fill()

  face.penup()
  face.goto(10, -190)
  face.fillcolor("white")
  face.begin_fill()
  face.circle(7)
  face.end_fill()


# determine end message based on if loss/profit, display face
if(profit > 0 and failed != True):
  message = "You earned"
  happy()
elif(profit < 0):
  message = "You lost"
  profit = profit*-1
  sad()
else:
  message = "You earned"
  angry()

# write end message
drawer.goto(-75, 300)
drawer.write(message + " $" + str(profit), font=('Roboto', 15, 'normal'))

# if failed, write "you broke wall street" message
if(failed):
  drawer.goto(-170, 270)
  drawer.write("But... you broke Wall Street, caused an economic recession, and lost it all.", font=('Roboto', 8, 'normal'))

wn.mainloop()