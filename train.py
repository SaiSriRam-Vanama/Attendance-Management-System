from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import cv2
import numpy as np
from tkinter import messagebox


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Train Panel")

        img = Image.open("Images_GUI/banner.jpg")
        img = img.resize((1366, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        bg1 = Image.open("Images_GUI/t_bg1.jpg")
        bg1 = bg1.resize((1366, 768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        title_lb1 = Label(bg_img, text="Welcome to Training Panel",
                          font=("Segoe UI", 24, "bold"), bg="white", fg="#1a1a2e")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        std_img_btn = Image.open("Images_GUI/t_btn1.png")
        std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.train_classifier,
                        image=self.std_img1, cursor="hand2", bd=0)
        std_b1.place(x=600, y=170, width=180, height=180)

        std_b1_1 = Button(bg_img, command=self.train_classifier, text="Train Dataset",
                          cursor="hand2", font=("Segoe UI", 14, "bold"),
                          bg="white", fg="#1a1a2e", bd=0,
                          activebackground="#e94560", activeforeground="white")
        std_b1_1.place(x=600, y=355, width=180, height=40)

    def train_classifier(self):
        data_dir = "data_img"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("clf.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Completed!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
