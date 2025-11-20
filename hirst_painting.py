import turtle
import random
turtle.colormode(255)
tod = turtle.Turtle()
color_list = [(46, 92, 144), (243, 250, 245), (170, 13, 26), (34, 44, 62), (141, 80, 44), (228, 154, 7), (161, 57, 88), (211, 162, 101), (37, 144, 46), (68, 34, 47), (235, 219, 63), (225, 223, 4), (48, 45, 93), (22, 51, 47), (50, 40, 36), (88, 195, 171), (117, 162, 171), (247, 90, 16), (18, 96, 49), (233, 237, 244), (211, 56, 76), (155, 23, 19), (187, 143, 156), (60, 167, 91), (46, 149, 196), (226, 177, 167), (163, 209, 182), (227, 171, 180)]
tod.penup()
tod.speed("fastest")
tod.hideturtle()
tod.setheading(225)
tod.forward(300)
tod.setheading(0)
no_of_dots=100

for i in range(1,no_of_dots+1):
    tod.dot(20,random.choice(color_list))
    tod.forward(50)
    if i%10==0:
        tod.setheading(90)
        tod.forward(50)
        tod.setheading(180)
        tod.forward(500)
        tod.setheading(0)




screen = turtle.Screen()
screen.exitonclick()

