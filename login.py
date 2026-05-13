from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
import os


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")

        self.var_ssq = StringVar()
        self.var_sa = StringVar()
        self.var_pwd = StringVar()

        self.bg = ImageTk.PhotoImage(file="Images_GUI/loginBg1.jpg")
        lb1_bg = Label(self.root, image=self.bg)
        lb1_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame1 = Frame(self.root, bg="#1a1a2e")
        frame1.place(x=560, y=170, width=340, height=450)

        img1 = Image.open("Images_GUI/log1.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lb1img1 = Label(image=self.photoimage1, bg="#1a1a2e")
        lb1img1.place(x=690, y=175, width=100, height=100)

        get_str = Label(frame1, text="Login", font=("Segoe UI", 22, "bold"), fg="white", bg="#1a1a2e")
        get_str.place(x=140, y=100)

        username = Label(frame1, text="Username:", font=("Segoe UI", 14, "bold"), fg="white", bg="#1a1a2e")
        username.place(x=30, y=160)
        self.txtuser = ttk.Entry(frame1, font=("Segoe UI", 14))
        self.txtuser.place(x=33, y=190, width=270)

        pwd = Label(frame1, text="Password:", font=("Segoe UI", 14, "bold"), fg="white", bg="#1a1a2e")
        pwd.place(x=30, y=230)
        self.txtpwd = ttk.Entry(frame1, font=("Segoe UI", 14), show="*")
        self.txtpwd.place(x=33, y=260, width=270)

        loginbtn = Button(frame1, command=self.login, text="Login",
                          font=("Segoe UI", 14, "bold"), bd=0, relief=RIDGE,
                          fg="white", bg="#e94560", activeforeground="white", activebackground="#c23152")
        loginbtn.place(x=33, y=320, width=270, height=40)

        regbtn = Button(frame1, command=self.reg, text="Register",
                        font=("Segoe UI", 10, "bold"), bd=0, relief=RIDGE,
                        fg="#e94560", bg="#1a1a2e", activeforeground="white", activebackground="#e94560")
        regbtn.place(x=33, y=370, width=70, height=25)

        forgbtn = Button(frame1, command=self.forget_pwd, text="Forget Password",
                         font=("Segoe UI", 10, "bold"), bd=0, relief=RIDGE,
                         fg="#e94560", bg="#1a1a2e", activeforeground="white", activebackground="#e94560")
        forgbtn.place(x=110, y=370, width=120, height=25)

    def reg(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpwd.get() == "":
            messagebox.showerror("Error", "All Fields Required!")
        elif self.txtuser.get() == "admin" and self.txtpwd.get() == "admin":
            messagebox.showinfo("Success", "Welcome to Attendance Management System")
            self.open_main()
        else:
            try:
                conn = mysql.connector.connect(username='root', password='root',
                                               host='localhost', database='face_recognition', port=3307)
                mycursor = conn.cursor()
                mycursor.execute("select * from regteach where email=%s and pwd=%s", (
                    self.txtuser.get(), self.txtpwd.get()
                ))
                row = mycursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Username or Password!")
                else:
                    open_min = messagebox.askyesno("Access", "Open Admin Panel?")
                    if open_min:
                        self.open_main()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Database Error: {str(e)}")

    def open_main(self):
        from main import Face_Recognition_System
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition_System(self.new_window)

    def reset_pass(self):
        if self.var_ssq.get() == "Select":
            messagebox.showerror("Error", "Select Security Question!", parent=self.root2)
        elif self.var_sa.get() == "":
            messagebox.showerror("Error", "Please Enter the Answer!", parent=self.root2)
        elif self.var_pwd.get() == "":
            messagebox.showerror("Error", "Please Enter New Password!", parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='root',
                                               host='localhost', database='face_recognition', port=3307)
                mycursor = conn.cursor()
                mycursor.execute("select * from regteach where email=%s and ss_que=%s and s_ans=%s",
                                 (self.txtuser.get(), self.var_ssq.get(), self.var_sa.get()))
                row = mycursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Incorrect Answer!", parent=self.root2)
                else:
                    mycursor.execute("update regteach set pwd=%s where email=%s",
                                     (self.var_pwd.get(), self.txtuser.get()))
                    conn.commit()
                    messagebox.showinfo("Success", "Password Reset Successfully!", parent=self.root2)
                    self.root2.destroy()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root2)

    def forget_pwd(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter Email to reset Password!")
            return
        try:
            conn = mysql.connector.connect(username='root', password='root',
                                           host='localhost', database='face_recognition', port=3307)
            mycursor = conn.cursor()
            mycursor.execute("select * from regteach where email=%s", (self.txtuser.get(),))
            row = mycursor.fetchone()
            conn.close()
            if row is None:
                messagebox.showerror("Error", "Email not found!")
                return
        except Exception as e:
            messagebox.showerror("Error", f"Database Error: {str(e)}")
            return

        self.root2 = Toplevel()
        self.root2.title("Forget Password")
        self.root2.geometry("400x400+610+170")
        self.root2.configure(bg="#1a1a2e")

        l = Label(self.root2, text="Forget Password", font=("Segoe UI", 26, "bold"),
                  fg="#e94560", bg="#1a1a2e")
        l.place(x=0, y=10, relwidth=1)

        ssq = Label(self.root2, text="Select Security Question:",
                    font=("Segoe UI", 12, "bold"), fg="white", bg="#1a1a2e")
        ssq.place(x=70, y=80)
        self.combo_security = ttk.Combobox(self.root2, textvariable=self.var_ssq,
                                           font=("Segoe UI", 12), state="readonly")
        self.combo_security["values"] = ("Select", "Your Date of Birth", "Your Nick Name", "Your Favorite Book")
        self.combo_security.current(0)
        self.combo_security.place(x=70, y=110, width=270)

        sa = Label(self.root2, text="Security Answer:", font=("Segoe UI", 12, "bold"),
                   fg="white", bg="#1a1a2e")
        sa.place(x=70, y=150)
        self.txtsa = ttk.Entry(self.root2, textvariable=self.var_sa, font=("Segoe UI", 12))
        self.txtsa.place(x=70, y=180, width=270)

        new_pwd = Label(self.root2, text="New Password:", font=("Segoe UI", 12, "bold"),
                        fg="white", bg="#1a1a2e")
        new_pwd.place(x=70, y=220)
        self.new_pwd = ttk.Entry(self.root2, textvariable=self.var_pwd, font=("Segoe UI", 12), show="*")
        self.new_pwd.place(x=70, y=250, width=270)

        loginbtn = Button(self.root2, command=self.reset_pass, text="Reset Password",
                          font=("Segoe UI", 14, "bold"), bd=0, relief=RIDGE,
                          fg="white", bg="#e94560", activeforeground="white", activebackground="#c23152")
        loginbtn.place(x=70, y=300, width=270, height=35)


if __name__ == "__main__":
    root = Tk()
    app = Login(root)
    root.mainloop()
