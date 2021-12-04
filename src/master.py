from tkinter import *
from tkinter import ttk

class AutoMouseMoverGUI:
#user defined functions will go here
    def __init__(self,app):
        #User defined elements will go here
        # self.butt = ttk.Button(app,text="Test")
        # self.butt.pack()
        self.duration = StringVar()
        self.duration.set("minutes")
        self.input_frame = ttk.Frame(app)
        self.input_frame.grid(row=0, column=0)

        self.number_input = ttk.Entry(self.input_frame, justify=CENTER, width=10)
        self.number_input.grid(row=0,column=0,padx=10,pady=10)

        self.actionbtn = ttk.Button(self.input_frame,text="Hello World")
        self.actionbtn.grid(row=0,column=1,padx=10,pady=2 ,sticky="E")

        # self.actionbtn = ttk.Button(self.input_frame,text="Hello World")
        # self.actionbtn.grid(row=1,column=1,padx=10,pady=2 ,sticky="E")

        self.second_radiobtn = ttk.Radiobutton(self.input_frame,text="Seconds",variable=self.duration,value="seconds")
        self.second_radiobtn.grid(row=1,column=0,padx=10,pady=2 ,sticky="W")

        self.minute_radiobtn = ttk.Radiobutton(self.input_frame,text="Minutes",variable=self.duration,value="minutes", state=ACTIVE)
        self.minute_radiobtn.grid(row=2,column=0,padx=10,pady=2 , sticky="W")

        self.hours_radiobtn = ttk.Radiobutton(self.input_frame,text="Hours",variable=self.duration,value="hours")
        self.hours_radiobtn.grid(row=3,column=0,padx=10,pady=2 , sticky="W")

        

        print(self.duration.get())

def main():
    root = Tk()
    root.title("Auto Mouse Mover")
    root.geometry("200x120")
    root.resizable("False","False")
    obj = AutoMouseMoverGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()      
