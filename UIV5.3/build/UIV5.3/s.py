from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

class LibraryApp:
    def __init__(self):
        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / Path(r"C:\Users\migue\OneDrive\Desktop\Applications\UI\library\UIV5.3\build\assets\frame0")

        self.window = Tk()
        self.window.geometry("1000x550")
        self.window.configure(bg="#001EBF")

        self.canvas = Canvas(
            self.window,
            bg="#001EBF",
            height=550,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        # Images
        self.image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))
        self.image_5 = PhotoImage(file=self.relative_to_assets("image_5.png"))
        self.image_6 = PhotoImage(file=self.relative_to_assets("image_6.png"))
        self.image_7 = PhotoImage(file=self.relative_to_assets("image_7.png"))
        self.image_8 = PhotoImage(file=self.relative_to_assets("image_8.png"))
        self.image_9 = PhotoImage(file=self.relative_to_assets("image_9.png"))
        self.image_10 = PhotoImage(file=self.relative_to_assets("image_10.png"))
        self.image_11 = PhotoImage(file=self.relative_to_assets("image_11.png"))
        self.image_12 = PhotoImage(file=self.relative_to_assets("image_12.png"))
        self.image_13 = PhotoImage(file=self.relative_to_assets("image_13.png"))
        self.image_14 = PhotoImage(file=self.relative_to_assets("image_14.png"))
        self.image_15 = PhotoImage(file=self.relative_to_assets("image_15.png"))
        self.image_16 = PhotoImage(file=self.relative_to_assets("image_16.png"))

        # Buttons
        self.button_1 = self.create_button("button_1.png", self.check_home)
        self.button_2 = self.create_button("button_2.png", self.check_students)
        self.button_3 = self.create_button("button_3.png", self.check_book)
        self.button_4 = self.create_button("button_4.png", self.check_button_4)
        self.button_5 = self.create_button("button_5.png", self.check_button_5)
        # ... Repeat for other buttons ...

        # Entry and its background
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_bg_1 = self.canvas.create_image(
            308.5,
            21.0,
            image=PhotoImage(file=self.relative_to_assets("entry_1.png"))
        )

        # Other images and buttons...

        # GUI main loop
        self.window.resizable(False, False)
        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

    def create_button(self, image_path: str, command_func):
        button = Button(
            image=PhotoImage(file=self.relative_to_assets(image_path)),
            borderwidth=0,
            highlightthickness=0,
            command=command_func,
            relief="flat"
        )
        return button

    # Button functions
    def check_home(self):
        pass

    def check_students(self):
        pass

    def check_book(self):
        pass

    def check_button_4(self):
        pass

    def check_button_5(self):
        pass

    # ... Repeat for other button functions ...

if __name__ == "__main__":
    app = LibraryApp()
