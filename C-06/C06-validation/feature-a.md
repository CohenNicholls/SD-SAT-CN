# C06 Feature Evidence File — Feature a

Student name:  Cohen Nicholls
Project name:  EduTrack
Feature name:  Add Student Window
Date committed:  30/7/2026

---

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
