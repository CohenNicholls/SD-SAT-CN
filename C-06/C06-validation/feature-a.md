# C06 Feature Evidence File — Feature a

Student name:  Cohen Nicholls

Project name:  EduTrack

Feature name:  Add Student Window

Date committed:  30/7/2026

---
```
# ==========================================================
# ADD STUDENT WINDOW
# ==========================================================
# C641: function creates the add student window feature
def add_student_window(refresh):

    """
    Creates a new student record.
    """

    # C652: object created from the Tkinter Toplevel class
    popup = tk.Toplevel(window)

    # C627: GUI window control used to display the add student window
    popup.title(
        "Add Student"
    )

    popup.geometry(
        "350x450"
    )


    # C637: dictionary data structure stores multiple entry controls
    entries = {}


    # C632: iteration repeats through each required student field
    for field in ["Name", "ID"]:

        # C633: GUI label control displays field names
        tk.Label(
            popup,
            text=field
        ).pack()


        # C633: GUI entry control allows user input
        entry = tk.Entry(
            popup
        )

        entry.pack()


        # C621: local variable stores each entry widget in the dictionary
        entries[field] = entry



    # C633: GUI label control displays class option
    tk.Label(
        popup,
        text="Class"
    ).pack()


    # C633: GUI combobox control allows class selection
    class_box = ttk.Combobox(

        popup,

        # C622: constant list stores available class choices
        values=CLASSES,

        state="readonly"

    )


    class_box.pack()



    # C633: GUI label control displays status option
    tk.Label(
        popup,
        text="Status"
    ).pack()



    # C633: GUI combobox control allows status selection
    status_box = ttk.Combobox(

        popup,

        # C622: constant list stores available status choices
        values=STATUSES,

        state="readonly"

    )


    status_box.pack()



    # C641: nested function handles saving student data
    def save():


        # C621: local variable stores the entered student ID
        # C613: text data is stored because IDs are entered as characters
        student_id = entries["ID"].get()



        # C624: conditional operators check whether the ID is invalid
        if not student_id.isdigit() or len(student_id) != 10:


            messagebox.showwarning(

                "Invalid ID",

                "Student ID must contain exactly 10 digits."

            )

            return



        # C632: iteration checks each existing student record
        for student in students:


            # C623: logical comparison checks matching student IDs
            if student["ID"] == student_id:


                messagebox.showwarning(

                    "Duplicate ID",

                    "Student already exists."

                )

                return



        # C624: conditional operators check whether required fields are blank
        if class_box.get() == "" or status_box.get() == "":

            messagebox.showwarning(

                "Missing Details",

                "Select a class and status."

            )

            return



        # C632: method adds a new student record to the list
        students.append(

            {

                # C614: numeric data stores a generated record ID
                "RecordID": len(students) + 1,

                # C613: text data stores the student's name
                "Name": entries["Name"].get(),

                # C613: text data stores the student ID
                "ID": student_id,

                # C613: text data stores the selected class
                "Class": class_box.get(),

                # C613: text data stores the selected status
                "Status": status_box.get()

            }

        )



        # C642: methods are called to save data, refresh display and close window
        save_data()

        refresh(students)

        popup.destroy()



    # C633: GUI button control allows the user to save the record
    tk.Button(

        popup,

        text="Save",

        # C642: method reference connects button to save function
        command=save

    ).pack(

        pady=20

    )


    ).pack(

        pady=20

    )
