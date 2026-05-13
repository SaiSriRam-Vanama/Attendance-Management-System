from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Panel")

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_mob = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio1 = StringVar()

        img = Image.open("Images_GUI/banner.jpg")
        img = img.resize((1366, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        bg1 = Image.open("Images_GUI/bg3.jpg")
        bg1 = bg1.resize((1366, 768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        title_lb1 = Label(bg_img, text="Welcome to Student Panel",
                          font=("Segoe UI", 24, "bold"), bg="white", fg="#1a1a2e")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=50, width=1355, height=520)

        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Details", font=("Segoe UI", 12, "bold"), fg="#1a1a2e")
        left_frame.place(x=10, y=5, width=660, height=500)

        current_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE,
                                          text="Current Course", font=("Segoe UI", 12, "bold"), fg="#1a1a2e")
        current_course_frame.place(x=10, y=5, width=635, height=120)

        dep_label = Label(current_course_frame, text="Department",
                          font=("Segoe UI", 11, "bold"), bg="white", fg="#1a1a2e")
        dep_label.grid(row=0, column=0, padx=5, pady=8, sticky=W)
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep,
                                 width=18, font=("Segoe UI", 11), state="readonly")
        dep_combo["values"] = ("Select Department", "BSCS", "BSIT", "BSENG", "BSPHY", "BSMATH")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=5, pady=8, sticky=W)

        cou_label = Label(current_course_frame, text="Course",
                          font=("Segoe UI", 11, "bold"), bg="white", fg="#1a1a2e")
        cou_label.grid(row=0, column=2, padx=5, pady=8)
        cou_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course,
                                 width=18, font=("Segoe UI", 11), state="readonly")
        cou_combo["values"] = ("Select Course", "SE", "FE", "TE", "BE", "MS")
        cou_combo.current(0)
        cou_combo.grid(row=0, column=3, padx=5, pady=8, sticky=W)

        year_label = Label(current_course_frame, text="Year",
                           font=("Segoe UI", 11, "bold"), bg="white", fg="#1a1a2e")
        year_label.grid(row=1, column=0, padx=5, sticky=W)
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year,
                                  width=18, font=("Segoe UI", 11), state="readonly")
        year_combo["values"] = ("Select Year", "2017-21", "2018-22", "2019-23", "2020-24", "2021-25")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=5, pady=8, sticky=W)

        sem_label = Label(current_course_frame, text="Semester",
                          font=("Segoe UI", 11, "bold"), bg="white", fg="#1a1a2e")
        sem_label.grid(row=1, column=2, padx=5, sticky=W)
        sem_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester,
                                 width=18, font=("Segoe UI", 11), state="readonly")
        sem_combo["values"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3",
                               "Semester-4", "Semester-5", "Semester-6", "Semester-7", "Semester-8")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=5, pady=8, sticky=W)

        class_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Class Student Information", font=("Segoe UI", 12, "bold"), fg="#1a1a2e")
        class_frame.place(x=10, y=130, width=635, height=280)

        fields = [
            ("Std-ID:", "var_std_id", 0, 0),
            ("Std-Name:", "var_std_name", 0, 2),
            ("Class Division:", None, 1, 0),
            ("Roll-No:", "var_roll", 1, 2),
            ("Gender:", None, 2, 0),
            ("DOB:", "var_dob", 2, 2),
            ("Email:", "var_email", 3, 0),
            ("Mob-No:", "var_mob", 3, 2),
            ("Address:", "var_address", 4, 0),
            ("Tutor Name:", "var_teacher", 4, 2),
        ]

        for label, var, row, col in fields:
            lbl = Label(class_frame, text=label, font=("Segoe UI", 11, "bold"),
                        fg="#1a1a2e", bg="white")
            lbl.grid(row=row, column=col, padx=5, pady=4, sticky=W)
            if var:
                entry = ttk.Entry(class_frame, textvariable=getattr(self, var),
                                  width=16, font=("Segoe UI", 11))
                entry.grid(row=row, column=col + 1, padx=5, pady=4, sticky=W)

        div_combo = ttk.Combobox(class_frame, textvariable=self.var_div,
                                 width=14, font=("Segoe UI", 11), state="readonly")
        div_combo["values"] = ("Morning", "Evening")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=5, pady=4, sticky=W)

        gender_combo = ttk.Combobox(class_frame, textvariable=self.var_gender,
                                    width=14, font=("Segoe UI", 11), state="readonly")
        gender_combo["values"] = ("Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=5, pady=4, sticky=W)

        radiobtn1 = ttk.Radiobutton(class_frame, text="Take Photo Sample",
                                    variable=self.var_radio1, value="Yes")
        radiobtn1.grid(row=5, column=0, padx=5, pady=6, sticky=W)
        radiobtn2 = ttk.Radiobutton(class_frame, text="No Photo Sample",
                                    variable=self.var_radio1, value="No")
        radiobtn2.grid(row=5, column=1, padx=5, pady=6, sticky=W)

        btn_frame = Frame(left_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=10, y=420, width=635, height=55)

        btn_data = [
            ("Save", self.add_data, 0), ("Update", self.update_data, 1),
            ("Delete", self.delete_data, 2), ("Reset", self.reset_data, 3),
            ("Take Pic", self.generate_dataset, 4), ("Update Pic", None, 5),
        ]
        for text, cmd, col in btn_data:
            btn = Button(btn_frame, command=cmd, text=text,
                         width=9, font=("Segoe UI", 11, "bold"), fg="white", bg="#1a1a2e",
                         bd=0, activebackground="#e94560", activeforeground="white",
                         cursor="hand2")
            btn.grid(row=0, column=col, padx=3, pady=8)

        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Student Records", font=("Segoe UI", 12, "bold"), fg="#1a1a2e")
        right_frame.place(x=680, y=5, width=660, height=500)

        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE,
                                  text="Search System", font=("Segoe UI", 12, "bold"), fg="#1a1a2e")
        search_frame.place(x=10, y=5, width=635, height=75)

        search_label = Label(search_frame, text="Search:", font=("Segoe UI", 11, "bold"),
                             fg="#1a1a2e", bg="white")
        search_label.grid(row=0, column=0, padx=5, pady=8, sticky=W)
        self.var_searchTX = StringVar()
        search_combo = ttk.Combobox(search_frame, textvariable=self.var_searchTX,
                                    width=10, font=("Segoe UI", 11), state="readonly")
        search_combo["values"] = ("Select", "Roll-No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=8, sticky=W)

        self.var_search = StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.var_search,
                                 width=10, font=("Segoe UI", 11))
        search_entry.grid(row=0, column=2, padx=5, pady=8, sticky=W)

        search_btn = Button(search_frame, command=self.search_data, text="Search",
                            width=8, font=("Segoe UI", 11, "bold"), fg="white",
                            bg="#1a1a2e", bd=0, activebackground="#e94560", cursor="hand2")
        search_btn.grid(row=0, column=3, padx=5, pady=8, sticky=W)

        showAll_btn = Button(search_frame, command=self.fetch_data, text="Show All",
                             width=8, font=("Segoe UI", 11, "bold"), fg="white",
                             bg="#1a1a2e", bd=0, activebackground="#e94560", cursor="hand2")
        showAll_btn.grid(row=0, column=4, padx=5, pady=8, sticky=W)

        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=85, width=635, height=400)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            column=("ID", "Name", "Dep", "Course", "Year", "Sem", "Div",
                    "Gender", "DOB", "Mob-No", "Address", "Roll-No", "Email", "Teacher", "Photo"),
            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        col_widths = {"ID": 80, "Name": 100, "Dep": 90, "Course": 80, "Year": 80,
                      "Sem": 90, "Div": 80, "Gender": 70, "DOB": 80, "Mob-No": 90,
                      "Address": 100, "Roll-No": 70, "Email": 120, "Teacher": 100, "Photo": 90}
        for col, text in [
            ("ID", "StudentID"), ("Name", "Name"), ("Dep", "Department"),
            ("Course", "Course"), ("Year", "Year"), ("Sem", "Semester"),
            ("Div", "Division"), ("Gender", "Gender"), ("DOB", "DOB"),
            ("Mob-No", "Mob-No"), ("Address", "Address"), ("Roll-No", "Roll-No"),
            ("Email", "Email"), ("Teacher", "Teacher"), ("Photo", "PhotoSample")
        ]:
            self.student_table.heading(col, text=text)
            self.student_table.column(col, width=col_widths[col])

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or \
           self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or \
           self.var_std_id.get() == "" or self.var_std_name.get() == "" or \
           self.var_div.get() == "" or self.var_roll.get() == "" or \
           self.var_gender.get() == "" or self.var_dob.get() == "" or \
           self.var_email.get() == "" or self.var_mob.get() == "" or \
           self.var_address.get() == "" or self.var_teacher.get() == "":
            messagebox.showerror("Error", "Please Fill All Fields!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='root',
                                               host='localhost', database='face_recognition', port=3307)
                mycursor = conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_std_id.get(), self.var_std_name.get(), self.var_dep.get(),
                    self.var_course.get(), self.var_year.get(), self.var_semester.get(),
                    self.var_div.get(), self.var_gender.get(), self.var_dob.get(),
                    self.var_mob.get(), self.var_address.get(), self.var_roll.get(),
                    self.var_email.get(), self.var_teacher.get(), self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Records Saved!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(username='root', password='root',
                                           host='localhost', database='face_recognition', port=3307)
            mycursor = conn.cursor()
            mycursor.execute("select * from student")
            data = mycursor.fetchall()
            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        if data:
            self.var_std_id.set(data[0])
            self.var_std_name.set(data[1])
            self.var_dep.set(data[2])
            self.var_course.set(data[3])
            self.var_year.set(data[4])
            self.var_semester.set(data[5])
            self.var_div.set(data[6])
            self.var_gender.set(data[7])
            self.var_dob.set(data[8])
            self.var_mob.set(data[9])
            self.var_address.set(data[10])
            self.var_roll.set(data[11])
            self.var_email.set(data[12])
            self.var_teacher.set(data[13])
            self.var_radio1.set(data[14])

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or \
           self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or \
           self.var_std_id.get() == "":
            messagebox.showerror("Error", "Please Fill All Fields!", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Update this record?", parent=self.root)
                if Update:
                    conn = mysql.connector.connect(username='root', password='root',
                                                   host='localhost', database='face_recognition', port=3307)
                    mycursor = conn.cursor()
                    mycursor.execute(
                        "update student set Name=%s,Department=%s,Course=%s,Year=%s,Semester=%s,"
                        "Division=%s,Gender=%s,DOB=%s,Mobile_No=%s,Address=%s,Roll_No=%s,"
                        "Email=%s,Teacher_Name=%s,PhotoSample=%s where Student_ID=%s",
                        (self.var_std_name.get(), self.var_dep.get(), self.var_course.get(),
                         self.var_year.get(), self.var_semester.get(), self.var_div.get(),
                         self.var_gender.get(), self.var_dob.get(), self.var_mob.get(),
                         self.var_address.get(), self.var_roll.get(), self.var_email.get(),
                         self.var_teacher.get(), self.var_radio1.get(), self.var_std_id.get())
                    )
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Updated Successfully!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID Required!", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Delete this record?", parent=self.root)
                if delete:
                    conn = mysql.connector.connect(username='root', password='root',
                                                   host='localhost', database='face_recognition', port=3307)
                    mycursor = conn.cursor()
                    mycursor.execute("delete from student where Student_ID=%s", (self.var_std_id.get(),))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Deleted", "Record Deleted!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def reset_data(self):
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_div.set("Morning")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_mob.set("")
        self.var_address.set("")
        self.var_roll.set("")
        self.var_email.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    def search_data(self):
        if self.var_search.get() == "" or self.var_searchTX.get() == "Select":
            messagebox.showerror("Error", "Select option and enter value!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='root',
                                               host='localhost', database='face_recognition', port=3307)
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "SELECT * FROM student where Roll_No='" + str(self.var_search.get()) + "'"
                )
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("", END, values=i)
                else:
                    messagebox.showerror("Error", "No Data Found!", parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or \
           self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or \
           self.var_std_id.get() == "":
            messagebox.showerror("Error", "Please Fill All Fields!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='root',
                                               host='localhost', database='face_recognition', port=3307)
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myresult = mycursor.fetchall()
                id = len(myresult) + 1

                mycursor.execute(
                    "update student set Name=%s,Department=%s,Course=%s,Year=%s,Semester=%s,"
                    "Division=%s,Gender=%s,DOB=%s,Mobile_No=%s,Address=%s,Roll_No=%s,"
                    "Email=%s,Teacher_Name=%s,PhotoSample=%s where Student_ID=%s",
                    (self.var_std_name.get(), self.var_dep.get(), self.var_course.get(),
                     self.var_year.get(), self.var_semester.get(), self.var_div.get(),
                     self.var_gender.get(), self.var_dob.get(), self.var_mob.get(),
                     self.var_address.get(), self.var_roll.get(), self.var_email.get(),
                     self.var_teacher.get(), self.var_radio1.get(), id)
                )
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        return img[y:y + h, x:x + w]

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (200, 200))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = f"data_img/student.{id}.{img_id}.jpg"
                        cv2.imwrite(file_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Capture Images", face)
                    if cv2.waitKey(1) == 13 or img_id >= 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Dataset Generated!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
