from screeninfo import get_monitors
import autopy
import random

monitors_list = get_monitors()
width = getattr(monitors_list[0],'width') 
height = getattr(monitors_list[0],'height')

def moveMouseCursor():
    autopy.mouse.smooth_move(random.randint(0,width), random.randint(0,height))
