from tkinter import *
from tkinter import ttk

class AutoMouseMoverGUI:
#user defined functions will go here
    def __init__(self,app):
        #User defined elements will go here
        self.butt = ttk.Button(app,text="Test")
        self.butt.pack()

def main():
    root = Tk()
    root.title("Auto Mouse Mover")
    root.geometry("200x200")
    root.resizable("False","False")
    obj = AutoMouseMoverGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()      
