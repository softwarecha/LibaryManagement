import tkinter as tk
from tkinter import messagebox

class LoginForm:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Form")

        # Create widgets
        self.label_username = tk.Label(master, text="Username:")
        self.entry_username = tk.Entry(master)

        self.label_password = tk.Label(master, text="Password:")
        self.entry_password = tk.Entry(master, show="*")

        self.button_login = tk.Button(master, text="Login", command=self.login)

        # Place widgets using grid
        self.label_username.grid(row=0, column=0, sticky=tk.E)
        self.entry_username.grid(row=0, column=1)

        self.label_password.grid(row=1, column=0, sticky=tk.E)
        self.entry_password.grid(row=1, column=1)

        self.button_login.grid(row=2, column=1, pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Check if the username and password are correct
        if username == "Admin" and password == "1234":
            self.open_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def open_dashboard(self):
        self.master.destroy()  # Close the login form
        DashboardForm()

class DashboardForm:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Dashboard")

        # Create widgets for the dashboard
        label_dashboard = tk.Label(self.root, text="Welcome to the Dashboard!")
        label_dashboard.pack(pady=20)

        button_exit = tk.Button(self.root, text="Exit", command=self.exit_dashboard)
        button_exit.pack(pady=10)

        self.root.mainloop()

    def exit_dashboard(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    login_form = LoginForm(root)
    root.mainloop()
