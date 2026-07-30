# ==========================================================
# IMPORTS
# ==========================================================

# Used for saving and loading account data
import json

# Used for creating folders and checking files
import os

# Used for username/password validation
import re

# Used for loading the EduTrack logo
from PIL import Image, ImageTk

# Used for creating the graphical interface
import tkinter as tk
from tkinter import ttk, messagebox


# ==========================================================
# ACCOUNT STORAGE
# ==========================================================

# Creates the accounts folder if it does not exist
if not os.path.exists("accounts"):
    os.mkdir("accounts")


# ==========================================================
# MAIN WINDOW SETUP
# ==========================================================

window = tk.Tk()

window.title("EduTrack")

window.geometry("1100x700")

window.configure(
    bg="#F4F6FA"
)


# ==========================================================
# COLOURS
# ==========================================================

COLORS = {

    "primary": "#1F4E79",

    "secondary": "#2E75B6",

    "background": "#F4F6FA",

    "white": "#FFFFFF",

    "dark": "#1E293B",

    "grey": "#64748B",

    "danger": "#DC2626",

    "warning": "#F59E0B",

    "success": "#16A34A"

}



# ==========================================================
# FONTS
# ==========================================================

FONT_TITLE = (
    "Segoe UI",
    24,
    "bold"
)


FONT_HEADER = (
    "Segoe UI",
    16,
    "bold"
)


FONT_NORMAL = (
    "Segoe UI",
    11
)



# ==========================================================
# LOGO LOADING
# ==========================================================

# Default value if logo cannot load
logo = None


try:

    logo_image = Image.open(
        "assets/logo.png"
    )

    logo_image = logo_image.resize(
        (80, 80)
    )

    logo = ImageTk.PhotoImage(
        logo_image
    )


except Exception:

    # Program continues without logo
    logo = None



# ==========================================================
# GLOBAL VARIABLES
# ==========================================================

# Stores all student records
students = []


# Stores logged-in username
current_user = ""


# Stores dashboard content area
content_frame = None



# ==========================================================
# AVAILABLE OPTIONS
# ==========================================================

CLASSES = [

    "English",

    "Maths",

    "Science",

    "Drama",

    "Humanities",

    "Digi-Tech",

    "Japanese",

    "Art",

    "Agriculture"

]


STATUSES = [

    "Missing",

    "Late",

    "Submitted"

]



# ==========================================================
# TKINTER STYLE
# ==========================================================

style = ttk.Style()

style.theme_use(
    "clam"
)


style.configure(

    "Treeview",

    background=COLORS["white"],

    foreground=COLORS["dark"],

    rowheight=35,

    fieldbackground=COLORS["white"],

    font=FONT_NORMAL

)


style.configure(

    "Treeview.Heading",

    font=(
        "Segoe UI",
        11,
        "bold"
    )

)



# ==========================================================
# WINDOW CLEARING
# ==========================================================

def clear_window():

    """
    Removes all widgets from the window.
    """

    for widget in window.winfo_children():

        widget.destroy()



# ==========================================================
# SAVE DATA
# ==========================================================

def save_data():

    """
    Saves current students into the
    logged-in user's JSON file.
    """

    if current_user == "":

        return


    filename = (
        f"accounts/{current_user}.json"
    )


    if not os.path.exists(filename):

        return


    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)


    data["students"] = students


    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )



# ==========================================================
# LOAD ACCOUNT
# ==========================================================

def load_account(filename):

    """
    Loads account data from JSON.
    """

    try:

        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except Exception:

        messagebox.showerror(
            "Error",
            "Unable to load account."
        )

        return None



# ==========================================================
# CREATE ACCOUNT
# ==========================================================

def create_account(username, password):

    """
    Creates a new teacher account.
    """


    if username == "" or password == "":

        messagebox.showwarning(
            "Missing Details",
            "Enter username and password."
        )

        return



    if len(username) > 16:

        messagebox.showwarning(
            "Invalid Username",
            "Username must be 16 characters or less."
        )

        return



    if not re.fullmatch(
        r"[A-Za-z0-9_]+",
        username
    ):

        messagebox.showwarning(
            "Invalid Username",
            "Only letters, numbers and underscores allowed."
        )

        return



    if len(password) < 12 or len(password) > 16:

        messagebox.showwarning(
            "Invalid Password",
            "Password must be 12-16 characters."
        )

        return



    if not re.search(
        r"[A-Z]",
        password
    ):

        messagebox.showwarning(
            "Invalid Password",
            "Password requires uppercase letter."
        )

        return



    if not re.search(
        r"[a-z]",
        password
    ):

        messagebox.showwarning(
            "Invalid Password",
            "Password requires lowercase letter."
        )

        return



    if not re.search(
        r"[0-9]",
        password
    ):

        messagebox.showwarning(
            "Invalid Password",
            "Password requires number."
        )

        return



    filename = (
        f"accounts/{username}.json"
    )


    if os.path.exists(filename):

        messagebox.showerror(
            "Account Exists",
            "Username already exists."
        )

        return



    data = {

        "password": password,

        "students": []

    }


    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


    messagebox.showinfo(
        "Success",
        "Profile created."
    )


    login_screen()
    
    # ==========================================================
# LOGIN SYSTEM
# ==========================================================

def login_user(username, password):

    """
    Checks login details and loads saved data.
    """

    global current_user


    if username == "" or password == "":

        messagebox.showwarning(
            "Missing Details",
            "Enter username and password."
        )

        return



    filename = (
        f"accounts/{username}.json"
    )


    if not os.path.exists(filename):

        messagebox.showerror(
            "Login Failed",
            "Account does not exist."
        )

        return



    data = load_account(filename)


    if data is None:

        return



    if data["password"] != password:

        messagebox.showerror(
            "Login Failed",
            "Incorrect password."
        )

        return



    current_user = username


    students.clear()


    students.extend(
        data["students"]
    )


    show_student_list()



# ==========================================================
# LOGIN SCREEN
# ==========================================================

def login_screen():

    """
    Creates the login interface.
    """

    clear_window()


    background = tk.Frame(

        window,

        bg=COLORS["background"]

    )


    background.pack(

        fill="both",

        expand=True

    )



    if logo:

        tk.Label(

            background,

            image=logo,

            bg=COLORS["background"]

        ).pack(

            pady=20

        )



    tk.Label(

        background,

        text="EduTrack",

        font=FONT_TITLE,

        fg=COLORS["primary"],

        bg=COLORS["background"]

    ).pack()



    card = tk.Frame(

        background,

        bg=COLORS["white"],

        padx=40,

        pady=40,

        relief="ridge",

        bd=1

    )


    card.pack(

        pady=30

    )



    tk.Label(

        card,

        text="Username",

        bg=COLORS["white"],

        font=FONT_NORMAL

    ).pack(anchor="w")



    username_entry = tk.Entry(

        card,

        width=35

    )


    username_entry.pack()



    tk.Label(

        card,

        text="Password",

        bg=COLORS["white"],

        font=FONT_NORMAL

    ).pack(anchor="w")



    password_entry = tk.Entry(

        card,

        width=35,

        show="*"

    )


    password_entry.pack()



    tk.Button(

        card,

        text="Sign In",

        width=25,

        bg=COLORS["primary"],

        fg="white",

        command=lambda:

        login_user(

            username_entry.get(),

            password_entry.get()

        )

    ).pack(

        pady=10

    )



    tk.Button(

        card,

        text="Create New Profile",

        width=25,

        command=lambda:

        create_account(

            username_entry.get(),

            password_entry.get()

        )

    ).pack()



# ==========================================================
# DASHBOARD
# ==========================================================

def create_dashboard():

    """
    Creates the main application layout.
    """

    global content_frame


    clear_window()



    sidebar = tk.Frame(

        window,

        bg=COLORS["primary"],

        width=220

    )


    sidebar.pack(

        side="left",

        fill="y"

    )



    if logo:

        tk.Label(

            sidebar,

            image=logo,

            bg=COLORS["primary"]

        ).pack(

            pady=15

        )



    tk.Label(

        sidebar,

        text="EduTrack",

        font=FONT_TITLE,

        fg="white",

        bg=COLORS["primary"]

    ).pack()



    buttons = [

        ("Students", show_student_list),

        ("Profile", show_profile),

        ("Reminders", show_reminders),

        ("Reports", show_report)

    ]



    for text, command in buttons:

        tk.Button(

            sidebar,

            text=text,

            width=18,

            height=2,

            bg=COLORS["secondary"],

            fg="white",

            command=command

        ).pack(

            pady=8

        )



    tk.Frame(

        sidebar,

        bg=COLORS["primary"]

    ).pack(

        expand=True

    )



    tk.Button(

        sidebar,

        text="Logout",

        bg=COLORS["danger"],

        fg="white",

        width=15,

        command=logout

    ).pack(

        pady=25

    )



    content_frame = tk.Frame(

        window,

        bg=COLORS["background"]

    )


    content_frame.pack(

        side="right",

        fill="both",

        expand=True

    )



# ==========================================================
# LOGOUT
# ==========================================================

def logout():

    """
    Saves data and returns to login.
    """

    global current_user


    save_data()


    students.clear()


    current_user = ""


    login_screen()



# ==========================================================
# STUDENT MANAGEMENT PAGE
# ==========================================================

def show_student_list():

    """
    Displays student records.
    """

    create_dashboard()



    title = tk.Label(

        content_frame,

        text="Student Management",

        font=FONT_TITLE,

        bg=COLORS["background"],

        fg=COLORS["primary"]

    )


    title.pack(

        pady=20

    )



    search_frame = tk.Frame(

        content_frame,

        bg=COLORS["background"]

    )


    search_frame.pack()



    search_entry = tk.Entry(

        search_frame,

        width=40

    )


    search_entry.pack(

        side="left"

    )



    columns = (

        "Name",

        "Student ID",

        "Class",

        "Status",

        "Record"

    )


    table = ttk.Treeview(

        content_frame,

        columns=columns,

        show="headings"

    )



    for column in columns:

        table.heading(

            column,

            text=column

        )

        table.column(

            column,

            width=140

        )



    table.column(

        "Record",

        width=0,

        stretch=False

    )


    table.pack(

        fill="both",

        expand=True,

        padx=20,

        pady=20

    )



    def refresh(data):

        for item in table.get_children():

            table.delete(item)


        for student in data:

            table.insert(

                "",

                "end",

                values=(

                    student["Name"],

                    student["ID"],

                    student["Class"],

                    student["Status"],

                    student["RecordID"]

                )

            )


    refresh(students)

    def search():

        text = search_entry.get().lower()


        results = []


        for student in students:

            if (

                text in student["Name"].lower()

                or text in student["ID"]

            ):

                results.append(student)


        refresh(results)



    tk.Button(

        search_frame,

        text="Search",

        command=search

    ).pack(

        side="left"

    )
    
    tk.Button(

        search_frame,

        text="Filter",

        command=lambda: filter_students(refresh)

    ).pack(

        side="left",

        padx=5

    )



    button_frame = tk.Frame(

        content_frame

    )


    button_frame.pack()



    tk.Button(

        button_frame,

        text="Add Student",

        command=lambda:

        add_student_window(refresh)

    ).grid(

        row=0,

        column=0,

        padx=5

    )



    tk.Button(

        button_frame,

        text="Edit Student",

        command=lambda:

        edit_student_window(

            table,

            refresh

        )

    ).grid(

        row=0,

        column=1,

        padx=5

    )



    tk.Button(

        button_frame,

        text="Remove Student",

        command=lambda:

        remove_student(

            table,

            refresh

        )

    ).grid(

        row=0,

        column=2,

        padx=5

    )
# ==========================================================
# FILTER STUDENTS
# ==========================================================

def filter_students(refresh):

    """
    Opens a window allowing students to be
    filtered by class, status and ID.
    """

    popup = tk.Toplevel(window)

    popup.title(
        "Filter Students"
    )

    popup.geometry(
        "350x350"
    )


    # -----------------------------
    # CLASS FILTER
    # -----------------------------

    tk.Label(
        popup,
        text="Class"
    ).pack(
        pady=5
    )


    class_box = ttk.Combobox(

        popup,

        values=[
            "All Classes"
        ] + CLASSES,

        state="readonly"

    )


    class_box.set(
        "All Classes"
    )


    class_box.pack()



    # -----------------------------
    # STATUS FILTER
    # -----------------------------

    tk.Label(
        popup,
        text="Status"
    ).pack(
        pady=5
    )


    status_box = ttk.Combobox(

        popup,

        values=[
            "All Statuses"
        ] + STATUSES,

        state="readonly"

    )


    status_box.set(
        "All Statuses"
    )


    status_box.pack()



    # -----------------------------
    # STUDENT ID FILTER
    # -----------------------------

    tk.Label(
        popup,
        text="Student ID"
    ).pack(
        pady=5
    )


    id_entry = tk.Entry(
        popup
    )


    id_entry.pack()



    # -----------------------------
    # APPLY FILTER
    # -----------------------------

    def apply_filter():


        filtered_students = []


        selected_class = class_box.get()

        selected_status = status_box.get()

        selected_id = id_entry.get()



        for student in students:


            # Check class

            if selected_class != "All Classes":

                if student["Class"] != selected_class:

                    continue



            # Check status

            if selected_status != "All Statuses":

                if student["Status"] != selected_status:

                    continue



            # Check ID

            if selected_id != "":

                if selected_id not in student["ID"]:

                    continue



            filtered_students.append(
                student
            )



        refresh(
            filtered_students
        )


        popup.destroy()



    tk.Button(

        popup,

        text="Apply Filter",

        bg=COLORS["primary"],

        fg="white",

        command=apply_filter

    ).pack(

        pady=25

    )



    # -----------------------------
    # RESET FILTER
    # -----------------------------

    def reset_filter():

        refresh(
            students
        )

        popup.destroy()



    tk.Button(

        popup,

        text="Clear Filters",

        command=reset_filter

    ).pack()    
# ==========================================================
# ADD STUDENT WINDOW
# ==========================================================

def add_student_window(refresh):

    """
    Creates a new student record.
    """

    popup = tk.Toplevel(window)

    popup.title(
        "Add Student"
    )

    popup.geometry(
        "350x450"
    )


    entries = {}


    for field in ["Name", "ID"]:

        tk.Label(
            popup,
            text=field
        ).pack()


        entry = tk.Entry(
            popup
        )

        entry.pack()


        entries[field] = entry



    tk.Label(
        popup,
        text="Class"
    ).pack()


    class_box = ttk.Combobox(

        popup,

        values=CLASSES,

        state="readonly"

    )


    class_box.pack()



    tk.Label(
        popup,
        text="Status"
    ).pack()



    status_box = ttk.Combobox(

        popup,

        values=STATUSES,

        state="readonly"

    )


    status_box.pack()



    def save():


        student_id = entries["ID"].get()



        if not student_id.isdigit() or len(student_id) != 10:


            messagebox.showwarning(

                "Invalid ID",

                "Student ID must contain exactly 10 digits."

            )

            return



        for student in students:


            if student["ID"] == student_id:


                messagebox.showwarning(

                    "Duplicate ID",

                    "Student already exists."

                )

                return



        if class_box.get() == "" or status_box.get() == "":

            messagebox.showwarning(

                "Missing Details",

                "Select a class and status."

            )

            return



        students.append(

            {

                "RecordID": len(students) + 1,

                "Name": entries["Name"].get(),

                "ID": student_id,

                "Class": class_box.get(),

                "Status": status_box.get()

            }

        )



        save_data()

        refresh(students)

        popup.destroy()



    tk.Button(

        popup,

        text="Save",

        command=save

    ).pack(

        pady=20

    )





# ==========================================================
# REMOVE STUDENT
# ==========================================================

def remove_student(table, refresh):

    """
    Deletes selected student.
    """


    selected = table.focus()



    if not selected:

        messagebox.showwarning(

            "No Selection",

            "Select a student first."

        )

        return



    record_id = table.item(selected)["values"][4]



    for student in students:


        if student["RecordID"] == record_id:

            students.remove(student)

            break



    save_data()

    refresh(students)





# ==========================================================
# EDIT STUDENT WINDOW
# ==========================================================

def edit_student_window(table, refresh):

    """
    Edits an existing student.
    """


    selected = table.focus()



    if not selected:

        messagebox.showwarning(

            "No Selection",

            "Select a student first."

        )

        return



    record_id = table.item(selected)["values"][4]



    for student in students:


        if student["RecordID"] == record_id:


            popup = tk.Toplevel(window)


            popup.title(
                "Edit Student"
            )


            popup.geometry(
                "350x400"
            )



            tk.Label(
                popup,
                text="Name"
            ).pack()



            name_entry = tk.Entry(
                popup
            )


            name_entry.insert(

                0,

                student["Name"]

            )


            name_entry.pack()



            tk.Label(
                popup,
                text="Student ID"
            ).pack()



            id_entry = tk.Entry(
                popup
            )


            id_entry.insert(

                0,

                student["ID"]

            )


            id_entry.pack()



            tk.Label(
                popup,
                text="Class"
            ).pack()



            class_box = ttk.Combobox(

                popup,

                values=CLASSES,

                state="readonly"

            )


            class_box.set(

                student["Class"]

            )


            class_box.pack()



            tk.Label(
                popup,
                text="Status"
            ).pack()



            status_box = ttk.Combobox(

                popup,

                values=STATUSES,

                state="readonly"

            )


            status_box.set(

                student["Status"]

            )


            status_box.pack()



            def save_changes():


                new_id = id_entry.get()



                if not new_id.isdigit() or len(new_id) != 10:


                    messagebox.showwarning(

                        "Invalid ID",

                        "Student ID must contain exactly 10 digits."

                    )

                    return



                for other in students:


                    if (

                        other != student

                        and other["ID"] == new_id

                    ):


                        messagebox.showwarning(

                            "Duplicate ID",

                            "Student ID already exists."

                        )

                        return



                student["Name"] = name_entry.get()

                student["ID"] = new_id

                student["Class"] = class_box.get()

                student["Status"] = status_box.get()



                save_data()

                refresh(students)

                popup.destroy()



            tk.Button(

                popup,

                text="Save Changes",

                command=save_changes

            ).pack(

                pady=20

            )


            break





# ==========================================================
# PROFILE PAGE
# ==========================================================

def show_profile():

    """
    Displays teacher statistics.
    """


    create_dashboard()



    tk.Label(

        content_frame,

        text="User Profile",

        font=FONT_TITLE,

        bg=COLORS["background"],

        fg=COLORS["primary"]

    ).pack(

        pady=20

    )



    missing = 0

    late = 0

    submitted = 0



    for student in students:


        if student["Status"] == "Missing":

            missing += 1


        elif student["Status"] == "Late":

            late += 1


        else:

            submitted += 1



    information = [

        f"Username: {current_user}",

        f"Students Managed: {len(students)}",

        f"Missing Work: {missing}",

        f"Late Work: {late}",

        f"Submitted Work: {submitted}"

    ]



    for item in information:


        tk.Label(

            content_frame,

            text=item,

            font=FONT_HEADER,

            bg=COLORS["background"]

        ).pack(

            pady=8

        )





# ==========================================================
# REMINDERS PAGE
# ==========================================================

def show_reminders():

    """
    Displays missing work reminders.
    """


    create_dashboard()



    tk.Label(

        content_frame,

        text="Missing Work Reminders",

        font=FONT_TITLE,

        fg=COLORS["danger"],

        bg=COLORS["background"]

    ).pack(

        pady=20

    )



    missing_students = [

        student

        for student in students

        if student["Status"] == "Missing"

    ]



    tk.Label(

        content_frame,

        text=f"{len(missing_students)} student(s) require attention",

        font=FONT_HEADER,

        bg=COLORS["background"]

    ).pack()



    for student in missing_students:


        tk.Label(

            content_frame,

            text=(

                f"{student['Name']} - "

                f"{student['Class']}"

            ),

            font=FONT_NORMAL,

            bg=COLORS["background"]

        ).pack(

            pady=5

        )
        
        # ==========================================================
# REPORT DASHBOARD
# ==========================================================

def show_report():

    """
    Displays student progress statistics.
    """


    create_dashboard()



    tk.Label(

        content_frame,

        text="Reports Dashboard",

        font=FONT_TITLE,

        fg=COLORS["primary"],

        bg=COLORS["background"]

    ).pack(

        pady=20

    )



    missing = 0

    late = 0

    submitted = 0



    for student in students:


        if student["Status"] == "Missing":

            missing += 1


        elif student["Status"] == "Late":

            late += 1


        elif student["Status"] == "Submitted":

            submitted += 1



    statistics = [

        ("Total Students", len(students)),

        ("Missing", missing),

        ("Late", late),

        ("Submitted", submitted)

    ]



    card_frame = tk.Frame(

        content_frame,

        bg=COLORS["background"]

    )


    card_frame.pack(

        pady=20

    )



    for title, value in statistics:


        card = tk.Frame(

            card_frame,

            bg=COLORS["white"],

            width=180,

            height=110,

            relief="ridge",

            bd=2

        )


        card.pack(

            side="left",

            padx=15

        )


        card.pack_propagate(False)



        tk.Label(

            card,

            text=title,

            font=FONT_NORMAL,

            bg=COLORS["white"],

            fg=COLORS["dark"]

        ).pack(

            pady=10

        )



        tk.Label(

            card,

            text=str(value),

            font=(

                "Segoe UI",

                25,

                "bold"

            ),

            bg=COLORS["white"],

            fg=COLORS["primary"]

        ).pack()



    # ======================================================
    # STUDENTS NEEDING ATTENTION
    # ======================================================


    tk.Label(

        content_frame,

        text="Students Requiring Attention",

        font=FONT_HEADER,

        bg=COLORS["background"]

    ).pack(

        pady=20

    )



    report_box = tk.Text(

        content_frame,

        width=70,

        height=10,

        font=FONT_NORMAL

    )


    report_box.pack()



    found = False



    for student in students:


        if student["Status"] != "Submitted":


            found = True


            report_box.insert(

                tk.END,

                f"{student['Name']} - "

                f"{student['Class']} - "

                f"{student['Status']}\n"

            )



    if not found:


        report_box.insert(

            tk.END,

            "All students have submitted work."

        )



    report_box.config(

        state="disabled"

    )





# ==========================================================
# APPLICATION CLOSE
# ==========================================================

def close_program():

    """
    Saves data before closing.
    """


    save_data()


    window.destroy()





# ==========================================================
# WINDOW CLOSE EVENT
# ==========================================================

window.protocol(

    "WM_DELETE_WINDOW",

    close_program

)





# ==========================================================
# START APPLICATION
# ==========================================================

login_screen()


window.mainloop()