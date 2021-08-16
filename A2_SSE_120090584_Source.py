import turtle
import time as ttt
import random
import sys

player,hide,monster,hide2 = turtle.Turtle('square'),turtle.Turtle('square'),turtle.Turtle('square'),turtle.Turtle('square')
player.color('red','green')
player.penup()
player_head = turtle.Turtle('square')
player_head.color('green','red')
player_head.penup()
player_head.stamp()
hide.color('white')
playerdirection = 'forward'
stampscount,snakeLength,time,left,right,g_flag = 0,5,0,620/2-40,660/2-40,True
g_monsterPosition = (-200,-200)   
monster.penup()
monster.goto(g_monsterPosition[0],g_monsterPosition[1])
monster.stamp()
g_fruits,g_grows = [],[ i+1 for i in range(9)]    #it is a series of fruits,everyposition should be in the form of (x,y)
hide2.color('white')
hide2.penup()
hide2.goto(g_monsterPosition[0],g_monsterPosition[1])   
hide2.goto(g_monsterPosition[0],g_monsterPosition[1])  
hide3 = turtle.Turtle('square')
hide3.color('white')
hide3.penup()           
gameMap = turtle.Screen()
gameMap.setup(580,660)#give the screen size, direction is a vector which is also in the form of (x,y)
motion,contact,timer,drawPen = turtle.Turtle(),turtle.Turtle(),turtle.Turtle(),turtle.Turtle()
drawPen.hideturtle()  
gameMap.tracer(0)
context = 'right'
playerStampsPosition = []
contactnumber = 0
snakemove = False

def up():
    global playerdirection,context,snakemove
    playerdirection = 'up'
    context = 'up'
    snakemove = True
def down():
    global playerdirection,context,snakemove
    playerdirection = 'down'
    context = 'down'
    snakemove = True
def left1():
    global playerdirection,context,snakemove
    playerdirection = 'left'
    context = 'left'
    snakemove = True
def right1():
    global playerdirection,context,snakemove
    playerdirection = 'right'
    context = 'right'
    snakemove = True
def space():
    global snakemove
    snakemove = not snakemove
def getDirection():
    turtle.onkey(up,'Up')
    turtle.onkey(down,'Down')
    turtle.onkey(left1,'Left')
    turtle.onkey(right1,'Right')
    turtle.onkey(space,'space')

def stampCountAdd(position):
    global stampscount, playerStampsPosition
    player.stamp()
    stampscount += 1
    playerStampsPosition.append(position)

def stampCountMinu():
    global stampscount,playerStampsPosition
    player.clearstamps(1)
    stampscount -= 1
    playerStampsPosition.pop(0)

def moveMonster(direction):#move monster
    speed = 15
    directionlist = {'up':(0,speed),'down':(0,-speed),'right':(speed,0),'left':(-speed,0)}
    temp = monster.pos()
    monster.goto(temp[0] + directionlist[direction][0],temp[1] + directionlist[direction][1])
    monster.stamp()
    monster.clearstamps(1)
    
def move(direction = 'forward',speed = 20):
    global playerStampsPosition
    if stampscount < snakeLength:
        speed = 15
    directionlist = {'up':(0,speed),'down':(0,-speed),'right':(speed,0),'left':(-speed,0),'forward':None}
    PositionNow = player.pos()
    if directionlist[direction] != None:
        PositionNext = (PositionNow[0]+directionlist[direction][0],PositionNow[1]+directionlist[direction][1])
        if outRange(PositionNext) == False:
            player.goto(PositionNext)
            stampCountAdd(player.pos())
            if stampscount > snakeLength: 
                stampCountMinu()
    else: 
        player.fd(20)
        if outRange(player.pos()):
            player.back(20)
        else:
            stampCountAdd(player.pos())
            if stampscount > snakeLength: 
                stampCountMinu()

def drawtime():
    global g_flag
    global playerdirection
    global time
    global snakeLength
    if not g_flag:
        drawmotion()
        getDirection()
        if snakemove:
            move(playerdirection)
        time += 1
        time1 = time/2
        timer.undo()
        timer.write('%d'%time1,font=('Arial',14,'normal'))
        colidposition = colid(player.pos(),g_fruits,monster.pos())
        if colidposition != None or len(g_fruits) == 0:
            a = Judge(colidposition,monster.pos(),g_fruits)
            if a == None:
                player.clearstamps(-1)
                player.stamp()
            elif a > 0 :
                snakeLength += a 
                player.clearstamps(-1)
                player.stamp()
            elif a == False:
                drawPen.goto(player.pos())
                drawPen.write('you lose')
                ttt.sleep(3)
                sys.exit()
                
        moveMonster(findDirection(player.pos(),monster.pos()))
        drawcontact()
        player_head.goto(player.pos())
        player_head.stamp()
        player_head.clearstamps(1)
        turtle.ontimer(drawtime,t=500)


def inipen(PEN,n):
    PEN.hideturtle()
    PEN.penup()
    PEN.goto(-left+n,right-40)

def outRange(position):#if outrange return true
    if position[0]>left or position[0]<(-left) or position[1] > (right-40) or position[1]<(-right):
        return True
    else:
        return False

def getclick(x,y):#if click then pause changed into continue
    global g_flag
    g_flag = not g_flag
    a.clear()
    if not g_flag:
        drawtime()#to the main loop

def drawMenu():#give a menu
    width = left*2
    hight = right*2
    drawPen.penup()
    drawPen.goto(-left,-right)
    drawPen.pendown()
    for i in range(2):
        drawPen.forward(width)
        drawPen.left(90)
        drawPen.forward(hight)
        drawPen.left(90)
    gameMap.update()
    drawPen.penup()
    drawPen.goto(-left+40,right-40)
    drawPen.pendown()
    drawPen.write('contact:',font=('Arial',14,'normal'))
    drawPen.penup()
    drawPen.forward(150)
    drawPen.write('time:',font=('Arial',14,'normal'))
    drawPen.forward(150)
    drawPen.write('motion:',font=('Arial',14,'normal'))
    drawPen.penup()
    drawPen.goto(-left,right-40)
    drawPen.pendown()
    drawPen.forward(width)

def repeat(aList,temp):#if there are two points which are too close
    if len(aList) == 0 or temp == None:
        return False
    else:
        for i in aList:
            if abs(temp[0]-i[0])<20 and abs(temp[1]-i[1])<20:
                return True
        return False

def drawmotion():
    global g_flag,context
    if g_flag == True:
        motion.undo()
        motion.write('pause',font=('Arial',14,'normal'))
    else:
        motion.undo()
        motion.write(context,font=('Arial',14,'normal'))
   
def colid(playerPostion,fruitPosition,mosterPosition):
    colidvalue = 20    #when the distance in x or y direction less than this value, colid
    temp1 = playerPostion
    temp2 = fruitPosition.copy()
    temp2.append(mosterPosition)
    colidpen = turtle.Turtle()
    colidpen,turtle.hideturtle()
    for i in range(len(temp2)):
        if abs(temp2[i][0]-temp1[0])<=colidvalue and (abs(temp2[i][1]-temp1[1]+10))<=colidvalue:# if colid with sometiong
            colidpen.penup()
            colidpen.goto(temp2[i][0]+7,temp2[i][1]+14)
            colidpen.shape('square')
            colidpen.color('white')
            colidpen.shapesize(1,1,1)
            colidpen.stamp()
            return temp2[i]#return colid with where(position)

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
            return 'down'#the dir of monster should point to player

def Judge(position,monsterPosition, fruitPosition): #judge wether the player is win or lose, activate only when colid
    #the position is from colid, if the colid with monster, player lose
    global stampscount,snakeLength
    if position == monsterPosition:
        return False
    else:
        if len(fruitPosition) == 0 and stampscount == snakeLength:
            drawPen.goto(player.pos())
            drawPen.write('you win')
            ttt.sleep(3)
            sys.exit()

        if len(fruitPosition) != 0:
            for i in range(len(fruitPosition)):
                if position == fruitPosition[i]:
                    grow = g_grows[i]
                    fruitPosition.remove(position)
                    g_grows.remove(grow)
                    return grow


def drawcontact():
    colidvalue = 15
    global contactnumber, playerStampsPosition,monster
    monsterposition = monster.pos()
    for i in playerStampsPosition:
        if abs(i[0]-monsterposition[0])<=colidvalue and (abs(i[1]-monsterposition[1]))<=colidvalue:
            contactnumber += 1
            contact.undo()
            contact.write('%d'%(contactnumber),font=('Arial',14,'normal'))
            break


inipen(timer,250)
inipen(motion,420)
inipen(contact,120)
drawMenu()
timer.write('0',font=('Arial',14,'normal'))
motion.write('pause',font=('Arial',14,'normal'))
contact.write('0',font=('Arial',14,'normal'))

a = turtle.Turtle()
a.penup()
a.goto(-left+40,right-100)
a.hideturtle()
a.write('A saliteta game.\nAfter reading this you can click any where to start game,\nclick again to stop whole system,\nand click space key to stop the move of snake')

for i in range(9):
    temp = None
    x = random.randint(-left+40,left-40)
    y = random.randint(-right,right-80)
    temp = [x,y]
    while repeat(g_fruits,temp):
        x = random.randint(-left+40,left-40)
        y = random.randint(-right,right-80)#new border
        temp = [x,y]
    g_fruits.append(temp)

gameMap.tracer(0)
gameMap.listen()
for i in range(len(g_fruits)):
    drawPen.penup()
    drawPen.goto(g_fruits[i][0],g_fruits[i][1])
    drawPen.pendown()
    drawPen.write('%d'%(i+1),font=('Arial',12,'normal'))
gameMap.onscreenclick(getclick)#game start
gameMap.mainloop()  