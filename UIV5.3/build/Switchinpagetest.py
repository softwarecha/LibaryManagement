import tkinter as tk

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Application")

        # Create frames for different pages
        self.home_frame = tk.Frame(self.root)
        self.database_frame = tk.Frame(self.root)

        # Set up the Home page
        self.setup_home_page()

        # Set up the Database page
        self.setup_database_page()

        # Start with the Home page
        self.show_home_page()

    def setup_home_page(self):
        # Home Page Label, Entry, Button, Text Entry, and OptionMenu
        home_label = tk.Label(self.home_frame, text="Home Page", font=("Helvetica", 16))
        home_label.pack(pady=10)

        # Entry widget for the text
        self.text_entry = tk.Entry(self.home_frame, width=20)
        self.text_entry.pack(pady=10)

        # OptionMenu to choose the placement
        options = ["Center", "Left", "Right"]
        self.placement_var = tk.StringVar(self.home_frame)
        self.placement_var.set(options[0])  # default placement is Center
        placement_menu = tk.OptionMenu(self.home_frame, self.placement_var, *options)
        placement_menu.pack(pady=10)

        home_button = tk.Button(self.home_frame, text="Database Page", command=self.show_database_page)
        home_button.pack(pady=10)

        # Label to display the entered text
        self.display_label = tk.Label(self.home_frame, text="")
        self.display_label.pack(pady=10)

    def setup_database_page(self):
        # Database Page Label, Entry, Button, Text Entry, and OptionMenu
        database_label = tk.Label(self.database_frame, text="Database Page", font=("Helvetica", 16))
        database_label.pack(pady=10)

        # Entry widget for the text
        self.text_entry = tk.Entry(self.database_frame, width=20)
        self.text_entry.pack(pady=10)

        # OptionMenu to choose the placement
        options = ["Center", "Left", "Right"]
        self.placement_var = tk.StringVar(self.database_frame)
        self.placement_var.set(options[0])  # default placement is Center
        placement_menu = tk.OptionMenu(self.database_frame, self.placement_var, *options)
        placement_menu.pack(pady=10)

        database_button = tk.Button(self.database_frame, text="Home Page", command=self.show_home_page)
        database_button.pack(pady=10)

        # Label to display the entered text
        self.display_label = tk.Label(self.database_frame, text="")
        self.display_label.pack(pady=10)

    def show_home_page(self):
        # Show the Home page and hide the Database page
        self.database_frame.pack_forget()
        self.home_frame.pack()

    def show_database_page(self):
        # Show the Database page and hide the Home page
        self.home_frame.pack_forget()
        self.database_frame.pack()

    def display_text(self):
        # Get the entered text and placement
        entered_text = self.text_entry.get()
        placement = self.placement_var.get()

        # Display the entered text at the chosen position
        if placement == "Center":
            self.display_label.config(text=entered_text, justify="center")
        elif placement == "Left":
            self.display_label.config(text=entered_text, justify="left")
        elif placement == "Right":
            self.display_label.config(text=entered_text, justify="right")


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
