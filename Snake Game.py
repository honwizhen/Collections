from re import S
import pygame
import sys
import os
import random
import math

pygame.init()
pygame.display.set_caption("Snake Game")
pygame.font.init()
random.speed()

speed = 0.30
SNAKE_SIZE = 9
APPLE_SIZE = SNAKE_SIZE
SEPARATION = 10
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
FPS = 25
KEY = {'UP':1, 'DOWN':2, 'LEFT':3, 'RIGHT':4}

# Initialize 
scree = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH),pygame.HWSURFACE)
# Hw surface = hardware surface. It refers to using memory on the video card for storing.
# Draws as opposed to main memory.

# Resources
score_font = pygame.font.Font(None,38)
score_numb_font = pygame.font.Font(None,28)
game_over_font = pygame.font.Font(None,48)
play_again_font = score_numb_font
score_msg = score_font.render("Score : ",1,pygame.Color("green"))
score_msg_size = score_font.size("Score")
background_color = pygame.Color(0,0,0)     # background color will be set to black.
black = pygame.Color(0,0,0)

# Clock
gameClock = pygame.time.Clock()

# to check boundaries and making sure it is not limit. So it can pass through side to the other.

def checkCollision(posA, As, posB, Bs): 
    if(posA.x < posB.x+Bs and posA.x+As > posB.x and posA.y < posB.y+Bs and posA.y+As > posB.y):
        return True
    return False

def checkLimits(snake):
    if(snake.x > SCREEN_WIDTH):
        snake.x = SNAKE_SIZE
    if(snake.x < 0):
        snake.x = SCREEN_WIDTH - SNAKE_SIZE
    if(snake.y > SCREEN_HEIGHT):
        snake.y = SNAKE_SIZE
    if(snake.y < 0):
        snake.y = SCREEN_HEIGHT - SNAKE_SIZE

# Create a class for the apple(food)

class Apple:
    def __init__(self,x,y,state):
        self.x = x
        self.y = y
        self.state = state
        self.color = pygame.color.Color("orange")

    def draw(self,screen):
        pygame.draw.rect(screen, self.color, (self x, self y, APPLE_SIZE, APPLE_SIZE ),0)

class segment:
    # initially snake will move in up direction
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.dircetion = KEY["UP"]
        self.color = "white"

class snake:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.dricetion = KEY["UP"]
        self.stack = []
        self.stack.append(self)
        blackBox = segment(self.x, self.y + SEPARATION)
        blackBox.direction = KEY["UP"]
        blackBox.color = "NULL"
        self.stack.append(blackBox)

# The movement of the sanke
    def move(self, snake):
        last_element = len(self.stack) - 1
        while(last_element != 0):
            self.stack[last_element].direction = self.stack[last_element].direction
            self.stack[last_element].x = self.stack[last_element -1].x
            self.stack[last_element].y = self.stack[last_element -1].y
            last_element -=1 
        if (len(self,stack) < 2):
            last_segment = self
        else:
            last_segment = self.stack.pop(last_element)
        last_segment.direction = self.stack[0].direction
        if(self.stack[0].direction == KEY["UP"]):
            last_segment.y = self.stack[0].y - (SPEED + FPS)
        elif(self.stack[0].direction == KEY["UP"]):
            last_segment.y = self.stack[0].y + (SPEED + FPS)
        elif(self.stack[0].direction == KEY["UP"]):
            last_segment.x = self.stack[0].x - (SPEED + FPS)
        elif(self.stack[0].direction == KEY["UP"]):
            last_segment.x = self.stack[0].x + (SPEED + FPS)
        self.stack.insert(0,last_segment)

    def getHead(self): # head of the snake
        return(self.stack[0]) # It will be always 0 index
    
    # now when they eat apple it grows 1 more

    def grow(self):
        last_element = len(self.stack) - 1
        self.stack[last_element].direction = self.stack[last_element].direction
        if(self.stack[last_element].direction == KEY["UP"]):
            newSegment = segment(self.stack[last_element].x, self.stack[last_element].y - SNAKE_SIZE)
            blackBox = segment(newSegment.x, newSegment.y - SEPARATION)
        
        elif(self.stack[last_element].direction == KEY["DOWN"]):
            newSegment = segment(self.stack[last_element].x, self.stack[last_element].y + SNAKE_SIZE)
            blackBox = segment(newSegment.x, newSegment.y + SEPARATION)
        
        elif(self.stack[last_element].direction == KEY["LEFT"]):
            newSegment = segment(self.stack[last_element].x - SNAKE_SIZE, self.stack[last_element].y)
            blackBox = segment(newSegment.x - SEPARATION, newSegment.y)
        
        elif(self.stack[last_element].direction == KEY["RIGHT"]):
            newSegment = segment(self.stack[last_element].x + SNAKE_SIZE, self.stack[last_element].y)
            blackBox = segment(newSegment.x + SEPARATION, newSegment.y)
        
        blackBox.color = "NULL"
        self.stack.append(newSegment)
        self.stack.append(blackBox)

    def iterateSegments(self, delta):
        pass

    def

    

# We will define keys

def getKey():
    """
    This function is incharge to giving the keys and sending the reaction program.
    """
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                return KEY["UP"]
            elif event.key == pygame.K_DOWN:
                return KEY["DOWN"]
            elif event.key == pygame.K_LEFT:
                return KEY["LEFT"]
            elif event.key == pygame.K_RIGHT:
                return KEY["RIGHT"]
            # To exit 
            elif event.key == pygame.K_ESCAPE:
                return 'exit'
            # To play again
            elif event.key == pygame.K_y:
                return 'yes'
            # If not
            elif event.key == pygame.K_n:
                return 'no'
        if event.typ == pygame.QUIT:
            sys.ext(0)

def endGame():
    """
    The function presents the ability of the user at the end of the game,
    in order to proceed, to play again or end terminate.
    """

    message = game_over_font.render("Game Over",1,pygame.Color("white"))
    message_paly_again = play_again_font.render("Play Again ? (Y/N)",1,pygame.Color("green"))
    screen.blit(message,(320,240))
    screen.blit(message_play_again,(320+12,240+40))

    pygame.display.flip()

    mKey = getKey()
    while (mKey != "exit"):
        if (mKey == "yes"):
            main()
        elif(mKey == "no"):
            break
        mKey = getKey()
        gameClock.tick(FPS)
    sys.exit(0)

def drawScore(score):
    score_numb = score_numb_font.render(str(score),1,pygame.Color("red"))
    screen.blit(score_msg, (SCREEN_WIDTH - score_msg_size[0]-60,10))
    screen.blit(score_numb, (SCREEN_WIDTH - 45,14))

def drawGameTime(gameTime):
    game_time = score_font.render("Time:", 1, pygame.Color("white"))
    game_time_numb = score_numb_font.render(str(gameTime/1000),1,pygame.Color("white"))
    screen.blit(game_time,(30,10))
    screen.blit(game_time_numb,105,14))

def exitScreen():
    pass

def main():
    score = 0