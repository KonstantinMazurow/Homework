import turtle

step = 10
for i in range(20):
    for k in range(2):
        turtle.forward(step)
        turtle.right(90)
        step += 10
turtle.exitonclick()

