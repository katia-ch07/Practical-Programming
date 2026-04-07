#student progress tracker 

#first import libraries 
import tkinter as tk  #GUI creation (python software foundation, 2024)

#this is main app class 
class App(tk.Tk):
    def __init__(self):
        super().__init__() #start the tkinter window properly
        
        #window  setting
        self.title("Student Progress Tracker")
        self.geometry("800x600")

        #simple title label
        title = tk.Label(self, text="Student Tracker", font=("Arial", 18))
        title.pack(pady=20)

#run program 
if __name__ == "__main__":
    app = App()
    app.mainloop()