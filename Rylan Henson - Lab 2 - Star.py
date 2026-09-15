# Rylan Henson - Lab 2 - Star.py
# Draws a five-pointed star with the turtle.

import turtle


def drawStar(t, sideLength):
    """Draw a five-pointed star.

    Each point is made by moving forward and turning 144 degrees (the exterior
    angle for a five-pointed star). Repeating this five times closes the shape.
    """
    for _ in range(5):
        t.forward(sideLength)
        t.right(144)


def main():
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.color("gold")

    drawStar(t, 200)

    window.exitonclick()


main()
