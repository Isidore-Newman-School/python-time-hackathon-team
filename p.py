import datetime
import pygame
now = datetime.datetime.now()

def main():
    pygame.init()
    pygame.display.init()

class Clock():
    def __init__(self):
        print("hi")
    def displayTime():
        pygame.font.Font.render(datetime.datetime.now())
    def displayDate():
        pygame.font.Font.render(str(now.day) + "-" + str(now.month) + "-" + str(now.year))
