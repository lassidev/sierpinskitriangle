import turtle
import random

turtle.setup(1000, 1000)
screen = turtle.Screen()

# uncomment for faster drawing (disables real-time), also check line 41
# screen.tracer(0)

triangle = turtle.Turtle()
triangle.color("black")
triangle.penup()
triangle.speed(0) 

#Main triangle
triangle.goto(-450,-450)
triangle.dot(1)
a = triangle.position()
triangle.forward(900) # draw base
triangle.dot(1)
b = triangle.position()
triangle.left(120)
triangle.forward(900) # top point
c = triangle.position()
triangle.dot(1)
triangle.left(120)
triangle.forward(900) # back to starting

# first drawn point
triangle.goto(0, -450)
triangle.dot(1)

for i in range(25000):
    mainpoints = [a, b, c]
    randomchoice = random.choice(mainpoints) # randomly select one of the main triangle points
    distanceto = triangle.distance(randomchoice) 
    triangle.setheading(triangle.towards(randomchoice))
    triangle.forward((distanceto/2))
    triangle.dot(1)

# uncomment for faster drawing (disables real-time)
#screen.update()

turtle.mainloop() # dont close the window after completion
