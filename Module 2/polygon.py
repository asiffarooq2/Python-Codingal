import turtle

# Create turtle
pen = turtle.Turtle()

# Number of sides
sides = int(input("Enter the number of sides: "))
length = 100

# Calculate angle
angle = 360 / sides

# Draw polygon
for i in range(sides):
    pen.forward(length)
    pen.right(angle)

turtle.done()
