from tkinter import Tk, Label, Entry, Button, StringVar

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

# Create the Tkinter window
window = Tk()
window.title("Centered Window")

# Set window dimensions
width = 300
height = 150

# Center the window on the screen
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
login_button = Button(window, text="Login")
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the Tkinter main loop
window.mainloop()
