# Naomi Weissberg
# Created: Oct. 21, 2021
# halloween turtle

import turtle
import random
import time

# set up
window = turtle.Screen()
window.setup(1000,750)
window.title("halloween turtle")
suke = turtle.Turtle()

suke.speed(10)
suke.shape('turtle')

#randomize the size of the drawing
scale = random.uniform(2,7)

# draw body

suke.penup()
suke.goto(18*scale,-50*scale)

suke.pencolor('green')
suke.fillcolor('green')
suke.begin_fill()

def draw_oval(radius, turtle):
    suke.left(45)
    for i in range(2):
        turtle.circle(radius,90)
        turtle.circle(radius//2,90)

suke.pendown()
draw_oval(50*scale, suke)
suke.end_fill()

suke.speed(0)

#draw arms

for a in range(4):
    suke.penup()
    suke.goto(0,-14*scale)
    suke.left(90)
    suke.pendown()
    suke.pensize(15*scale)
    suke.forward(40*scale)

#draw head

suke.goto(0,0)
suke.pensize(15*scale)
suke.setheading(90)
suke.forward(40*scale)
suke.right(90)
suke.forward(5*scale)

suke.begin_fill()
draw_oval(15*scale, suke)
suke.end_fill()

suke.hideturtle()

# tail

suke.penup()
suke.goto(0,-50*scale)
suke.setheading(270)
mult = 10
suke.pendown()
while mult >= 1:
    suke.pensize(mult*scale)
    suke.forward(2*scale)
    mult -= 1

# blackout

time.sleep(1)
suke.pensize(10000)
for color in ('blue', 'yellow', 'black'):
    suke.pencolor(color)
    suke.forward(0)
time.sleep(0.5)
    
# mouth

suke.penup()
suke.color('white')
suke.goto(0,0)
suke.setheading(90)
suke.forward(45*scale)
suke.pensize(20*scale)
suke.pendown()
suke.forward(0)

suke.penup()
suke.color('black')
suke.forward(2*scale)
suke.pensize(20*scale)
suke.pendown()
suke.forward(0)
suke.penup()

# red eyes
              
suke.pensize(scale)
suke.color('red')
suke.fillcolor('red')

suke.goto(0,0)
suke.setheading(90)
suke.forward(50*scale)

def red_eye(turtle):
    turtle.pendown()
    suke.setheading(0)
    turtle.begin_fill()
    turtle.circle(3*scale)
    turtle.end_fill()
    turtle.penup()

# right eye
suke.setheading(0)
suke.forward(6*scale)
red_eye(suke)

# left eye
suke.setheading(180)
suke.forward(12*scale)
red_eye(suke)

# add text

t_font_list = ['Arial', 'Courier', 'Times New Roman']
t_font = t_font_list[random.randint(0,2)]

t_size = random.randint(7,40)

t_type_list = ['normal', 'bold', 'italic']
t_type = t_type_list[random.randint(0,2)]

style = (t_font, t_size, t_type)

suke.goto(0,-20*scale)
suke.color('red')
suke.write('h a p p y h a l l o w e e n', font=style, align='center')

# finish
turtle.mainloop()
