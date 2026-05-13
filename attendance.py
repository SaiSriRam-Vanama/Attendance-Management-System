from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import mysql.connector
from tkinter import messagebox
from datetime import datetime
import csv
from tkinter import filedialog

mydata = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Attendance Panel")

        self.var_id = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attend = StringVar()

        img = Image.open("Images_GUI/banner.jpg")
        img = img.resize((1366, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        bg1 = Image.open("Images_GUI/bg2.jpg")
        bg1 = bg1.resize((1366, 768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        title_lb1 = Label(bg_img, text="Welcome to Attendance Panel",
                          font=("Segoe UI", 24, "bold"), bg="white", fg="#1a1a2e")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=50, width=1355, height=520)

        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Details", font=("Segoe UI", 12, "bold"), fg="#1a1a2e")
        left_frame.place(x=10, y=5, width=660, height=500)

        fields = [
            ("Std-ID:", "var_id", 0, 0),
            ("Roll.No:", "var_roll", 0, 2),
            ("Std-Name:", "var_name", 1, 0),
            ("Time:", "var_time", 1, 2),
            ("Date:", "var_date", 2, 0),
        ]
        for label, var, row, col in fields:
            lbl = Label(left_frame, text=label, font=("Segoe UI", 11, "bold"),
                        fg="#1a1a2e", bg="white")
            lbl.grid(row=row, column=col, padx=5, pady=4, sticky=W)
            entry = ttk.Entry(left_frame, textvariable=getattr(self, var),
                              width=16, font=("Segoe UI", 11))
            entry.grid(row=row, column=col + 1, padx=5, pady=4, sticky=W)

        attend_label = Label(left_frame, text="Attend-status:", font=("Segoe UI", 11, "bold"),
                             fg="#1a1a2e", bg="white")
        attend_label.grid(row=2, column=2, padx=5, pady=4, sticky=W)
        attend_combo = ttk.Combobox(left_frame, textvariable=self.var_attend,
                                    width=14, font=("Segoe UI", 11), state="readonly")
        attend_combo["values"] = ("Status", "Present", "Absent")
        attend_combo.current(0)
        attend_combo.grid(row=2, column=3, padx=5, pady=4, sticky=W)

        table_frame = Frame(left_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=85, width=635, height=335)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendanceReport_left = ttk.Treeview(
            table_frame,
            column=("ID", "Roll_No", "Name", "Time", "Date", "Attend"),
            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendanceReport_left.xview)
        scroll_y.config(command=self.attendanceReport_left.yview)

        col_data = [("ID", "Std-ID"), ("Roll_No", "Roll.No"), ("Name", "Std-Name"),
                    ("Time", "Time"), ("Date", "Date"), ("Attend", "Attend-status")]
        for col, text in col_data:
            self.attendanceReport_left.heading(col, text=text)
            self.attendanceReport_left.column(col, width=105)

        self.attendanceReport_left["show"] = "headings"
        self.attendanceReport_left.pack(fill=BOTH, expand=1)
        self.attendanceReport_left.bind("<ButtonRelease>", self.get_cursor_left)

        btn_frame = Frame(left_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=10, y=430, width=635, height=55)

        btn_defs = [
            ("Import CSV", self.importCsv, 0),
            ("Export CSV", self.exportCsv, 1),
            ("Update", self.action, 2),
            ("Reset", self.reset_data, 3),
        ]
        for text, cmd, col in btn_defs:
            btn = Button(btn_frame, command=cmd, text=text, width=11,
                         font=("Segoe UI", 11, "bold"), fg="white", bg="#1a1a2e",
                         bd=0, activebackground="#e94560", activeforeground="white", cursor="hand2")
            btn.grid(row=0, column=col, padx=5, pady=8)

        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Attendance Records", font=("Segoe UI", 12, "bold"), fg="#1a1a2e")
        right_frame.place(x=680, y=5, width=660, height=500)

        table_frame2 = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame2.place(x=10, y=5, width=635, height=380)

        scroll_x2 = ttk.Scrollbar(table_frame2, orient=HORIZONTAL)
        scroll_y2 = ttk.Scrollbar(table_frame2, orient=VERTICAL)

        self.attendanceReport = ttk.Treeview(
            table_frame2,
            column=("ID", "Roll_No", "Name", "Time", "Date", "Attend"),
            xscrollcommand=scroll_x2.set, yscrollcommand=scroll_y2.set
        )
        scroll_x2.pack(side=BOTTOM, fill=X)
        scroll_y2.pack(side=RIGHT, fill=Y)
        scroll_x2.config(command=self.attendanceReport.xview)
        scroll_y2.config(command=self.attendanceReport.yview)

        for col, text in col_data:
            self.attendanceReport.heading(col, text=text)
            self.attendanceReport.column(col, width=105)

        self.attendanceReport["show"] = "headings"
        self.attendanceReport.pack(fill=BOTH, expand=1)
        self.attendanceReport.bind("<ButtonRelease>", self.get_cursor_right)
        self.fetch_data()

        btn_frame2 = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame2.place(x=10, y=395, width=635, height=55)

        btn2_defs = [
            ("Update", self.update_data, 0),
            ("Delete", self.delete_data, 1),
        ]
        for text, cmd, col in btn2_defs:
            btn = Button(btn_frame2, command=cmd, text=text, width=11,
                         font=("Segoe UI", 11, "bold"), fg="white", bg="#1a1a2e",
                         bd=0, activebackground="#e94560", activeforeground="white", cursor="hand2")
            btn.grid(row=0, column=col, padx=5, pady=8)

    def update_data(self):
        if self.var_id.get() == "" or self.var_roll.get() == "" or self.var_name.get() == "" or \
           self.var_time.get() == "" or self.var_date.get() == "" or self.var_attend.get() == "Status":
            messagebox.showerror("Error", "All Fields Required!", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Update this record?", parent=self.root)
                if Update:
                    conn = mysql.connector.connect(username='root', password='root',
                                                   host='localhost', database='face_recognition', port=3307)
                    mycursor = conn.cursor()
                    mycursor.execute(
                        "update stdattendance set std_id=%s,std_roll_no=%s,std_name=%s,"
                        "std_time=%s,std_date=%s,std_attendance=%s where std_id=%s",
                        (self.var_id.get(), self.var_roll.get(), self.var_name.get(),
                         self.var_time.get(), self.var_date.get(), self.var_attend.get(),
                         self.var_id.get())
                    )
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Updated!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Student ID Required!", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Delete this record?", parent=self.root)
                if delete:
                    conn = mysql.connector.connect(username='root', password='root',
                                                   host='localhost', database='face_recognition', port=3307)
                    mycursor = conn.cursor()
                    mycursor.execute("delete from stdattendance where std_id=%s", (self.var_id.get(),))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Deleted", "Record Deleted!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(username='root', password='root',
                                           host='localhost', database='face_recognition', port=3307)
            mycursor = conn.cursor()
            mycursor.execute("select * from stdattendance")
            data = mycursor.fetchall()
            if len(data) != 0:
                self.attendanceReport.delete(*self.attendanceReport.get_children())
                for i in data:
                    self.attendanceReport.insert("", END, values=i)
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def reset_data(self):
        self.var_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("Status")

    def fetchData(self, rows):
        global mydata
        mydata = rows
        self.attendanceReport_left.delete(*self.attendanceReport_left.get_children())
        for i in rows:
            self.attendanceReport_left.insert("", END, values=i)

    def importCsv(self):
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",
                                         filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
                                         parent=self.root)
        if fln:
            with open(fln) as myfile:
                csvread = csv.reader(myfile, delimiter=",")
                for i in csvread:
                    mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("Error", "No Data Found!", parent=self.root)
                return
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV",
                                               filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
                                               parent=self.root)
            if fln:
                with open(fln, mode="w", newline="") as myfile:
                    exp_write = csv.writer(myfile, delimiter=",")
                    for i in mydata:
                        exp_write.writerow(i)
                messagebox.showinfo("Success", "Export Successful!")
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def get_cursor_left(self, event=""):
        cursor_focus = self.attendanceReport_left.focus()
        content = self.attendanceReport_left.item(cursor_focus)
        data = content["values"]
        if data:
            self.var_id.set(data[0])
            self.var_roll.set(data[1])
            self.var_name.set(data[2])
            self.var_time.set(data[3])
            self.var_date.set(data[4])
            self.var_attend.set(data[5])

    def get_cursor_right(self, event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]
        if data:
            self.var_id.set(data[0])
            self.var_roll.set(data[1])
            self.var_name.set(data[2])
            self.var_time.set(data[3])
            self.var_date.set(data[4])
            self.var_attend.set(data[5])

    def action(self):
        if self.var_id.get() == "" or self.var_roll.get() == "" or self.var_name.get() == "" or \
           self.var_time.get() == "" or self.var_date.get() == "" or self.var_attend.get() == "Status":
            messagebox.showerror("Error", "All Fields Required!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='root',
                                               host='localhost', database='face_recognition', port=3307)
                mycursor = conn.cursor()
                mycursor.execute("insert into stdattendance values(%s,%s,%s,%s,%s,%s)", (
                    self.var_id.get(), self.var_roll.get(), self.var_name.get(),
                    self.var_time.get(), self.var_date.get(), self.var_attend.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Records Saved to Database!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
