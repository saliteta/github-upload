import turtle
import random

temp = [i for i in range(9)]
random.shuffle(temp)
g_fruits = []                           #it is a series of position
g_grows = [ i for i in range(9)]
g_monsterPosition = (-200,-200)         #everyposition should be in the form of (x,y)
g_refreshrate = 500                     #refresh rate should be a constant number
g_squrelen = 40                         #length of the squer should be a constant
g_screensizex = 1240
g_screensizey = 720
left = g_screensizex/2-40
right = g_screensizey/2-40
g_flag = True

gameMap = turtle.Screen()
gameMap.setup(g_screensizex,g_screensizey)
drawPen = turtle.Turtle()
drawPen.hideturtle()
player = {'poslist':[[0,0]],'growlen':0,'direction': 'up'}    #player is a kind of dicionary to be a subsitution of class
timer = turtle.Turtle()                     #direction is a vector which is also in the form of (x,y)
time = 0
motion = turtle.Turtle()
contact = turtle.Turtle()
gameMap.tracer(0)
g_snakeSpeed = 40

def inipen(PEN,n):
    PEN.hideturtle()
    PEN.penup()
    PEN.goto(-left+n,right-40)

def outRange(position):
    if position[0]>left-40 or position[0]<(-left+40) or position[1] > (right-80)/2 or position[1]/2<(-right):
        return True
    else:
        return False

def getclick(x,y):
    global g_flag
    g_flag = not g_flag
    drawmotion()

def drawMenu():#give a menu
    width = left*2
    hight = right*2
    drawPen.penup()
    drawPen.goto(-left,-right)
    drawPen.pendown()
    drawPen.forward(width)
    drawPen.left(90)
    drawPen.forward(hight)
    drawPen.left(90)
    drawPen.forward(width)
    drawPen.left(90)
    drawPen.forward(hight)
    gameMap.update()
    drawPen.penup()
    drawPen.goto(-left+40,right-40)
    drawPen.pendown()
    drawPen.write('contact:',font=('Arial',26,'normal'))
    drawPen.penup()
    drawPen.left(90)
    drawPen.forward(400)
    drawPen.write('time:',font=('Arial',26,'normal'))
    drawPen.forward(400)
    drawPen.write('motion:',font=('Arial',26,'normal'))
    drawPen.penup()
    drawPen.goto(-left,right-40)
    drawPen.pendown()
    drawPen.forward(width)

def drawtime():
    global time
    time += 1
    timer.undo()
    move()
    timer.write('%d'%time,font=('Arial',26,'normal'))
    turtle.ontimer(drawtime,t=1000)

def drawmotion():
    global g_flag
    if g_flag:
        motion.undo()
        motion.write('pause',font=('Arial',26,'normal'))
    else:
        motion.undo()
        motion.write('continue',font=('Arial',26,'normal'))

def drawcontact():
    pass
    
def repeat(aList,temp):#if there are two points which are too close
    if len(aList) == 0 or temp == None:
        return False
    else:
    
        for i in aList:
            if abs(temp[0]-i[0])<g_snakeSpeed and abs(temp[1]-i[1])<g_snakeSpeed:
                return True
        return False



def moveMonster(direction):#move monster
    speed = 40
    directionlist = {'up':(0,speed),'down':(0,-speed),'right':(speed,0),'left':(-speed,0)}
    temp = g_monsterPosition
    g_monsterPosition[0] = directionlist[direction][0]+g_monsterPosition[0]
    g_monsterPosition[1] = directionlist[direction][1]+g_monsterPosition[1]
    if outRange(g_monsterPosition):
        g_monsterPosition = temp
        return

def colid(playerPostion,fruitPosition,mosterPosition):#first list them in x increasing way and find the two number close to snake 
    colidvalue = 20    #when the distance in x or y direction less than this value, colid
    temp1 = playerPostion[0]
    temp2 = fruitPosition.copy()
    temp2.append(mosterPosition)
    for i in range(len(temp2)):
        if abs(temp2[i][0]-temp1[0])<=colidvalue and abs(temp2[i][1]-temp1[1])<=colidvalue:
            return temp2[i]
#return colid with where(position)

def findDirection(playerPosition, monsterPosition):
    tempx = playerPosition[0]-monsterPosition[0]
    tempy = playerPosition[1]-monsterPosition[1]
    if abs(tempx)>abs(tempy):
        if tempx < 0:
            return 'left'
        else:
            return 'right'
    else:
        if tempy > 0:
            return 'up'
        else:
            return 'down'
    #the dir of monster should point to player


def Judge(position,monsterPosition, fruitPosition): #judge wether the player is win or lose, activate only when colid
    #the position is from colid, if the colid with monster, player lose
    if position == monsterPosition:
        return False
    else:
        for i in range(len(fruitPosition)):
            if position == fruitPosition[i]:
                grow = g_grows[i]
                fruitPosition.remove(i)
                g_grows.remove(i)
                if len(fruitPosition) == 0:
                    return True
                else:
                    return grow

def up():
    player['direction'] = 'up'
def down():
    player['direction'] = 'down'
def left1():
    player['direction'] = 'left'
def right1():
    player['direction'] = 'right'
def getDirection():
    turtle.onkey(up,'Up')
    turtle.onkey(down,'Down')
    turtle.onkey(left1,'Left')
    turtle.onkey(right1,'Right')

for i in range(9):
    temp = None
    x = random.randint(-left-40,left-40)
    y = random.randint(-right,right-80)
    temp = [x,y]
    while repeat(g_fruits,temp):
        x = random.randint(-left-40,left-40)
        y = random.randint(-right,right-80)#new border
        temp = [x,y]
    g_fruits.append(temp)


inipen(timer,600)
inipen(motion,1000)
inipen(contact,200)
timer.write('0',font=('Arial',26,'normal'))
motion.write('pause',font=('Arial',26,'normal'))
contact.write('0',font=('Arial',26,'normal'))
gameMap.tracer(0)
gameMap.listen()
gameMap.onscreenclick(getclick)
turtle.ontimer(drawtime,t=1000)
drawMenu()
for i in range(len(g_fruits)):
    drawPen.penup()
    drawPen.goto(g_fruits[i][0],g_fruits[i][1])
    drawPen.pendown()
    drawPen.write('%d'%(i+1),font=('Arial',26,'normal'))

gameMap.mainloop()