from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox

class AssetManager:
    def __init__(self, assets_path):
        self.assets_path = assets_path

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

class ButtonHandlers:
    def __init__(self, window, entry_1):
        self.window = window
        self.entry_1 = entry_1

    def show_message(self, button_name):
        messagebox.showinfo("Button Clicked", f"{button_name} button clicked")

    def check_home(self):
        self.entry_1.delete(0, 'end')
        messagebox.showinfo("Home", "Home - Inputs Cleared")

    def check_students(self):
        self.show_message("Students")

    def check_book(self):
        messagebox.showinfo("Book", "Coming soon")

    def check_signout(self):
        result = messagebox.askquestion("Sign Out", "Are you sure you want to sign out?")
        if result == "yes":
            self.window.destroy()

    def check_searchbar(self):
        self.show_message("Search Bar")

    def check_calendar(self):
        self.show_message("Calendar")

    def check_notification(self):
        self.show_message("Notification")

    def check_student(self):
        self.show_message("Student")

    def check_section(self):
        self.show_message("Section")

    def check_gradelevel(self):
        self.show_message("Grade Level")

class CanvasManager:
    def __init__(self, canvas):
        self.canvas = canvas

    def draw_static_elements(self, asset_manager):
        image_image_1 = PhotoImage(file=asset_manager.relative_to_assets("image_1.png"))
        self.canvas.create_image(563.0, 275.0, image=image_image_1)

        image_image_2 = PhotoImage(file=asset_manager.relative_to_assets("image_2.png"))
        self.canvas.create_image(45.0, 38.0, image=image_image_2)

        image_image_3 = PhotoImage(file=asset_manager.relative_to_assets("image_3.png"))
        self.canvas.create_image(443.0, 107.0, image=image_image_3)

        image_image_4 = PhotoImage(file=asset_manager.relative_to_assets("image_4.png"))
        self.canvas.create_image(648.0, 92.0, image=image_image_4)

        image_image_5 = PhotoImage(file=asset_manager.relative_to_assets("image_5.png"))
        self.canvas.create_image(446.0, 274.0, image=image_image_5)

        # Add remaining images similarly
        # Prevent images from being garbage collected
        return [image_image_1, image_image_2, image_image_3, image_image_4, image_image_5]

    def draw_dynamic_elements(self):
        self.canvas.create_text(175.0, 415.0, anchor="nw", text="Miguel Mamerto O. Dinglasa", fill="#000000", font=("InriaSerif Bold", 15 * -1))
        self.canvas.create_text(484.0, 415.0, anchor="nw", text="10-Generosity", fill="#000000", font=("InriaSerif Bold", 15 * -1))
        self.canvas.create_text(647.0, 419.0, anchor="nw", text="Total:", fill="#000000", font=("InriaSerif Bold", 12 * -1))
        self.canvas.create_text(684.0, 417.0, anchor="nw", text="60", fill="#000000", font=("InriaSerif Bold", 16 * -1))
        self.canvas.create_text(454.0, 484.0, anchor="nw", text="Study", fill="#000000", font=("InriaSerif Bold", 12 * -1))
        self.canvas.create_text(490.0, 482.0, anchor="nw", text="40", fill="#000000", font=("InriaSerif Bold", 16 * -1))
        self.canvas.create_text(540.0, 485.0, anchor="nw", text="Research", fill="#000000", font=("InriaSerif Bold", 12 * -1))
        self.canvas.create_text(595.0, 483.0, anchor="nw", text="79", fill="#000000", font=("InriaSerif Bold", 16 * -1))
        self.canvas.create_text(647.0, 485.0, anchor="nw", text="Total", fill="#000000", font=("InriaSerif Bold", 12 * -1))
        self.canvas.create_text(684.0, 482.0, anchor="nw", text="119", fill="#000000", font=("InriaSerif Bold", 16 * -1))
        self.canvas.create_text(175.0, 479.0, anchor="nw", text="Generosity", fill="#000000", font=("InriaSerif Bold", 15 * -1))

class LibraryAttendanceApp:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1000x550")
        self.window.title("Library Attendance")
        self.window.configure(bg="#001EBF")

        output_path = Path(__file__).parent
        assets_path = output_path / Path(r"C:\Users\softw\Documents\UIV5.3\build\assets\frame0")
        asset_manager = AssetManager(assets_path)

        self.center_window(self.window, 1000, 549)

        self.canvas = Canvas(self.window, bg="#001EBF", height=550, width=1000, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        self.entry_1 = Entry(self.window, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=236.0, y=9.0, width=145.0, height=22.0)

        self.button_handlers = ButtonHandlers(self.window, self.entry_1)
        self.canvas_manager = CanvasManager(self.canvas)
        self.images = self.canvas_manager.draw_static_elements(asset_manager)

        self.setup_buttons(asset_manager)

        self.canvas_manager.draw_dynamic_elements()

        self.window.resizable(False, False)
        self.window.mainloop()

    def center_window(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x_coordinate = (screen_width - width) // 2
        y_coordinate = (screen_height - height) // 2
        window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

    def setup_buttons(self, asset_manager):
        button_image_1 = PhotoImage(file=asset_manager.relative_to_assets("button_1.png"))
        button_1 = Button(self.window, image=button_image_1, borderwidth=0, highlightthickness=0, command=self.button_handlers.check_home, relief="flat")
        button_1.place(x=28.0, y=103.0, width=42.0, height=33.0)

        button_image_2 = PhotoImage(file=asset_manager.relative_to_assets("button_2.png"))
        button_2 = Button(self.window, image=button_image_2, borderwidth=0, highlightthickness=0, command=self.button_handlers.check_students, relief="flat")
        button_2.place(x=29.0, y=151.0, width=42.0, height=35.0)

        button_image_3 = PhotoImage(file=asset_manager.relative_to_assets("button_3.png"))
        button_3 = Button(self.window, image=button_image_3, borderwidth=0, highlightthickness=0, command=self.button_handlers.check_book, relief="flat")
        button_3.place(x=29.0, y=210.0, width=41.0, height=41.0)

        button_image_4 = PhotoImage(file=asset_manager.relative_to_assets("button_4.png"))
        button_4 = Button(self.window, image=button_image_4, borderwidth=0, highlightthickness=0, command=self.button_handlers.check_notification, relief="flat")
        button_4.place(x=956.0, y=7.0, width=35.0, height=32.0)

        button_image_5 = PhotoImage(file=asset_manager.relative_to_assets("button_5.png"))
        button_5 = Button(self.window, image=button_image_5, borderwidth=0, highlightthickness=0, command=self.button_handlers.check_signout, relief="flat")
        button_5.place(x=26.0, y=492.0, width=44.0, height=46.0)

        button_image_6 = PhotoImage(file=asset_manager.relative_to_assets("button_6.png"))
        button_6 = Button(self.window, image=button_image_6, borderwidth=0, highlightthickness=0, command=self.button_handlers.check_student, relief="flat")
        button_6.place(x=850.0, y=228.0, width=63.0, height=22.0)

        button_image_7 = PhotoImage(file=asset_manager.relative_to_assets("button_7.png"))
        button_7 = Button(self.window, image=button_image_7, borderwidth=0, highlightthickness=0, command=self.button_handlers.check_section, relief="flat")
        button_7.place(x=850.0, y=284.0, width=63.0, height=22.0)

        button_image_8 = PhotoImage(file=asset_manager.relative_to_assets("button_8.png"))
        button_8 = Button(self.window, image=button_image_8, borderwidth=0, highlightthickness=0, command=self.button_handlers.check_gradelevel, relief="flat")
        button_8.place(x=850.0, y=342.0, width=78.0, height=22.0)

        button_image_9 = PhotoImage(file=asset_manager.relative_to_assets("button_9.png"))
        button_9 = Button(self.window, image=button_image_9, borderwidth=0, highlightthickness=0, command=self.button_handlers.check_calendar, relief="flat")
        button_9.place(x=787.0, y=6.0, width=35.0, height=34.0)

        # image_image_10 = PhotoImage(file=asset_manager.relative_to_assets("image_10.png"))
        # image_10 = canvas.create_image(444.0, 425.0, image=image_image_10, )

        # Prevent images from being garbage collected
        self.window.button_image_1 = button_image_1
        self.window.button_image_2 = button_image_2
        self.window.button_image_3 = button_image_3
        self.window.button_image_4 = button_image_4
        self.window.button_image_5 = button_image_5
        self.window.button_image_6 = button_image_6
        self.window.button_image_7 = button_image_7
        self.window.button_image_8 = button_image_8
        self.window.button_image_9 = button_image_9

if __name__ == "__main__":
    app = LibraryAttendanceApp()
