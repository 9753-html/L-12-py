import turtle
w=turtle.Screen()
w=turtle.Screen().bgcolor("blue")
p=turtle.Turtle()

s=0
while True:
    for i in range(6):
        p.forward(s+1)
        p.left(60)
        s=s-5
    s=s+1