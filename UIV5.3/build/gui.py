



from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\softw\Documents\UIV5.3\build\assets\frame0")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Function to show a message box for button clicks
def show_message(button_name):
    messagebox.showinfo("Button Clicked", f"{button_name} button clicked")

# Button functions

def check_home():
    entry_1.delete(0, 'end')
    messagebox.showinfo("Home", "Home - Inputs Cleared")

def check_students():
    show_message("Students")

def check_book():
    # show_message("Book")
    messagebox.showinfo("Book", "Coming soon")

def check_signout():
    result = messagebox.askquestion("Sign Out", "Are you sure you want to sign out?")

    if result == "yes":

        window.destroy()

def check_searchbar():
    show_message("Search Bar")

def check_calendar():
    show_message("Calendar")

def check_notification():
    show_message("Notification")

def check_student():
    show_message("Student")

def check_section():
    show_message("Section")

def check_gradelevel():
    show_message("Grade Level")

# Updater functions (Note: I've removed duplicated functions)
def updater_function_1():
    pass

def updater_function_2():
    pass

def Leading_student(student_name):
    canvas.create_text(175.0,415.0,anchor="nw",text=student_name,fill="#000000",font=("InriaSerif Bold", 15 * -1))
def Section_name(section):
    canvas.create_text(484.0,415.0,anchor="nw",text=section,fill="#000000", font=("InriaSerif Bold", 15 * -1) )
def Total(Text_total):
    canvas.create_text(  647.0,419.0, anchor="nw",text=Text_total,fill="#000000", font=("InriaSerif Bold", 12 * -1))
def Total_Study(Num_Study):
    canvas.create_text(684.0,417.0,anchor="nw",text=Num_Study, fill="#000000",font=("InriaSerif Bold", 16 * -1))
def study(study_label):
    canvas.create_text(  454.0,   484.0, anchor="nw",  text=study_label,fill="#000000", font=("InriaSerif Bold", 12 * -1))
def study_total(total_study):
    canvas.create_text(  490.0,  482.0, anchor="nw", text=total_study, fill="#000000", font=("InriaSerif Bold", 16 * -1))
def research(researh_label):
    canvas.create_text( 540.0, 485.0, anchor="nw",    text=researh_label,  fill="#000000", font=("InriaSerif Bold", 12 * -1))

def research_total(total_research):
    canvas.create_text(  595.0,  483.0,  anchor="nw", text=total_research,  fill="#000000", font=("InriaSerif Bold", 16 * -1) )
def rsch_stdy_label(rs_label):
    canvas.create_text( 647.0, 485.0, anchor="nw",text=rs_label,fill="#000000",  font=("InriaSerif Bold", 12 * -1))


def rsch_stdy_total(sum_total):
    canvas.create_text( 684.0,482.0, anchor="nw",  text=sum_total,fill="#000000", font=("InriaSerif Bold", 16 * -1) )


def Leading_Section(section_name):
    canvas.create_text(  175.0, 479.0,  anchor="nw",text=section_name, fill="#000000", font=("InriaSerif Bold", 15 * -1))



def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

# Create the Tkinter window


# Set window dimensions
width = 1000
height = 549



window = Tk()

window.geometry("1000x550")
window.title("Library Attendance")
window.iconbitmap("C:\\Users\\softw\\Documents\\UIV5.3\\build\\assets\\frame0\\SMAP.ico")
window.configure(bg = "#001EBF")
center_window(window, width, height)


canvas = Canvas(  window,  bg = "#001EBF",  height = 550, width = 1000, bd = 0,  highlightthickness = 0,  relief = "ridge")

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(  file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(  563.0,  275.0,  image=image_image_1)

image_image_2 = PhotoImage( file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(  45.0,  38.0,  image=image_image_2)
canvas.create_text( 30.0,  73.0,  anchor="nw",  text="SMAP",  fill="#FFFFFF", font=("InriaSerif Bold", 12 * -1))

button_image_1 = PhotoImage( file=relative_to_assets("button_1.png"))
button_1 = Button(window,  image=button_image_1,  borderwidth=0,  highlightthickness=0, command= check_home,  relief="flat")
button_1.place( x=28.0,  y=103.0, width=42.0, height=33.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=check_students,relief="flat")
button_2.place(x=29.0,y=151.0,width=42.0,height=35.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=check_book,relief="flat")
button_3.place(x=29.0,y=210.0,width=41.0,height=41.0)

canvas.create_rectangle(951.0,0.0,1000.0, 43.0,fill="#D9D9D9", outline="")

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(image=button_image_4,borderwidth=0,highlightthickness=0,command=check_notification,relief="flat")
button_4.place(x=956.0,y=7.0,width=35.0,height=32.0)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(image=button_image_5,borderwidth=0,highlightthickness=0,command=check_signout,relief="flat")
button_5.place(x=26.0,y=492.0,width=44.0,height=46.0)

canvas.create_text(93.0,16.0,anchor="nw",text="Main Dashboard",fill="#001EBF",font=("InriaSans Bold", 14 * -1))

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(308.5,21.0,image=entry_image_1)
entry_1 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
entry_1.place(x=236.0,y=9.0,width=145.0,height=22.0)



image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(443.0,107.0,image=image_image_3)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(648.0,92.0,image=image_image_4)

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(446.0,274.0,image=image_image_5)

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(892.0,125.0,image=image_image_6)

image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(892.0,247.0,image=image_image_7)

image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(892.0,305.0,image=image_image_8)

image_image_9 = PhotoImage(file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(892.0,363.0,image=image_image_9)

image_image_10 = PhotoImage(file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(444.0,425.0,image=image_image_10,)

image_Student = PhotoImage(file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(140.0,420.0,image=image_Student)

Leading_student("Miguel Mamerto O. Dinglasa")
Section_name("10-Generosity")
Total("Total:")
Total_Study("60")


image_image_11 = PhotoImage(file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(444.0,491.0,image=image_image_11)

image_Section = PhotoImage(file=relative_to_assets("image_17.png"))
image_16 = canvas.create_image(140.0,488.0,image=image_Section)

Leading_Section("Generosity")
study("Study")
study_total("40")
research("Research")
research_total("79")
rsch_stdy_label("Total")
rsch_stdy_total("119")

image_image_12 = PhotoImage(file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(210.0,24.0,image=image_image_12)

canvas.create_text(143.0,83.0,anchor="nw",text="Good Morning Teacher",fill="#FFFFFF",font=("InriaSans Bold", 11 * -1))

canvas.create_text(139.0,109.0,anchor="nw",text="Check Library Daily Attendace",fill="#FFFFFF",font=("InriaSerif Bold", 18 * -1))

canvas.create_text(823.0,17.0,anchor="nw",text="November,18,2023",fill="#000000",font=("InriaSerif Bold", 11 * -1))

button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
button_6 = Button(image=button_image_6,borderwidth=0,highlightthickness=0,command=check_student,relief="flat")
button_6.place(x=850.0,y=228.0,width=63.0,height=22.0)

button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
button_7 = Button(image=button_image_7,borderwidth=0,highlightthickness=0,command=check_section,relief="flat")
button_7.place(x=850.0,y=284.0,width=63.0,height=22.0)

button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
button_8 = Button(image=button_image_8,borderwidth=0,highlightthickness=0,command=check_gradelevel,relief="flat")
button_8.place(x=850.0,y=342.0,width=78.0,height=22.0)

canvas.create_text(858.0,247.0,anchor="nw",text="0",fill="#000000",font=("InriaSerif Bold", 16 * -1))

canvas.create_text(858.0,305.0,anchor="nw",text="0",fill="#000000",font=("InriaSerif Bold", 16 * -1))

canvas.create_text(858.0,363.0,anchor="nw",text="12",fill="#000000",font=("InriaSerif Bold", 16 * -1))

button_image_9 = PhotoImage(file=relative_to_assets("button_9.png"))
button_9 = Button(image=button_image_9,borderwidth=0,highlightthickness=0,command=check_calendar,relief="flat")
button_9.place(x=787.0,y=6.0,width=35.0, height=34.0)
button_1.place(x=28.0, y=103.0, width=42.0, height=33.0)

image_image_13 = PhotoImage(file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(824.0,246.0,image=image_image_13)

image_image_14 = PhotoImage(file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(824.0,307.0,image=image_image_14)

image_image_15 = PhotoImage(file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(824.0,366.0,image=image_image_15)

canvas.create_text(135.0,173.0,anchor="nw",text="Status", fill="#000000",font=("InriaSerif Bold", 12 * -1))

image_image_16 = PhotoImage(file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(882.0,466.0,image=image_image_16)



window.resizable(False, False)
window.mainloop()
