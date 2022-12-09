import pygame as pg
import sys

pg.init()
WIDTH = 600
HEIGHT = 600
display = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Tron")
clock = pg.time.Clock()

class bike:
    def __init__(self, color, dark_color, coords):
        self.x=coords[0] 
        self.y=coords[1]
        self.color = color
        self.dark_color = dark_color
        pg.draw.rect(display, color=color, rect=(coords[0],coords[1],10,10))
        self.trace=[coords] # initial coordinates
    
    def move(self, xm, ym):
        self.trace.append([self.x,self.y])
        self.x = self.x + xm
        self.y = self.y + ym
    
    def draw(self):
        # Redraw last trace as regular. Draw current trace as dark
        if self.x not in self.trace and self.y not in self.trace:
            pg.draw.rect(display, color=self.dark_color, rect=(self.x,self.y,10,10))
            pg.draw.rect(display, color=self.color, rect=(self.trace[-1][-0], self.trace[-1][1],10,10))

# Takes RGB for bright color, RGB for dark color, and initial coordinates
bike1 = bike((52, 152, 219), (33, 97, 140), [50,300])
# Starts moving to the right
xm1=10
ym1=0

bike2 = bike((220, 118, 51), (186, 74, 0), [550,300])
# Starts moving to the left
xm2 = -10
ym2 = 0

font = pg.font.Font("freesansbold.ttf",50)
while True:
    for event in pg.event.get():
        # Player selects a direction to move on
        # Validates a player doesn't try to go on reverse
        if event.type == pg.KEYDOWN:
            # PLAYER 1 KEYS
            if event.key == pg.K_w:
                if xm1 != 0 and ym1 != 10:
                    xm1=0
                    ym1=-10
            if event.key == pg.K_d:
                if xm1 != -10 and ym1 != 0:
                    xm1=10
                    ym1=0
            if event.key == pg.K_a:
                if xm1 != 10 and ym1 != 0:
                    xm1=-10
                    ym1=0
            if event.key == pg.K_s:
                if xm1 != 0 and ym1 != -10:
                    xm1=0
                    ym1=10
            # PLAYER 2 KEYS
            if event.key == pg.K_UP:
                if xm2 != 0 and ym2 != 10:
                    xm2=0
                    ym2=-10
            if event.key == pg.K_DOWN:
                if xm2 != 0 and ym2 != -10:
                    xm2=0
                    ym2=10
            if event.key == pg.K_LEFT:
                if xm2 != 10 and ym2 != 0:
                    xm2=-10
                    ym2=0
            if event.key == pg.K_RIGHT:
                if xm2 != -10 and ym2 != 0:
                    xm2=10
                    ym2=0
    
    # Move in the direction stated
    bike1.move(xm1,ym1)
    bike1.draw()
    bike2.move(xm2,ym2)
    bike2.draw()

    # Get current player position
    bike1_actual = [bike1.x,bike1.y]
    bike2_actual = [bike2.x,bike2.y]

    # Collision checking
    # Each player can collide with any of the two traces or the borders of the game
    if bike1_actual == bike2_actual: # mutual collision
        # Displaying text
        text = font.render('Both players crashed!', True, 'white')
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 2)
        display.blit(text, textRect)

        # Game over
        pg.display.update()
        pg.time.delay(2000)
        pg.quit()
        sys.exit()
    elif (bike1_actual in bike1.trace or bike1_actual in bike2.trace or
            abs(bike1.x) == 600 or abs(bike1.y) == 600 or bike1.x == -10 or
            bike1.y == -10): 
        # Displaying text
        text = font.render('Player 1 crashed!', True, 'white')
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 2)
        display.blit(text, textRect)

        # Game over
        pg.display.update()
        pg.time.delay(2000)
        pg.quit()
        sys.exit()
    elif (bike2_actual in bike2.trace or bike2_actual in bike1.trace or
            abs(bike2.x) == 590 or abs(bike2.y) == 590 or bike2.x == 0 or
            bike2.y == 0):
        # Displaying text
        text = font.render('Player 2 crashed!', True, 'white')
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 2)
        display.blit(text, textRect)

        # Game over
        pg.display.update()
        print("bike2 crashed")
        pg.time.delay(2000)
        pg.quit()
        sys.exit()
    else:
        # No collisions detected
        pg.display.update()
        clock.tick(10)