import pgzrun
import pygame
from random import randint

#Set the screen size
WIDTH = 800
HEIGHT = 600

#get the balloons ready
balloon = Actor("balloon")
balloon.pos = 400, 300

#Prepare the obstacles
bird = Actor("bird-up")
bird.pos = randint(800, 1600), randint(10, 200)

house = Actor("house")
house.pos = randint(800, 1600), 460

tree = Actor("tree")
tree.pos = randint(800, 1600), 450

#Create global variables
bird_up = True
up = False
game_over = False
score = 0
number_of_updates = 0

scores = []

#Manage high scores
def update_high_scores():
    global score, scores
    screen.draw.text("HIGH SCORES", (350, 10), color="black")
    y = 175
    position = 1
    for high_score in scores:
        screen.draw.text(str(position) + "." + high_score, (350, y), color="black")
        y += 25
        position += 1
        
    file = r"C:\Dhiness\Python\Balloon proj\high-score.txt"
    scores = []
    with open (filename, "r") as file:
        line = file.readline()
        high_scores = line.split()
        for high_score in high_socres:
            if(score > int(high_score)):
                scores.append(str(score) + " ")
                score = int(high_scores)
            else:
                scores.append(str(high_scores) + " ")
    with open(filename, "w") as file:
        for high_score in scores:
            file.write(high-score)
        
    pass

def display_high_scores():
    pass

#create the draw() function
def draw():
    #Fullscreen function
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((800, 700),pygame.RESIZABLE)
    
    screen.blit("background", (0, 0))
    if not game_over:
        balloon.draw()
        bird.draw()
        house.draw()
        tree.draw()
        screen.draw.text("Score: " + str(score), (700, 5), color="black")
    else:
        display_high_scores()
    pass

#Reacting to mouse clicks
def on_mouse_down():
    global up
    up = True
    balloon.y -= 50

def on_mouse_up():
    global up
    up = False

#Make the Bird flap
def flap():
    global bird_up
    if bird_up:
        bird.images = "bird-down"
        bird_up = False
    else:
        bird.image = "bird-up"
        bird_up = True

#Create the update() function
def update():
    global game_over, score, number_of_updates
    if not game_over:
        if not up:
            balloon.y += 1

            if bird.x > 0:
                bird.x -= 4
                if number_of_updates == 9:
                    flap()
                    number_of_updates = 0
                else:
                    number_of_updates += 1
            else:
                bird.x = randint(800, 1600)
                bird.y = randint(10, 200)
                score += 1
                number_of_updates = 0

            #Move the house
            if house.right > 0:
                house.x -= 2
            else:
                house.x = randint(800, 1600)
                score += 1

            #Move the tree
            if tree.right > 0:
                tree.x -= 2
            else:
                tree.x = randint(800, 1600)
                score += 1

            #keep it steady
            if balloon.top < 0 or balloon.bottom > 560:
                gamew_over = True
                update_high_scores()

            #Handle collsions with obstacles
            if balloon.collidepoint(bird.x, bird.y) or \
               balloon.collidepoint(house.x, house.y) or \
               balloon.collidepoint(tree.x, tree.y):
                game_over = True
                update_high_scores()

pgzrun.go()
