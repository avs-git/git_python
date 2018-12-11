# coding UTF-8

import turtle
import random
import math

import mrobot

PHI = 360 / 7
R = 50



def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def make_circle(x, y, radius, color):
    gotoxy(x, y)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def create_pistol(x, y):
    make_circle(x, y, 80, 'white')
    make_circle(x, y + 160, 5, 'red')
    for i in range(0, 7):
        phi_rad = PHI * i * math.pi / 180.0
        make_circle(math.sin(phi_rad) * R, math.cos(phi_rad) * R + 60, 22, 'white')

def make_turn(start, turns):
    for i in range(start, turns):
        phi_rad = PHI * i * math.pi / 180.0
        make_circle(math.sin(phi_rad) * R, math.cos(phi_rad) * R + 60, 22, 'brown')
        make_circle(math.sin(phi_rad) * R, math.cos(phi_rad) * R + 60, 22, 'white')
    make_circle(math.sin(phi_rad) * R, math.cos(phi_rad) * R + 60, 22, 'brown')
    if i % 7 == 0:
        gotoxy(-150, 250)
        turtle.write("Вы проиграли!", font = ("Arial", 18, "normal"))
        if random.randrange(0,10) % 2 == 0:
            answer = turtle.textinput('Дубль'+ mrobot.dupl_random(),'y/n')
            
        else:
            answer = turtle.textinput('Удалили' + mrobot.del_random(),'y/n')
            
    else:
        gotoxy(-150, 250)
        turtle.write("Повезло!", font=("Arial", 18, "normal"))
    return i % 7


turtle.speed(0)

create_pistol(0, 0)
answer = ''
start = 0
while answer != 'n':
    answer = turtle.textinput('Играем','y/n')
    start = make_turn(start, 8)



