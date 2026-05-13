from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from helpsupport import Helpsupport
import os

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Attendance Management System")

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

        title_lb1 = Label(bg_img, text="Attendance Management System Using Facial Recognition",
                          font=("Segoe UI", 24, "bold"), bg="white", fg="#1a1a2e")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        buttons = [
            ("std1.jpg", "Student Panel", self.student_pannels, 250, 110),
            ("det1.jpg", "Face Detector", self.face_rec, 480, 110),
            ("att.jpg", "Attendance", self.attendance_pannel, 710, 110),
            ("hlp.jpg", "Help Support", self.helpSupport, 940, 110),
            ("tra1.jpg", "Data Train", self.train_pannels, 250, 340),
            ("qr1.png", "QR-Codes", self.open_img, 480, 340),
            ("dev.jpg", "Developers", self.developr, 710, 340),
            ("exi.jpg", "Exit", self.Close, 940, 340),
        ]

        for i, (img_name, text, cmd, x, y) in enumerate(buttons):
            img_btn = Image.open(f"Images_GUI/{img_name}")
            img_btn = img_btn.resize((180, 180), Image.LANCZOS)
            key = img_name.split('.')[0]
            setattr(self, f"{key}_img", ImageTk.PhotoImage(img_btn))
            btn = Button(bg_img, command=cmd, image=getattr(self, f"{key}_img"),
                         cursor="hand2", bd=0, highlightthickness=0)
            btn.place(x=x, y=y, width=180, height=180)
            lbl = Button(bg_img, command=cmd, text=text, cursor="hand2",
                         font=("Segoe UI", 14, "bold"), bg="white", fg="#1a1a2e",
                         bd=0, activebackground="#e94560", activeforeground="white")
            lbl.place(x=x, y=y + 185, width=180, height=40)

    def open_img(self):
        os.startfile("data_img")

    def student_pannels(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_pannels(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_rec(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_pannel(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developr(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def helpSupport(self):
        self.new_window = Toplevel(self.root)
        self.app = Helpsupport(self.new_window)

    def Close(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
