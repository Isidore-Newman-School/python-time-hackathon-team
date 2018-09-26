import sys, pygame, pygame.font
from time import localtime
from datetime import timedelta, datetime
from math import sin, cos, pi
pygame.init
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

size = width, height = 1000,600
black = 0, 0, 0
white = 255, 255, 255
center = 150
radius = 100
dHours = 5

class Clock():
    def __init__(self, deltahours, center, radius):
        self.c = center
        self.r = radius
        self.type = type
        self.delta = timedelta(hours = deltahours)
    def drawHands(self):
        T = datetime.timetuple(datetime.utcnow()-self.delta)
        x,x,x,h,m,s,x,x,x = T
        print(str(h) +":" + str(m))
        # get time

        angle = -pi/2 + pi/6 * (h + m/60.0)
        x, y = (cos(angle)*self.r*2/3) + self.c, (sin(angle)*self.r*2/3) + self.c
        pygame.draw.line(screen, black, (self.c, self.c), (x, y), 3)
        # draw the hour handle

        angle = -pi/2 + pi/30 * (m + s/60.0)
        x, y = (cos(angle)*(self.r-10)) + self.c, (sin(angle)*(self.r-10)) + self.c
        # print("angle = "+ str(angle) +" x and y = "+ str(x1) +" "+str(y1))
        pygame.draw.line(screen, black, (self.c, self.c), (x, y), 2)
        # draw the minute handle

        angle = -pi/2 + pi/30 * s
        x, y = cos(angle)*(self.r*2/3) + self.c,sin(angle)*(self.r*2/3) + self.c
        pygame.draw.line(screen, (255, 0, 0), (self.c, self.c), (x, y), 1)
        # draw the second handle

    def redraw(self):
        pygame.draw.circle(screen, black, (self.c, self.c), self.r, 3)
        start = pi/2              # 12h is at pi/2
        step = pi/6
        for i in range(12):       # draw the minute ticks as circles
            angle =  start-i*step
            x, y = (cos(angle)*self.r) + self.c, (sin(angle)*self.r) + self.c
            pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), 5, 0)
        self.drawHands()

# def main(argv=None):
#     if argv is None:
#        argv = sys.argv
#     if len(argv) > 2:
#        try:
#            deltahours = int(argv[1])
#            sImage = (argv[2] == 'True')
#            w = int(argv[3])
#            h = int(argv[4])
#            t = (argv[5] == 'True')
#        except ValueError:
#            print ("A timezone is expected.")
#            return 1
#     else:
#        deltahours = 3
#        sImage = True
#        w = h = 400
#        t = False
#
#     root = Tk()
#     root.geometry ('+0+0')
#     # deltahours: how far are you from utc?
#     # Sometimes the clock may be run from another timezone ...
#     #clock(root,deltahours,sImage,w,h,t)
#
#     root.mainloop()

text = myfont.render("Clock", True, black)

clock = Clock(dHours, center, radius)
screen = pygame.display.set_mode(size)
screen.fill((white))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill((white))
    clock.redraw()
    screen.blit(text, (600, 300))
    pygame.display.flip()
