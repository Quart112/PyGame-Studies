import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)
blue = (0,0,255)
orange = (255,165,0)

display_width = 800
display_height = 600

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Fazer Arcade")

block_width = 20
block_height = 10
fazer_width = 3
fazer_height = 15
FPS = 15

native_x = display_width / 2
native_y = display_height / 8


gameExit = False

print(gameExit)

def spaceship(screen, color, x, y, block_width, block_height):
    pygame.draw.rect(screen, color, [x, y, block_width, block_height])

def spaceship_2(screen, color, x, y, block_width, block_height):
    pygame.draw.rect(screen, color, [display_width - x, display_height - y, block_width, block_height])

def fazers(screen, color, x, y, block_width, block_height):
    pygame.draw.rect(screen, color, [x, y, block_width, block_height])

def draw_fazers(i):
    if i == 1:
        fazers(gameDisplay, orange, native_x, native_y, fazer_width, fazer_height)




while not gameExit:
    gameDisplay.fill(white)
    spaceship(gameDisplay, blue, native_x, native_y, block_width, block_height)

    check = False









    #fazers(gameDisplay, orange, native_x, native_y, fazer_width, fazer_height)
    #spaceship_2(gameDisplay, red, native_x, native_y, block_width, block_height)
    pygame.display.update()


    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                native_x -= 10
            if event.key == pygame.K_RIGHT:
                native_x += 10
            if event.key == pygame.K_UP:
                native_y -= 10
            if event.key == pygame.K_DOWN:
                native_y += 10
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == pygame.K_x:
                check = True
                print(check)

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    while check :
        fazers(gameDisplay, orange, native_x, native_y, fazer_width, fazer_height)
        clock.tick(FPS)

    clock.tick(FPS)
    pygame.display.update()



