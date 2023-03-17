from turtle import *
from random import randrange
from freegames import vector,square

#vector used for postion a point
food =vector(0,0)
snake = [vector(10,0)]
aim =vector(0,-10)

def change(x,y):
    aim.x=x #declare x-axis
    aim.y=y #declare y-axis

def inside(head):
    return -200 <head.x< 300 and -200 <head.y < 200

def move():
    head=snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x,head.y,9,'red')
        update()
        return
    snake.append(head)
    

    if head==food:
        print('snake',len(snake))
        food.x=randrange(-15,20)*10
        food.y=randrange(-15,20)*10
        
    else:
        snake.pop(0)
    clear()

    for body in snake:
        square(body.x,body.y,9,'yellow')


    square(food.x,food.y,9,'red')
    update()
    ontimer(move, 100)

hideturtle()
tracer(False)
listen()
onkey(lambda:change(10,0),'Right')
onkey(lambda:change(-10,0),'Left')
onkey(lambda:change(0,10),'Up')
onkey(lambda:change(0,-10),'Down')


move()
done()





















