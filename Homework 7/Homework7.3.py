import turtle

turtle.shape("turtle")
turtle.speed(10)
turtle.left(120)
for i in range(5):
    turtle.right(60)
    turtle.circle(-100)
    if i == 4:
        turtle.right(60)
        turtle.circle(-100, 180)
turtle.exitonclick()
