import turtle
from tkinter import *

slope = eval(input("Enter a slope value : "))
y_intercept = eval(input("Enter a y-intercept value : "))
window = turtle.Screen()
window.title("Line Drawing")
point = turtle.Turtle()
point.speed(9999999999)

def draw_board():
    point.color("lightgray")
    point.penup()
    point.right(90)
    point.goto(-400, 400)
    point.pendown()
    for i in range(32):
        point.forward(800)
        point.left(90)
        point.forward(12.5)
        point.left(90)
        point.forward(800)
        point.right(90)
        point.forward(12.5)
        point.right(90)
    point.penup()
    point.left(90)
    point.goto(-400, 400)
    point.pendown()
    for i in range(32):
        point.forward(800)
        point.right(90)
        point.forward(12.5)
        point.right(90)
        point.forward(800)
        point.left(90)
        point.forward(12.5)
        point.left(90)
    point.color("black")
    point.penup()
    point.goto(0, 0)
    point.pendown()
    for i in range(2):
        for j in range(4):
            point.forward(400)
            point.left(90)
        for k in range(4):
            point.forward(400)
            point.right(90)
        point.left(180)

def draw_line():
    point.goto(0, y_intercept * 12.5)
    point.color("red")
    x = 0
    y = y_intercept
    for i in range(50):
        x += 12.5
        y = slope * x + y_intercept * 12.5
        point.goto(x, y)
    point.penup()
    point.goto(0, y_intercept * 12.5)
    point.pendown()
    x = 0
    y = y_intercept * 12.5
    for i in range(50):
        x -= 12.5
        y = slope * x + y_intercept * 12.5
        point.goto(x, y)
    point.penup()
    point.goto(0, y_intercept * 12.5)
    point.shape("circle")

draw_board()
draw_line()

root = Tk()
root.title("Your Equation")
root.resizable(width = False, height = False)
equation = Label(root, text = "y = " + str(slope) + "x + " + str(y_intercept), font = ("Font", 50))
equation.pack()
root.mainloop()
turtle.done()