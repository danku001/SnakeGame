"""
Snake game using turtle

"""

import turtle
import random

#Define Program Constants
WIDTH = 500
HEIGHT = 500
DELAY = 400
food_size = 20


def move_snake():
    """moves snake"""
    stamper.clearstamps() #clears screen, gets rid of all stamps

    newHead = snake[-1].copy()
    newHead[0] += 20

    #Add new head to snake body
    snake.append(newHead)

    #Remove last segment of snake
    snake.pop(0)    #removing the 0th element of the snake


    #Draw snake
    for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()


    #refresh screen
    screen.update()

    #rinse and repeat
    turtle.ontimer(move_snake,DELAY)



#Create a screen or window where the drawing will be done
screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)  # Set the dimensions of the Turtle Graphics window
screen.title("Snake vers.1")# Name the sub window that pops up
screen.bgcolor("pink")      # Changes the background color to pink
screen.tracer(False)         # Turns off automatic automation


#Create a turtle object to do your bidding
stamper = turtle.Turtle()
stamper.shape('square')
stamper.penup()             # Will not draw on screen as turtle moves

#create a snake as a list of lists.
snake = [[0,0],[20,0],[40,0],[60,0]]

#Draw snake
for segment in snake:
    stamper.goto(segment[0],segment[1])
    stamper.stamp()


#set animation in motion
move_snake()

#necesary in order for close to work
turtle.done()
