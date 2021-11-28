from screeninfo import get_monitors
import autopy
import random
import schedule
import time
import argparse

parser = argparse.ArgumentParser(description= "Small and easy python script to move the mouse cursor and stop the system from locking. Made for individuals working in the IT field who use the laptop provided by their employer and have no control over screen lock time.")

monitors_list = get_monitors()
width = getattr(monitors_list[0],'width') 
height = getattr(monitors_list[0],'height')

def moveMouseCursor():
    autopy.mouse.smooth_move(random.randint(0,width), random.randint(0,height))

print("Auto Mouse Mover Running")
print("Press Ctrl+C To Stop")

schedule.every(2).minutes.do(moveMouseCursor)

if __name__ == "__main__":
    while(True):
        schedule.run_pending()
        time.sleep(1)