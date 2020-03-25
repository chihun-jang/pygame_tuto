import pygame
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

size = [1000,1000]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
print(clock)
FPS = 60  # Frames per second.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
cnt = 0
mylist = [[500,500],[500,500]]

screen.fill(WHITE)
while True:
    clock.tick(3)
    cnt += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("Player moved up!")
                mylist[1] = [500,500-cnt]
            elif event.key == pygame.K_LEFT:
                print("Player moved left!")
                mylist[1] = [500-cnt,500]
            elif event.key == pygame.K_DOWN:
                print("Player moved down!")
                mylist[1] = [500,500+cnt]
            elif event.key == pygame.K_RIGHT:
                print("Player moved right!")
                mylist[1] = [500+cnt,500]
                mylist[0] = [500+cnt-20,500]

    pygame.draw.aalines(screen, BLUE, False, [[cnt-20,cnt-20],[cnt,cnt]] ,False)
    pygame.display.update()
    pygame.display.flip()

