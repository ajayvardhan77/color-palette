import turtle
from turtle import Turtle, Screen
import random
from typing import List

import colorgram
from colorgram import Color

tom = Turtle()
turtle.colormode(255)  # generates random color
tom.shape("arrow")

# challenge - 1
# for i in range(4):
#     tom.fd(100)
#     tom.rt(90)
# challenge - 2
# for i in range(0, 15):
#     tom.fd(10)
#     tom.penup()
#     tom.fd(10)
#     tom.pendown()


# challenge - 3
# for i in range(3):
#     tom.fd(100)
#     tom.rt(120)
#
# for i in range(4):
#     tom.fd(100)
#     tom.rt(90)
#     tom.color("blue")
#
# for i in range(5):
#     tom.fd(100)
#     tom.rt(72)
#     tom.color("red")
#
# for i in range(6):
#     tom.fd(100)
#     tom.rt(60)
#     tom.color("orange")
#
#
# for i in range(8):
#     tom.fd(100)
#     tom.rt(45)
#     tom.color("pink")
#
# for i in range(10):
#     tom.fd(100)
#     tom.rt(36)
#     tom.color("green")


# challenge-4
# colors = ["turquoise", "spring green", "dark sea green", "floral white", "chartreuse", "SeaGreen", "IndianRed"]
# def rand_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_clr = (r, g, b)
#     return random_clr
#
#
# direction = [0, 90, 180, 270]  # 0: east etc
# tom.pensize(10)
# tom.speed("fastest")
# tom.speed("fastest")
# for i in range(300):
#     tom.color(rand_color())
#     tom.fd(30)
#     tom.setheading(random.choice(direction))

# challenge - 5

# def rand_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
#
# tom.speed("fastest")
#
#
# def draw_spirograph(size_of_gap):  # here we are lopping till the gap b/w circles is size_of_gap
#     for i in range(int(360/size_of_gap)):  # here 360 because 360 degree  makes a circle
#         tom.color(rand_color())
#         tom.circle(100)
#         tom.setheading(tom.heading() + size_of_gap)
#
#
# draw_spirograph(3)

# DAY CHALLENGE
# colorgram package: extracts colors from the image


# colors = colorgram.extract('image.jpg', 10)
# img_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     img_colors.append(new_color)
#
# print(img_colors)

color_list = [(235, 234, 231), (234, 229, 231), (236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35),
              (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46)]
a = 35
tom.home()
for i in range(10):
    for j in range(10):
        tom.dot(20, random.choice(color_list))
        tom.penup()
        tom.fd(50)
    tom.goto(0, a)
    a = a + 35


screen = Screen()
screen.exitonclick()
