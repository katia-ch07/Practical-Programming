#student progress tracker 

#first import libraries 
import tkinter as tk  #GUI creation (python software foundation, 2024)
import json #JSON handling (Python Software Foundation, 2024)
import os #file system (Programiz, 2024)

DATA_FILE = "students.json"

#load data
def load_data():
    #we have to check if the file exists first (Real python, 2023)
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                return json.load(file)
    return {}

#this is main app class 
class App(tk.Tk):
    def __init__(self):
        super().__init__() #start the tkinter window properly
        
        #window  setting
        self.title("Student Progress Tracker")
        self.geometry("800x600")

        #simple title label
        title = tk.Label(self, text="Student Tracker", font=("Arial", 18)).pack(pady=20)

#run program 
if __name__ == "__main__":
    app = App()
    app.mainloop()
    