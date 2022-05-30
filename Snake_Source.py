import turtle
import time
import random

# Global variables
g_bodymove = True
g_pendo = True
g_SnakeMove = True
g_gameContinue = False
g_eatingTest = False
g_Bodylist = [[0,0]]
g_foodlist = []
g_start = 0
g_timeused = 0
g_contacted = 0
g_finalUpdate = 0
g_foodnumber = 0
g_bodyExtend = [0]*9+[5]
g_snakeDirection = 'up'
Directions = {"up": (0, 20),"down": (0, -20),"left": (-20, 0),"right": (20, 0)}

# Basic turtles' settings
def setScreen():
    s = turtle.Screen()
    s.setup(500,500)
    s.tracer(0)
    return s
def setPen():
    pen = turtle.Turtle()
    pen.color('black')
    pen.ht()
    pen.up()
    pen.goto(-280,130)
    return pen
def setBodyPen():
    bodypen = turtle.Turtle('square')
    bodypen.color('blue','black')
    bodypen.ht()
    bodypen.up()
    return bodypen
def setSnakeHead(shape='square', color='red'):
    head = turtle.Turtle(shape)
    head.color(color)
    head.up()
    head.goto(0,0)
    head.setheading(90)
    return head
def setMonster(shape='square', color='purple'):
    monster = turtle.Turtle(shape)
    monster.color(color)
    monster.up()
    monster.goto(-150,-150)
    return monster
def setFood():
    global g_foodnumber
    if g_foodnumber < 9 and g_gameContinue:
        food = turtle.Turtle()
        food.up()
        food.ht()
        foodX = random.randint(-200,200)
        foodY = random.randint(-200,200)
        food.goto(foodX,foodY)
        food.write(str(g_foodnumber+1),False,'left',("Arial", 8, "normal"))
        g_foodlist.append(food)
        g_foodnumber += 1
    g_screen.ontimer(setFood,100)
def eatingFood():
    for food in g_foodlist:
        if g_snakeHead.distance(food) < 20:
            g_bodyExtend[g_foodlist.index(food)] = g_foodlist.index(food)+1
            food.clear()
            food.goto(1000,1000)
        if g_bodyExtend != [0]*10:
            for a in range(0,10):
                if g_bodyExtend[a] != 0:
                    g_bodyExtend[a] -= 1
            return True
    return False

# Set turtles
g_screen = setScreen()
g_bodypen = setBodyPen()
g_snakeHead = setSnakeHead()
g_monster = setMonster()
g_pen = setPen()

# Action control
def moveUp():
    global g_snakeDirection
    g_snakeHead.setheading(90)
    g_snakeDirection = "up"
def moveDown():
    global g_snakeDirection
    g_snakeHead.setheading(270)
    g_snakeDirection = "down"
def moveLeft():
    global g_snakeDirection
    g_snakeHead.setheading(180)
    g_snakeDirection = "left"
def moveRight():
    global g_snakeDirection
    g_snakeHead.setheading(0)
    g_snakeDirection = "right"
def moveSnake(posponer=200):
    x = g_snakeHead.xcor()
    y = g_snakeHead.ycor()
    if g_gameContinue and g_SnakeMove:
        if g_snakeHead.heading() == 90:
            if y <= 220:
                g_snakeHead.fd(20)
                g_bodymove = True
            else:
                g_bodymove = False
        if g_snakeHead.heading() == 270:
            if y >= -220:
                g_snakeHead.fd(20)
                g_bodymove = True
            else:
                g_bodymove = False
        if g_snakeHead.heading() == 180:
            if x >= -220:
                g_snakeHead.fd(20)
                g_bodymove = True
            else:
                g_bodymove = False
        if g_snakeHead.heading() == 0:
            if x <= 220:
                g_snakeHead.fd(20)
                g_bodymove = True
            else:
                g_bodymove = False
        g_eatingTest = eatingFood()
        global g_snakeDirection, g_Bodylist
        if g_bodymove:        
            new_head = g_Bodylist[-1].copy() 
            new_head[0] = g_Bodylist[-1][0] + Directions[g_snakeDirection][0]
            new_head[1] = g_Bodylist[-1][1] + Directions[g_snakeDirection][1]
            g_Bodylist.append(new_head)
            if not g_eatingTest:
                g_Bodylist.pop(0)
            else:
                posponer = 300
            g_bodypen.clearstamps()
            for segment in g_Bodylist:
                g_bodypen.goto(segment[0], segment[1])
                g_bodypen.stamp()
        Win()
    g_screen.update()
    g_screen.ontimer(moveSnake, posponer)
def moveMonster():
    angle = g_monster.towards(g_snakeHead.xcor(),g_snakeHead.ycor())
    time = random.randint(190,400)
    if g_gameContinue:
        if 0<=angle<=45 or 315<=angle<360:
            g_monster.setheading(0)
            g_monster.fd(20)
        elif 45<angle<=135:
            g_monster.setheading(90)
            g_monster.fd(20)
        elif 135<angle<=225:
            g_monster.setheading(180)
            g_monster.fd(20)
        elif 225<angle<315:
            g_monster.setheading(270)
            g_monster.fd(20)
        Gameover()
    g_screen.update()
    g_screen.ontimer(moveMonster,time)

# Key bound
def Clicktostart(x,y):
    g_pen.clear()
    global g_gameContinue, g_pendo
    g_gameContinue = True
    g_pendo = False
    moveUp()
    global g_start
    g_start = time.time()
    g_screen.onclick(None)
def PuaseSnake():
    global g_SnakeMove
    g_SnakeMove = False
    g_screen.onkeypress(ActiveSnake,'space')
def ActiveSnake():
    global g_SnakeMove
    g_SnakeMove = True
    g_screen.onkeypress(PuaseSnake,'space')

# Start and End
def Counter():
    global g_start
    now = time.time()
    g_timeused = int(now-g_start)

    # Count the contacts
    for body in g_Bodylist:
        if g_monster.distance(body[0],body[1])<15:
            global g_contacted
            g_contacted += 1
    if g_gameContinue:
        g_screen.title('Snake   Contacted: '+str(g_contacted)+'  Time: '+str(g_timeused))
    g_screen.ontimer(Counter,1000)
def Welcome():
    if g_pendo:
        g_pen.write(
        '''
        Welcome to Snake!
        You are going to use the 4 arrow keys to move the snake
        around the screen and use the space bar to pause it, 
        trying to consume all the food items shown in number 
        before the monster cathches you.
        Click anywhere to start the game, have fun!
        '''
        , move=False, align='left', font=("Black", 12, "normal"))
def Win():
    global g_finalUpdate
    if len(g_Bodylist) == 51:
        if g_finalUpdate < 1:
            g_finalUpdate += 1
        else:
            g_snakeHead.pencolor('red')
            g_snakeHead.write('Winnner!!!', move=False, align='left', font=("Arial", 15, "normal"))
            global g_gameContinue
            g_gameContinue = False
def Gameover():
    if g_snakeHead.distance(g_monster)<=20:
        g_monster.pencolor('red')
        g_monster.write('Game Over!!!', move=False, align='left', font=("Arial", 15, "normal"))
        global g_gameContinue
        g_gameContinue = False

if __name__ == "__main__":
    g_screen.listen()
    g_screen.onkeypress(moveUp, 'Up')
    g_screen.onkeypress(moveDown, 'Down')
    g_screen.onkeypress(moveLeft, 'Left')
    g_screen.onkeypress(moveRight,'Right')
    g_screen.onkeypress(PuaseSnake,'space')
    g_screen.onclick(Clicktostart)
    if g_gameContinue:
        g_start = time.time()
    Welcome()
    Counter()
    setFood()
    moveSnake()
    moveMonster()
    g_screen.mainloop()