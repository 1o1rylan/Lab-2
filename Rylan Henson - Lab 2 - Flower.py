
# Rylan Henson - Lab 2 - Flower.py
# Draws a flower by repeating a square many times, turning between each square.

import turtle


def drawSquare(t, sideLength):
    """Draw one square with the given side length."""
    for _ in range(4):
        t.forward(sideLength)
        t.right(90)


def drawFlower(t, numSquares):
    """Draw a flower made of numSquares squares.

    The turtle turns 360 / numSquares degrees between each square so that the
    squares are spread evenly around a full circle.
    """
    turnAngle = 360 / numSquares
    for _ in range(numSquares):
        drawSquare(t, 100)
        t.right(turnAngle)


def main():
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.color("purple")

    drawFlower(t, 36)

    window.exitonclick()


main()
