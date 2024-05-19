import turtle as tr, colorsys
import random as rn


win = tr.Screen()
pen = tr.Turtle()
pen.pensize(1)
color = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
pen.speed(0)
h = 1
n = 70

for i in range(360):
    h += 1/n
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    pen.color(c)
    pen.circle(80)
    pen.left(1)

tr.mainloop()