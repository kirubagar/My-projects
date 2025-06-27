import random
import turtle
from turtle import Turtle, Screen
color_list = [ (133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209)]

turtle.colormode(255)

tim = Turtle()
tim.penup()
tim.speed("normal")


dot_size = 20
spacing = 50
start_x = -150
start_y = -150

tim.setheading(0)
tim.goto(start_x, start_y)

for row in range(10):
    for col in range(10):
        tim.dot(dot_size, random.choice(color_list))
        tim.forward(spacing)
    tim.setheading(90)
    tim.forward(spacing)
    tim.setheading(180)
    tim.forward(spacing * 10)
    tim.setheading(0)

screen = Screen()
screen.exitonclick()