import pygame
import urllib2

######################################
########## Global variables ##########
######################################
UIFont = None

########################################
########## Method definitions ##########
########################################
def init():
    global UIFont
    
    pygame.init()
    UIFont = pygame.font.SysFont(None, 30)

def draw():
    global UIFont
    
    screen.fill(BLACK)

    label = UIFont.render("-Hub controller user interface-", 1, RED)
    # TODO Calculate the center of the screen here.
    screen.blit(label, (250, 100))

    # TODO The code to update the auth label should be in update() rather than draw.
    authCodeText = "Current auth code: " + getCurrentAuthCode()
    authCodeLabel = UIFont.render(authCodeText, 1, RED)
    screen.blit(authCodeLabel, (300, 300))

    pygame.display.flip()

def update():
    print("Updating!")

def getCurrentAuthCode():
    authCode = urllib2.urlopen("http://127.0.0.1:8081/get_current_auth_token").read()
    return authCode

########################################
########## Main program logic ##########
########################################

# Define some colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0,   255, 0)
RED =   (255, 0,   0)

init()

# Set screen dimensions (width, height).
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Hub Controller UI")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates.
clock = pygame.time.Clock()

# ========== Main program loop ==========
while not done:
    # ========== Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    update()
    draw()

    # --- Limit to 60 FPS
    clock.tick(60)

# Close the window and quit.
pygame.quit()
