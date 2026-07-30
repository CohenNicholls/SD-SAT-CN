# C06 Feature Evidence File — Feature c

Student name:  Cohen Nicholls,
Project name:  EduTrack,
Feature name:  Reminder Page,
Date committed:  30/7/26,

---

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
