import turtle
turtle.speed(5)
turtle.shape("turtle")
turtle.hideturtle()
degree = 0

for i in range(12):
    turtle.right(degree)
    turtle.forward(100)
    turtle.stamp()
    turtle.home()
    degree += 30
turtle.exitonclick()