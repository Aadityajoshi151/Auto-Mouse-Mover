from screeninfo import get_monitors
import autopy
import random
import schedule
import time
import argparse

parser = argparse.ArgumentParser(description= "Small and easy python script to move the mouse cursor and stop the system from locking. Made for individuals working in the IT field who use the laptop provided by their employer and have no control over screen lock time.")
parser.add_argument("-n", type=int, required=True, help="Number of Hours/minutes/seconds")

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-s',action='store_const', dest='type', const='s')
group.add_argument('-m',action='store_const', dest='type', const='m')
group.add_argument('-H',action='store_const', dest='type', const='H')

args = parser.parse_args()

monitors_list = get_monitors()
width = getattr(monitors_list[0],'width') 
height = getattr(monitors_list[0],'height')

def moveMouseCursor():
    autopy.mouse.smooth_move(random.randint(0,width), random.randint(0,height))

if args.type == 's':
    schedule.every(args.n).seconds.do(moveMouseCursor)
elif args.type == "m":
    schedule.every(args.n).minutes.do(moveMouseCursor)
else:
    schedule.every(args.n).hours.do(moveMouseCursor)

print("Auto Mouse Mover Running")
print("Press Ctrl+C To Stop")

if __name__ == "__main__":
    while(True):
        schedule.run_pending()
        time.sleep(1)
