import datetime

now = datetime.datetime.now()

def setup():
    size(1000, 500)
    ellipse((displayWidth/2) - 50, (displayHeight/2) - 50, 100, 100)
    clock = Clock("basic")
    clock.displayTime()
class Clock():
    def __init__(self, type):
        self.type = type 
    def displayTime(d):
        if type == "basic":
            ellipse((displayWidth/2) - 50, (displayHeight/2) - 50, 100, 100)
    # def displayDate():
        
