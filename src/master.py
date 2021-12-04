from tkinter import *
from tkinter import ttk

class AutoMouseMoverGUI:
#user defined functions will go here
    def __init__(self,app):
        #User defined elements will go here
        # self.butt = ttk.Button(app,text="Test")
        # self.butt.pack()
        self.duration = StringVar()
        self.input_frame = ttk.Frame(app)
        self.input_frame.grid(row=0, column=0)

        self.number_input = ttk.Entry(self.input_frame, justify=CENTER)
        self.number_input.grid(row=0,column=0,padx=10,pady=10)

        self.second_radiobtn = Radiobutton(self.input_frame,text="Seconds",variable=self.duration,value="seconds")
        self.second_radiobtn.grid(row=1,column=0, sticky="W")

        self.minute_radiobtn = Radiobutton(self.input_frame,text="Minutes",variable=self.duration,value="minutes")
        self.minute_radiobtn.grid(row=2,column=0, sticky="W")
        print(self.duration.get())

def main():
    root = Tk()
    root.title("Auto Mouse Mover")
    root.geometry("200x200")
    root.resizable("False","False")
    obj = AutoMouseMoverGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()      
