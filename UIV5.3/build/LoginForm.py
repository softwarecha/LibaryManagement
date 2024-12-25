from tkinter import Tk, Toplevel, Label, Entry, Button, StringVar, ttk, messagebox
import subprocess
import threading
import time

def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    correct_username = "admin"
    correct_password = "1234"

    if entered_username == correct_username and entered_password == correct_password: 
        start_loading_animation()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

def open_python_script(file_path):
    try:
        subprocess.Popen(['python', file_path], shell=True)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open Python script: {e}")

def simulate_loading(top):
    for _ in range(5):  # Simulate loading by sleeping for 1 second (5 times)
        time.sleep(1)
        top.update_idletasks()

    top.destroy()
    open_python_script("C:\\Users\\softw\\Documents\\UIV5.3\\build\\gui.py")

def start_loading_animation():
    loading_top = Toplevel(window)
    loading_top.title("Loading")
    loading_top.iconbitmap('C:\\Users\\softw\\Documents\\UIV5.3\\build\\assets\\frame0\\SMAP.ico')
    loading_top.geometry("200x100")

    loading_label = Label(loading_top, text="Loading...")
    loading_label.pack(pady=20)

    loading_progress = ttk.Progressbar(loading_top, mode="indeterminate")
    loading_progress.pack()

    loading_thread = threading.Thread(target=lambda: simulate_loading(loading_top))
    loading_thread.start()

    # Center the loading window on the screen
    loading_top.update_idletasks()
    width = loading_top.winfo_width()
    height = loading_top.winfo_height()
    x = (loading_top.winfo_screenwidth() - width) // 2
    y = (loading_top.winfo_screenheight() - height) // 2
    loading_top.geometry(f"{width}x{height}+{x}+{y}")
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

# Create the Tkinter window


# Set window dimensions
width = 300
height = 150

# Center the window on the screen
# Create the Tkinter window
window = Tk()
window.title("Login Form")
window.iconbitmap('C:\\Users\\softw\\Documents\\UIV5.3\\build\\assets\\frame0\\SMAP.ico')
window.geometry("300x150")
center_window(window, width, height)

# Username Entry
Label(window, text="Username:").grid(row=0, column=0, pady=10)
username_var = StringVar()
username_entry = Entry(window, textvariable=username_var)
username_entry.grid(row=0, column=1)

# Password Entry
Label(window, text="Password:").grid(row=1, column=0, pady=10)
password_var = StringVar()
password_entry = Entry(window, textvariable=password_var, show="*")
password_entry.grid(row=1, column=1)

# Login Button
login_button = Button(window, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the Tkinter main loop
window.mainloop()
