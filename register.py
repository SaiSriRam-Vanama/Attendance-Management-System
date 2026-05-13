from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1366x768+0+0")

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_cnum = StringVar()
        self.var_email = StringVar()
        self.var_ssq = StringVar()
        self.var_sa = StringVar()
        self.var_pwd = StringVar()
        self.var_cpwd = StringVar()
        self.var_check = IntVar()

        self.bg = ImageTk.PhotoImage(file="Images_GUI/bgReg.jpg")
        lb1_bg = Label(self.root, image=self.bg)
        lb1_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="#1a1a2e")
        frame.place(x=100, y=80, width=900, height=580)

        get_str = Label(frame, text="Registration", font=("Segoe UI", 26, "bold"),
                        fg="#e94560", bg="#1a1a2e")
        get_str.place(x=350, y=40)

        fields_left = [
            ("First Name:", "var_fname", 100, 130),
            ("Last Name:", "var_lname", 100, 200),
            ("Security Question:", None, 100, 270),
            ("Security Answer:", "var_sa", 100, 340),
        ]
        fields_right = [
            ("Contact No:", "var_cnum", 530, 130),
            ("Email:", "var_email", 530, 200),
            ("Password:", "var_pwd", 530, 270),
            ("Confirm Password:", "var_cpwd", 530, 340),
        ]

        for label, var, x, y in fields_left:
            lbl = Label(frame, text=label, font=("Segoe UI", 12, "bold"),
                        fg="white", bg="#1a1a2e")
            lbl.place(x=x, y=y)
            if var:
                is_pwd = "pwd" in var.lower() or var == "var_pwd"
                entry = ttk.Entry(frame, textvariable=getattr(self, var),
                                  font=("Segoe UI", 12), show="*" if is_pwd else "")
                entry.place(x=x + 3, y=y + 25, width=270)

        for label, var, x, y in fields_right:
            lbl = Label(frame, text=label, font=("Segoe UI", 12, "bold"),
                        fg="white", bg="#1a1a2e")
            lbl.place(x=x, y=y)
            if var:
                is_pwd = "pwd" in var.lower() or var == "var_pwd"
                entry = ttk.Entry(frame, textvariable=getattr(self, var),
                                  font=("Segoe UI", 12), show="*" if is_pwd else "")
                entry.place(x=x + 3, y=y + 25, width=270)

        self.combo_security = ttk.Combobox(frame, textvariable=self.var_ssq,
                                           font=("Segoe UI", 12), state="readonly")
        self.combo_security["values"] = ("Select", "Your Date of Birth", "Your Nick Name", "Your Favorite Book")
        self.combo_security.current(0)
        self.combo_security.place(x=103, y=295, width=270)

        checkbtn = Checkbutton(frame, variable=self.var_check,
                               text="I Agree the Terms & Conditions",
                               font=("Segoe UI", 11, "bold"), fg="#e94560",
                               bg="#1a1a2e", selectcolor="#1a1a2e",
                               activebackground="#1a1a2e", activeforeground="#e94560")
        checkbtn.place(x=100, y=420)

        regbtn = Button(frame, command=self.reg, text="Register",
                        font=("Segoe UI", 14, "bold"), bd=0, relief=RIDGE,
                        fg="white", bg="#e94560", activeforeground="white", activebackground="#c23152")
        regbtn.place(x=103, y=470, width=270, height=40)

        loginbtn = Button(frame, text="Login", font=("Segoe UI", 14, "bold"),
                          bd=0, relief=RIDGE, fg="white", bg="#0f3460",
                          activeforeground="white", activebackground="#e94560")
        loginbtn.place(x=533, y=470, width=270, height=40)

    def reg(self):
        if (self.var_fname.get() == "" or self.var_lname.get() == "" or
            self.var_cnum.get() == "" or self.var_email.get() == "" or
            self.var_ssq.get() == "Select" or self.var_sa.get() == "" or
            self.var_pwd.get() == "" or self.var_cpwd.get() == ""):
            messagebox.showerror("Error", "All Fields Required!")
        elif self.var_pwd.get() != self.var_cpwd.get():
            messagebox.showerror("Error", "Passwords do not match!")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to Terms & Conditions!")
        else:
            try:
                conn = mysql.connector.connect(username='root', password='root',
                                               host='localhost', database='face_recognition', port=3307)
                mycursor = conn.cursor()
                mycursor.execute("select * from regteach where email=%s", (self.var_email.get(),))
                if mycursor.fetchone() is not None:
                    messagebox.showerror("Error", "Email already registered!")
                else:
                    mycursor.execute("insert into regteach values(%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_fname.get(), self.var_lname.get(), self.var_cnum.get(),
                        self.var_email.get(), self.var_ssq.get(), self.var_sa.get(), self.var_pwd.get()
                    ))
                    conn.commit()
                    messagebox.showinfo("Success", "Registration Successful!", parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
