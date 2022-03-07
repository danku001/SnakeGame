"""
Snake game using turtle

"""

import turtle
import random

#Define Program Constants
WIDTH = 500
HEIGHT = 500
DELAY = 400 # Milliseconds
FOOD_SIZE = 20

offsets = {
    'up':(0,20),
    'down':(0,-20),
    'left':(-20,0),
    'right':(20,0),
    }

def food_col():
    """placing the food and having snake eat food"""
    global food_pos
    if get_dist(snake[-1], food_pos) < 10:
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False

def get_random_food_pos():
    """Randomly place food at random x and y position"""
    x = random.randint(-WIDTH/2 + FOOD_SIZE, WIDTH/2 - FOOD_SIZE)
    y = random.randint(-HEIGHT/2 + FOOD_SIZE, HEIGHT/2 - FOOD_SIZE)

    return (x,y)

def get_dist(pos1,pos2):
    """Calculate distance between 2 points"""
    x1,y1 = pos1
    x2,y2 = pos2

    dist = ((y2-y1)**2 + (x2-x1)**2)**0.5

    return dist


def go_up():
    """key binding for up"""
    global snake_direction
    if snake_direction != 'down':
        snake_direction = 'up'

def go_right():
    """key binding for right"""
    global snake_direction
    if snake_direction != 'left':
        snake_direction = 'right'

def go_down():
    """key binding for down"""
    global snake_direction
    if snake_direction != 'up':
        snake_direction = 'down'

def go_left():
    """key binding for left"""
    global snake_direction
    if snake_direction != 'right':
        snake_direction = 'left'

def game_loop():
    """game loop and logic"""
    stamper.clearstamps() #clears screen, gets rid of all stamps

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    #check collisions
    if (new_head in snake) or (new_head[0] < - WIDTH/2) or (new_head[0] > WIDTH/2) \
       or (new_head[1] < - HEIGHT/2) or (new_head[1] > HEIGHT/2):

        turtle.bye()

    else: 
        #Add new head to snake body.
        snake.append(new_head)

        if not food_col():
            #keep snake same length unless fed
            #Remove last segment of snake
            snake.pop(0)    #removing the 0th element of snake


        #Draw snake
        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        #refresh screen
        screen.update()

        #rinse and repeat
        turtle.ontimer(game_loop, DELAY)






#Create a screen or window where the drawing will be done
screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)  # Set the dimensions of the Turtle Graphics window
screen.title("Snake vers.1")# Name the sub window that pops up
screen.bgcolor("pink")      # Changes the background color to pink
screen.tracer(False)         # Turns off automatic automation

# Event Handlers
screen.listen() # listening for events
# keys to listen for
screen.onkey(go_up,'Up')
screen.onkey(go_right,'Right')
screen.onkey(go_down, 'Down')
screen.onkey(go_left,'Left')

#Create a turtle object to do your bidding
stamper = turtle.Turtle()
stamper.shape('square')
stamper.penup()             # Will not draw on screen as turtle moves

#create a snake as a list of lists.
snake = [[0,0],[20,0],[40,0],[60,0]]
# Default snake direction
snake_direction = 'up'

#Draw snake
for segment in snake:
    stamper.goto(segment[0],segment[1])
    stamper.stamp()

# Food
food = turtle.Turtle()
food.shape('circle')
food.color('blue')
food.shapesize(FOOD_SIZE/20)
food.penup()
food_pos = get_random_food_pos()
food.goto(food_pos)

#set animation in motion
game_loop()


#necesary in order for close to work
turtle.done()
