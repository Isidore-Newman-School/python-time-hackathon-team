import sys, pygame, datetime
pygame.init


size = width, height = 500,500
black= 0, 0, 0
white = 255, 255, 255

class Clock():
    def __init__(self, type):
        self.type = type
    def displayTime(self):
        if self.type == "basic":
            pygame.draw.circle(screen, black, (250, 250), 150, 3)
            now = datetime.datetime.now()
            time = now.time()
            pygame.draw.line(screen, (255, 0, 0), (250, 250), end_pos,1)
        else:
            print("not basic")

clock = Clock("basic")
screen = pygame.display.set_mode(size)
screen.fill((white))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    clock.displayTime()
    pygame.display.flip()
