from turtle import Turtle,Screen
tim=Turtle()
screen=Screen()

def move_forword():
    tim.forward(10)
def move_backwor():
    tim.backward(10)
def counter_clockwise():
    new_heading=tim.heading()-10
    tim.setheading(new_heading)
def clockwise():
    new_heading=tim.heading()+10
    tim.setheading(new_heading)
def clear_draw():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen.listen()
screen.onkey(move_forword,"w")
screen.onkey(move_backwor,"s")
screen.onkey(counter_clockwise,"d")
screen.onkey(clockwise,"a")
screen.onkey(clear_draw,"c")
screen.exitonclick()