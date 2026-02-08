import turtle
turtle.Screen().bgcolor("Blue")
turtle.Screen().setup(600,600)
poly=turtle.Turtle()

side=36
lenn = 10
angle = 360.0 / side

for i in range(side):
    poly.forward(lenn)
    poly.right(angle)

turtle.done()