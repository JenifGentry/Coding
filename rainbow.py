import turtle
rainbow_colors =['violet', 'indigo', 'blue', 'green', 'yellow', 'orange','red']
win=turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    win.pencolor(rainbow_colors[x%7])
    win.width(x/100+1)
    win.forward(x)
    win.left(50)
