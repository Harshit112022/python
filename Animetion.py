import turtle
def Animetion():
        for i in range(4):
            turtle.right(90)
            turtle.forward(100)

Animetion()
turtle.shape("triangle")
turtle.Screen().exitonclick()

import heroes
print(heroes.gen())
import turtle
def Animetion():
    for _ in range(10):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()
Animetion()
turtle.Screen()
turtle.Screen().exitonclick()

import turtle
'''
for _ in range(3):
     turtle.forward(100)
     turtle.right(120)
for _ in range(4):
     turtle.forward(100)
     turtle.right(90)
for _ in range(5):
    turtle.forward(95)
    turtle.forward(4)
    turtle.right(72)

for _ in range(6):
    turtle.forward(99)
    turtle.right(60)
    '''

turtle.Screen().exitonclick()
import turtle
from turtle import Turtle,Screen
def move_forward():
    turtle.forward(10)
turtle.Screen().listen()
turtle.Screen().onkey(key="space",fun=move_forward)
turtle.Screen().exitonclick()

