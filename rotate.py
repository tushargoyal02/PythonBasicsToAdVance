import rotatescreen
import time

screen = rotatescreen.get_primary_display()

for i in range(4):
    # left
    time.sleep(2) 
    screen.set_portrait_flipped()

    # flip
    time.sleep(2)
    screen.set_landscape_flipped()

    # right
    time.sleep(2) 
    screen.set_portrait()

    # Normal 
    time.sleep(2)
    screen.set_landscape()