import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 800))

gameCheck = "active"
over = False

walls = []

#player stats
x = 50
y = 775
size = 20
speeds = 4
color = (255, 255, 255)

#clock
clock = pygame.time.Clock()
time = pygame.time.get_ticks()

def initWalls():
    walls.append(pygame.Rect(0, 0, 30, 800))
    walls.append(pygame.Rect(0, 0, 30, 800))
    walls.append(pygame.Rect(100, 30, 30, 830))
    walls.append(pygame.Rect(200, 0, 30, 750))
    walls.append(pygame.Rect(200, 725, 600, 30))
    walls.append(pygame.Rect(770, 575, 30, 150))
    walls.append(pygame.Rect(770, 550, 200, 30))
    walls.append(pygame.Rect(940, 550, 30, 200))
    walls.append(pygame.Rect(855, 615, 30, 200))
    walls.append(pygame.Rect(940, 745, 100, 30))
    walls.append(pygame.Rect(1040, 50, 30, 725))
    walls.append(pygame.Rect(1060, 700, 100, 30))
    walls.append(pygame.Rect(1120, 600, 100, 30))
    walls.append(pygame.Rect(1060, 525, 100, 30))
    walls.append(pygame.Rect(1120, 450, 100, 30))
    walls.append(pygame.Rect(1060, 390, 100, 30))
    walls.append(pygame.Rect(1120, 320, 100, 30))
    walls.append(pygame.Rect(1060, 250, 115, 30))
    walls.append(pygame.Rect(1120, 187, 100, 30))
    walls.append(pygame.Rect(1060, 120, 115, 30))
    walls.append(pygame.Rect(1100, 40, 140, 30))


def movePlayer():
    global x
    global y
    press = pygame.key.get_pressed()
    if press[pygame.K_w]:
        y -= speeds
        if y < 0:
            y = 0
    if press[pygame.K_a]:
        x -= speeds
        if x < 0:
            x = 0
    if press[pygame.K_s]:
        y += speeds
        if y > 780:
            y = 780
    if press[pygame.K_d]:
        x += speeds
        if x > 1180:
            x = 1180

def draw():
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 1200, 800), 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, size, size), 0)

    for w in walls:
        pygame.draw.rect(screen, (255, 0, 0), w, 0)
initWalls()

def checkCollision():
    global walls
    global x
    global y
    for w in walls:
        if w.colliderect(pygame.Rect(x, y, size, size)):
            x = 50
            y = 775




while not over:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = True

    if gameCheck == "active":
        draw()
        checkCollision()
        movePlayer()



    pygame.display.flip()