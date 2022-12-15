import turtle

b = turtle.Turtle()
b.penup()
b.goto(-150,0)
b.pendown()
b.pensize(20)
b.pencolor("yellow")
b.circle(50)
b.left(180)
b.circle(50)

b.penup()
b.goto(0,100)
b.pendown()
b.right
b.circle(50,360)

b.circle(50,270)
b.left(180)
b.forward(60)
for x in range(120):
    b.forward(1)
    b.right(1)

b.penup()
b.goto(100,0)
b.pendown()
for x in range(180):
    b.forward(1)
    b.left(1)








sc = turtle.Screen().exitonclick()