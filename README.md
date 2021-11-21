# Auto Mouse Mover 🖱️

Small and easy python script to stop the system from locking. Made for individuals working in the IT field who use the laptop provided by their employer and have no control over screen lock time.
***Works on Windows and Linux.***

Due to security reasons, installing third-party software for mouse moving purposes may not be an option. This is where this script comes in handy.

The intention behind creating this script is **NOT** to keep this running and slack off. My machine and workspace lag like crazy when the machine locks. I am left with no option to restart the system. Please use the script to avoid similar problems and not make yourself look available when you are not. 

## Usage

**Step 1)** Clone this repository by using the command: `git clone https://github.com/Aadityajoshi151/Auto-Mouse-Mover.git`. If git is not installed, [download](https://github.com/Aadityajoshi151/Auto-Mouse-Mover/archive/refs/heads/master.zip "download") the project zip file and extract it.

**Step 2)** Open a command prompt in the project directory. Enter the command: `pip install -r requirements.txt`

**Step 3)** Execute the command `python master.py` (Windows) or `python3 master.py` (Linux).

**NOTE:** Currently the cursor moves in every 2 minutes. I will be adding the functionality where users can give custom input.

## TODOs and Improvements
- Custom user input
- Adding a counter (Cursor moved x times) **REQUIRED?**
- Displaying move coordinates (Cursor moved to x,y) **REQUIRED?**
- Tkinter GUI for the same script
