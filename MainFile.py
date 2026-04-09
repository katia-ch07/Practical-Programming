#student progress tracker  
# added charts for data visualisation (Matplotlib Development Team, 2024)


#first import libraries 
import tkinter as tk  #GUI creation (python software foundation, 2024)
from tkinter import messagebox, ttk # (ttk for table) for popups (Python Software Foundation, 2024)
import json #JSON handling (Python Software Foundation, 2024)
import os #file system (Programiz, 2024)
import matplotlib.pyplot as plt  # charts (Matplotlib Development Team, 2024)
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

         # search section
        search_frame = tk.Frame(self)
        search_frame.pack()

        tk.Label(search_frame, text="Search ID:").pack(side=tk.LEFT)
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side=tk.LEFT)

        tk.Button(search_frame, text="Search", command=self.search_student).pack(side=tk.LEFT)

         # sort button
        tk.Button(self, text="Sort by Average", command=self.sort_students).pack(pady=5)

        # chart button
        tk.Button(self, text="Show Chart", command=self.show_chart).pack(pady=5)

        # table
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Average"), show="headings")

        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Average", text="Average")

        self.tree.pack(fill=tk.BOTH, expand=True)

        self.refresh_table()

    def show_chart(self):
        # create simple bar chart (W3Schools, 2024)
        names = []
        averages = []

        for info in self.db.values():
            names.append(info["name"])
            averages.append(calculate_average(info["grades"]))

        fig, ax = plt.subplots()
        ax.bar(names, averages)

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def sort_students(self):
        # sort students (GeeksforGeeks, 2024)
        sorted_data = sorted(
            self.db.items(),
            key=lambda x: calculate_average(x[1]["grades"]),
            reverse=True
        )

        for row in self.tree.get_children():
            self.tree.delete(row)

        for sid, info in sorted_data:
            avg = calculate_average(info["grades"])
            self.tree.insert("", "end", values=(sid, info["name"], f"{avg:.1f}"))


    def search_student(self):
        # search in dictionary (GeeksforGeeks, 2024)
        query = self.search_entry.get()

        if query in self.db:
            student = self.db[query]
            messagebox.showinfo("Found", f"{student['name']}")
        else:
            messagebox.showwarning("Not Found", "Student not found")


    def refresh_table(self):
        #clear table (Stack Overflow Community, 2023)
        for row in self.tree.get_children():
            self.tree.delete(row)

        #insert data
        for sid, info in self.db.items():
            avg = calculate_average(info["grades"])
            self.tree.insert("", "end", values=(sid, info["name"], f"{avg:.1f}"))


    def add_student(self):
        #get values from user (freeCodeCamp, 2022)
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

        save_data(self.db)

        self.refresh_table()  # update table

        messagebox.showinfo("Success", "Student added")


#run program 
if __name__ == "__main__":
    app = App()
    app.mainloop()