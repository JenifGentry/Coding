import turtle
window =turtle.Screen()
turtle.speed(2)
n=int(input("Enter no of times to draw helix circle "))
for i in range(n):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
