# Practical-Programming
3rd Assessment Python Project
APP NAME: Student Progress Tracker

GitHub Repository URL:
The source code for this project is available on GitHub: https://github.com/katia-ch07/Practical-Programming.git

Identification:
- Name: Katia Chalal
- P-number: P472435
- Course code: IY499

Declaration of Own Work:
I confirm that this assignment is my own work.
Where I have referred to online sources, I have provided comments detailing the reference and
included a link to the source.

Introduction:
This project implements a Student Progress Tracker using the Tkinter library. It allows users
to add students with grades, view and search student records, sort students by performance,
and visualise grade data through bar charts.
The main functionality of the app includes:
- Add students with a name and grade, saved to a persistent JSON file
- Search for a student by their ID and view their details
- Sort all students by their average grade in descending order
- Display a bar chart comparing student averages using Matplotlib

Installation:
To run the app locally:
1. Make sure Python 3.x is installed.
2. Install required dependencies:
   pip install -r requirements.txt
   or manually install the external library used:
   pip install matplotlib

How to Run the App:
1. Open terminal/command prompt in the project folder.
2. Run the main script:
   python MainFile.py
3. Controls:
   - Type a student name and grade into the input fields, then click "Add Student"
   - Type a student ID (e.g. S1, S2) into the Search field and click "Search"
   - Click "Sort by Average" to reorder the table by grade average
   - Click "Show Chart" to open a bar chart of all student averages

App Elements:
- Name & Grade Input Fields: Enter a new student's name and a numeric grade (0-100)
- Add Student Button: Validates input and saves the new student to the database
- Search Bar: Looks up a student by their auto-generated ID and displays their name
- Sort by Average Button: Re-renders the table sorted from highest to lowest average
- Show Chart Button: Generates and displays a Matplotlib bar chart inside the window
- Student Table: Displays all stored students with their ID, name, and average grade

Libraries Used:
- tkinter – for the graphical user interface and window management
- tkinter.ttk – for the Treeview table widget
- tkinter.messagebox – for pop-up dialogs (errors, success, search results)
- json – for saving and loading student data to/from a file
- os – for checking whether the data file exists before loading
- matplotlib – for generating bar charts of student grade averages

Project Structure:
StudentProgressTracker/
MainFile.py          # Entry point and main application code
students.json        # Auto-generated file storing student data
requirements.txt     # List of external dependencies
README.txt           # Project documentation

Testing:
Valid cases:
- Entering a name and a numeric grade between 0 and 100 successfully adds the student
- The table updates immediately after a student is added
- Searching an existing ID (e.g. S1) displays the correct student name

Invalid cases:
- Leaving the name field empty shows an error: "Name cannot be empty"
- Entering a non-numeric grade (e.g. "abc") shows an error: "Grade must be a number"
- Searching for an ID that does not exist shows a warning: "Student not found"

Edge/boundary cases:
- Entering a grade of exactly 0 or exactly 100 is accepted as valid
- Entering a grade of -1 or 101 is rejected with an appropriate error message
- Clicking "Show Chart" or "Sort by Average" with no students entered does not crash the program

References:
- Bala Priya C (2026). How to Use the Command Pattern in Python. [online] freeCodeCamp.org. Available at: https://www.freecodecamp.org/news/how-to-use-the-command-pattern-in-python/ [Accessed 10 Apr. 2026].
- Code, B. (2021). Python Full Course 🐍【𝙁𝙧𝙚𝙚】. YouTube. Available at: https://www.youtube.com/watch?v=XKHEtdqhLK8.
- freeCodeCamp.org (2019). Tkinter Course - Create Graphic User Interfaces in Python Tutorial. YouTube. Available at: https://www.youtube.com/watch?v=YXPyB4XeYLA.
- Geeksforgeeks.org. (2026). GeeksforGeeks | 404. [online] Available at: https://www.geeksforgeeks.org/python-program-to-find-average-of-a-list/ [Accessed 10 Apr. 2026].
- katze (2014). How to clear an entire Treeview with Tkinter. [online] Stack Overflow. Available at: https://stackoverflow.com/questions/22812134/how-to-clear-tkinter-treeview-widget.
- Matplotlib (2024). Matplotlib: Python plotting — Matplotlib 3.3.4 documentation. [online] matplotlib.org. Available at: https://matplotlib.org/stable/index.html.
- Python, R. (n.d.). Working With Files in Python – Real Python. [online] realpython.com. Available at: https://realpython.com/working-with-files-in-python/.
- Python Software Foundation (2019). tkinter — Python interface to Tcl/Tk — Python 3.7.2 documentation. [online] python.org. Available at: https://docs.python.org/3/library/tkinter.html.
- Python Software Foundation (2023). json — JSON encoder and decoder — Python 3.8.3rc1 documentation. [online] docs.python.org. Available at: https://docs.python.org/3/library/json.html.
- W3Schools (2019). Python Tutorial. [online] W3schools.com. Available at: https://www.w3schools.com/python/.
- www.programiz.com. (n.d.). Python File I/O: Read and Write Files in Python. [online] Available at: https://www.programiz.com/python-programming/file-operation.
