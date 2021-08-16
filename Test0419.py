import random
import turtle
import sys

g_grows = [1,2,3]
def Judge(position,monsterPosition, fruitPosition): #judge wether the player is win or lose, activate only when colid
    #the position is from colid, if the colid with monster, player lose
    if position == monsterPosition:
        return False
    else:
        for i in range(len(fruitPosition)):
            if position == fruitPosition[i]:
                grow = g_grows[i]
                fruitPosition.remove((position))
                g_grows.remove(i+1)
                if len(fruitPosition) == 0:
                    return True
                else:
                    return grow

def colid(playerPostion,fruitPosition,mosterPosition):
    colidvalue = 20    #when the distance in x or y direction less than this value, colid
    temp1 = playerPostion
    temp2 = fruitPosition.copy()
    temp2.append(mosterPosition)
    for i in range(len(temp2)):
        if abs(temp2[i][0]-temp1[0])<=colidvalue and abs(temp2[i][1]-temp1[1])<=colidvalue:
            return temp2[i]
#return colid with where(position)
playpos = (0,0)
fruitpos = [(40,40),(1520,20),(10,10)]
monsterpos = (200,200)
a = colid(playpos,fruitpos,monsterpos)
print(colid(playpos,fruitpos,monsterpos))
a = Judge(a,monsterpos,fruitpos)
print(a)
print(fruitpos)
print(g_grows)
