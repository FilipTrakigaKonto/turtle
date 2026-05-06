import turtle
import math
import random
import colorsys

t = turtle.Turtle()
turtle.colormode(255)
t.speed(0)
t.hideturtle()
h = 0
turtle.tracer(0, 0)



def rita_triangel(sida):
    for i in range(3):
        t.forward(sida)
        t.left(120)

def sierpinski(length, depth):
    t.color(fractal_färg(depth))
    if depth == 0:
        rita_triangel(length)
    else:
        sierpinski(length/2, depth-1)
        t.forward(length/2)
        sierpinski(length/2, depth-1)
        t.backward(length/2)
        t.left(60)
        t.forward(length/2)
        t.right(60)
        sierpinski(length/2, depth-1)
        t.left(60)
        t.backward(length/2)
        t.right(60)


def fractal_färg(depth):
    global h
    h += 0.002 + depth * 0.0005

    r, g, b = colorsys.hsv_to_rgb(h % 1, 1, 1)
    return int(r * 255), int(g * 255), int(b * 255)

def main():
    t.penup()
    t.goto(-200, -150)
    t.pendown()
    t.color(fractal_färg(0))
    input_length = int(input("Ange längden på triangeln: "))
    input_depth = int(input("Ange djupet på Sierpinski-triangeln: "))
    length = input_length
    depth = input_depth
    sierpinski(length, depth)
    turtle.update()

    turtle.done()


main()