from screeninfo import get_monitors
import autopy
import random
import schedule
import time
import argparse

parser = argparse.ArgumentParser(description= "Small and easy python script to move the mouse cursor and stop the system from locking. Made for individuals working in the IT field who use the laptop provided by their employer and have no control over screen lock time.")
parser.add_argument("-n", type=int, metavar="", required=True, help="Number of seconds/minutes/hours")

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-s',action='store_const', metavar="", dest='type', const='s',help="Moves the cursor in specified seconds")
group.add_argument('-m',action='store_const', metavar="",dest='type', const='m',help="Moves the cursor in specified minutes")
group.add_argument('-H',action='store_const', metavar="",dest='type', const='H',help="Moves the cursor in specified hours")

args = parser.parse_args()

monitors_list = get_monitors()
width = getattr(monitors_list[0],'width') 
height = getattr(monitors_list[0],'height')


def moveMouseCursor():
    x_coordinate = random.randint(0,width)
    y_coordinate = random.randint(0,height)
    autopy.mouse.smooth_move(x_coordinate, y_coordinate)
    

if args.type == 's':
    schedule.every(args.n).seconds.do(moveMouseCursor)
elif args.type == "m":
    schedule.every(args.n).minutes.do(moveMouseCursor)
else:
    schedule.every(args.n).hours.do(moveMouseCursor)

print("Auto Mouse Mover Running")
print(f"Mouse Will Move Every {args.n}{args.type}")
print("Press Ctrl+C To Stop")

if __name__ == "__main__":
    try:
        while(True):
            schedule.run_pending()
            time.sleep(1)
    except:
        print("Auto Mouse Mover Stopped")
