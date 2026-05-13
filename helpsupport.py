from tkinter import *
from PIL import Image, ImageTk
import webbrowser


class Helpsupport:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Help & Support")

        img = Image.open("Images_GUI/banner.jpg")
        img = img.resize((1366, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        bg1 = Image.open("Images_GUI/bg4.png")
        bg1 = bg1.resize((1366, 768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        title_lb1 = Label(bg_img, text="Help & Support",
                          font=("Segoe UI", 24, "bold"), bg="white", fg="#1a1a2e")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        links = [
            ("web.png", "Website", self.website, 250),
            ("fb.png", "Facebook", self.facebook, 480),
            ("yt.png", "Youtube", self.youtube, 710),
            ("gmail.png", "Gmail", self.gmail, 940),
        ]

        for img_name, text, cmd, x in links:
            img_btn = Image.open(f"Images_GUI/{img_name}")
            img_btn = img_btn.resize((180, 180), Image.LANCZOS)
            setattr(self, f"img_{img_name.split('.')[0]}", ImageTk.PhotoImage(img_btn))
            btn = Button(bg_img, command=cmd, image=getattr(self, f"img_{img_name.split('.')[0]}"),
                         cursor="hand2", bd=0)
            btn.place(x=x, y=200, width=180, height=180)
            lbl = Button(bg_img, command=cmd, text=text, cursor="hand2",
                         font=("Segoe UI", 14, "bold"), bg="white", fg="#1a1a2e",
                         bd=0, activebackground="#e94560", activeforeground="white")
            lbl.place(x=x, y=385, width=180, height=40)

    def website(self):
        webbrowser.open("https://excelepre.com/")

    def facebook(self):
        webbrowser.open("https://www.facebook.com/")

    def youtube(self):
        webbrowser.open("https://www.youtube.com/channel/UCwpFCX_Z4SVkAT_6hPeUnsA")

    def gmail(self):
        webbrowser.open("https://www.gmail.com")


if __name__ == "__main__":
    root = Tk()
    obj = Helpsupport(root)
    root.mainloop()
