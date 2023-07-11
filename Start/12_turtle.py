#import turtle

#turtle.shape("turtle")
#turtle.bgcolor("yellow")

#turtle.shape("turtle")
#turtle.forward(100)
#turtle.left(90)
#turtle.forward(100)
#turtle.left(90)
#turtle.forward(100)
#turtle.left(90)
#turtle.forward(100)
#turtle.left(90)

#t = turtle.Turtle()
#t.shape("turtle")
#t.forward(100)
#t.left(120)
#t.forward(100)
#t.left(120)
#t.forward(100)
#t.left(120)

#turtle.color("yellow")
#t = turtle.Turtle()
#for i in range(6) :
#    t.forward(100)
#    t.right(360/i)

#from turtle import *
#shape("turtle")
#color("blue")
#write("동그라미 시작")
#penup()
#goto(-50, -50)
#pendown()
#circle(100)

#import turtle as t
#t.color("green")
#t.begin_fill()
#again = 11
#
#for i in range(again) :
#    t.forward(50)
#    t.left(360/again)
#t.end_fill()

#import turtle
#t1 = turtle.Turtle()
#t1.shape("turtle")
#t1.color("blue")
#t1.setx(100)
#
#t2 = turtle.Turtle()
#t2.shape("turtle")
#t2.color("purple")
#t2.sety(100)

from turtle import *
shape("turtle")
bgcolor("blue")
speed(0)
colors = ["red", "yellow", "green", "purple"]
pensize(2)
degree = 10

for i in range(1, 300) :
    pencolor(colors[i%4])
    forward(i)
    left(90+degree)

mainloop()


