# C06 Feature Evidence File — Feature b

Student name:  Cohen Nicholls
Project name:  EduTrack
Feature name:  Filter Class
Date committed:  30/7/2026

---

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
