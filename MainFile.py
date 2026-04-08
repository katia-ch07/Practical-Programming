#student progress tracker 

#first import libraries 
import tkinter as tk  #GUI creation (python software foundation, 2024)
from tkinter import messagebox  # for popups (Python Software Foundation, 2024)
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


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data,file,indent=4)


# function to calculate average (GeeksforGeeks, 2024)
def calculate_average(grades):
    return sum(grades) / len(grades)

#this is main app class 
class App(tk.Tk):
    def __init__(self):
        super().__init__() #start the tkinter window properly

        #window  setting
        self.title("Student Progress Tracker")
        self.geometry("800x600")

        self.db = load_data()

        #input section
        frame= tk.Frame(self)
        frame.pack(pady=20)

        #name input
        tk.Label(frame, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(frame)
        self.name_entry.grid(row=0, column=1)

        # grade input
        tk.Label(frame, text="Grade:").grid(row=1, column=0)
        self.grade_entry = tk.Entry(frame)
        self.grade_entry.grid(row=1, column=1)

        # add button
        tk.Button(self, text="Add Student", command=self.add_student).pack(pady=10)

    def add_student(self):
        # get values from user (freeCodeCamp, 2022)
        name = self.name_entry.get()
        grade = self.grade_entry.get()

        #check if name is empty (W3Schools, 2024)

        if name == "":
            messagebox.showerror("Error", "Name cannot be empty")
            return

        # check if grade is a number (GeeksforGeeks, 2024)
        try:
            grade = float(grade)
        except:
            messagebox.showerror("Error", "Grade must be a number")
            return

        # check grade range
        if grade < 0 or grade > 100:
            messagebox.showerror("Error", "Grade must be between 0 and 100")
            return
        
         # create student id (simple way) (Programiz, 2024)
        student_id = "S" + str(len(self.db) + 1)

        # store student data (dictionary structure)
        self.db[student_id] = {
            "name": name,
            "grades": [grade]  # list so we can add more later
        }

        save_data(self.db)  # save to file

        # calculate average after adding
        avg = calculate_average(self.db[student_id]["grades"])

        messagebox.showinfo("Success", f"Student added (Avg: {avg:.1f})")  # feedback

        print(self.db)  # for debug



#run program 
if __name__ == "__main__":
    app = App()
    app.mainloop()