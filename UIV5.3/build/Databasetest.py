import tkinter as tk
from tkinter import ttk

class StudentDatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Database")

        # Create a list of students (you can replace this with your actual data)
        self.students = [
            "John Doe",
            "Jane Smith",
            "Bob Johnson",
            "Alice Williams",
            "Charlie Brown",
            "Eva Davis",
            "Frank Miller",
            "Grace Wilson",
            "Harry Taylor",
            "Ivy Turner",
            "Jack Harris",
            "Kelly Moore",
            "Leo Young",
            "Mia Lee",
            "Noah Wright"
        ]

        # Create a Listbox to display the students
        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
        self.listbox.pack(padx=10, pady=10)

        # Populate the Listbox with student names
        for student in self.students:
            self.listbox.insert(tk.END, student)

        # Create a vertical scrollbar
        scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Create a button to perform an action (you can replace this with your specific functionality)
        action_button = tk.Button(root, text="Perform Action", command=self.perform_action)
        action_button.pack(pady=10)

    def perform_action(self):
        # Get the selected student from the Listbox
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_student = self.students[selected_index[0]]
            print(f"Performing action for student: {selected_student}")
        else:
            print("Please select a student.")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentDatabaseApp(root)
    root.mainloop()
