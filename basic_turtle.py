import turtle
import random
import time
import math

# CONSTANTS
colors = ['red', 'navy blue', 'light green', 'purple', 'gold', 'orange', 'black', 'cyan', 'gray', 'magenta']
sayings = [
    'great time for a stroll',
    'these shoes were made for waddling',
    'helps me think, ya know?',
    'not all those who wander...',
    'beats running!',
    'ready to seize the day!',
    'onward and upward! (or at least forward)',
    'just a few more paces...'
]
turtles = 10 # MAX 10
turtle.Screen().screensize()
turtle.Screen().setup(width=800, height=600)
turtle.Screen().bgcolor('#4F42B5')
x, y = turtle.getcanvas().winfo_pointerxy()
sayingCounter = 0

def createBox():
    var_exists = 'flagged' in locals() or 'flagged' in globals()
    if not var_exists:
        flagged = "yike"
    boxMaker = turtle.Turtle()
    boxMaker.speed(50)
    boxMaker.hideturtle()
    boxMaker.color('lightgrey')
    boxMaker.pensize(1)
    boxMaker.penup()
    boxMaker.setpos(-400, 250)
    boxMaker.pendown()
    boxMaker.begin_fill()
    for i in range(2):
        boxMaker.forward(800)
        boxMaker.left(90)
        boxMaker.forward(50)
        boxMaker.left(90)
    boxMaker.end_fill()
    writingTurtle = turtle.Turtle()
    writingTurtle.hideturtle()
    writingTurtle.color('deep pink')
    style = ('Courier', 20, 'italic')
    writingTurtle.penup()
    writingTurtle.setpos(0, 258)
    currentSaying = sayings[random.randrange(0, len(sayings))]
    while currentSaying == flagged:
        currentSaying = sayings[random.randrange(0, len(sayings))]
    writingTurtle.write(currentSaying, font=style, align='center')
    flagged = currentSaying
    global sayingCounter
    sayingCounter -= 10

# GENERATING TURTLES
boys = []
for i in range(turtles):
    boys.append(turtle.Turtle())
    boys[i].hideturtle()
    boys[i].speed(6)
    boys[i].shape('turtle')
    boys[i].pensize(2)
    randomColor = random.randrange(0, len(colors))
    boys[i].color(colors[randomColor])
    colors.pop(randomColor)
    boys[i].penup()
    divisions = 360/turtles
    rand = random.randrange(divisions*i,(divisions*i)+divisions)
    boys[i].setpos(math.cos(math.radians(rand))*150, math.sin(math.radians(rand))*150)
    for x in range(0, i):
        xdiff = abs(boys[i].pos()[0] - boys[x].pos()[0])
        ydiff = abs(boys[i].pos()[1] - boys[x].pos()[1])
        while xdiff < 30 and ydiff < 30:
            rand = random.randrange(0,360)
            boys[i].setpos(math.cos(math.radians(rand))*150, math.sin(math.radians(rand))*150)
            xdiff = abs(boys[i].pos()[0] - boys[x].pos()[0])
            ydiff = abs(boys[i].pos()[1] - boys[x].pos()[1])
    boys[i].left(rand+180)
    boys[i].showturtle()

# MOVING TURTLES AND VALUES
while(True):
    currentTurtle = boys[random.randrange(0, turtles)]
    currentAction = random.randrange(0, 3)
    if currentAction == 0:
        time.sleep(0.25)
        sayingCounter += 1
    elif currentAction == 1:
        if currentTurtle.pos()[1] >= 340:
            time.sleep(0.25)
            sayingCounter += 1
        else:
            for x in range(0, boys.index(currentTurtle)):
                xdiff = abs(currentTurtle.pos()[0] - boys[x].pos()[0])
                ydiff = abs(currentTurtle.pos()[1] - boys[x].pos()[1])
                if xdiff < 30 and ydiff < 30:
                    time.sleep(0.25)
                    sayingCounter += 1
            else:
                currentTurtle.forward(10)
    else:
        currentTurn = random.randrange(0,180)
        currentTurtle.speed(2)
        if currentTurn % 2 == 0:
            currentTurtle.left(currentTurn)
        else:
            currentTurtle.right(currentTurn)
        sayingCounter += 1
        currentTurtle.speed(6)
    print(sayingCounter)
    if sayingCounter == 10:
        createBox()

turtle.Screen().exitonclick()
