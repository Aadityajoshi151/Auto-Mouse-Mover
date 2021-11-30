# Auto Mouse Mover 🖱️

Small and easy python script to move the mouse cursor and stop the system from locking. Made for individuals working in the IT field who use the laptop provided by their employer and have no control over screen lock time.
***Works on Windows and Linux.***

Due to security reasons, installing third-party software for mouse moving purposes may not be an option. This is where this script comes in handy.

The intention behind creating this script is **NOT** to keep this running and slack off. My machine and workspace lag like crazy when the machine locks. I am left with no option to restart the system. Please use the script to avoid similar problems and not make yourself look available when you are not.🙂 

## Usage

**Step 1)** Clone this repository by using the command: `git clone https://github.com/Aadityajoshi151/Auto-Mouse-Mover.git`. If git is not installed, [download](https://github.com/Aadityajoshi151/Auto-Mouse-Mover/archive/refs/heads/master.zip "download") the project zip file and extract it.

**Step 2)** Open a command prompt in the project directory. Enter the command: `pip install -r requirements.txt`

**Step 3)** Use `cd src` to move in the src folder.

**Step 4)** Execute the command `python master.py -n 2 -m` (Windows) or `python3 master.py -n 2 -m` (Linux) to move mouse cursor in every 2 minutes.

The`-n` flag is used to pass the number, `-s` for seconds `-m` for minutes and `-H` for hours respectively. 

**More Examples**
 - `python master.py -n 3 -s` moves cursor every 3 seconds.
 - `python master.py -n 4 -m` moves cursor every 4 minutes.
 - `python master.py -n 2 -H` moves cursor every 2 hours.

## TODOs and Improvements
- [X] Custom user input
- [ ] Tkinter GUI for the same script
