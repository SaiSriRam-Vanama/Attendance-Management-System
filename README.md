<div align="center">

# Attendance Management System

### Facial Recognition Based Smart Attendance Solution

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-FF6F00)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8-5C3EE8?logo=opencv&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?logo=mysql&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

**A desktop application that automates student attendance using facial recognition technology.**
Captures faces via webcam, trains a recognizer model, and marks attendance in real-time.

</div>

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Usage Guide](#usage-guide)
- [UI Theme](#ui-theme)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Contact](#contact)

---

## Features

<details>
<summary><b>Click to expand</b></summary>

### Authentication
- Secure login system with username/password
- Teacher registration with security questions
- Forgot password recovery via security questions

### Student Management
- Full CRUD operations (Add, Update, Delete, Reset)
- Search students by Roll Number
- Student details: ID, Name, Department, Course, Year, Semester, Division, Gender, DOB, Email, Mobile, Address, Tutor

### Face Capture & Training
- Capture 100 face samples per student via webcam
- Automatic face detection using Haar Cascade
- LBPH (Local Binary Patterns Histograms) model training
- Generates `clf.xml` classifier file

### Real-Time Attendance
- Live webcam face detection and recognition
- 77% confidence threshold for accurate matching
- Auto-marks attendance in CSV with timestamp
- Displays Student ID, Name, and Roll No on video feed

### Attendance Reports
- View attendance records in table format
- Import attendance from CSV files
- Export attendance to CSV files
- Store attendance in MySQL database
- Update/Delete attendance records

### Developer Info
- Team member profiles with images
- Quick links to Website, YouTube, Facebook, Gmail

</details>

---

## Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Language** | Python 3.8+ | Core programming language |
| **GUI** | Tkinter (ttk) | Desktop graphical interface |
| **Face Detection** | OpenCV (Haar Cascade) | Real-time face detection |
| **Face Recognition** | OpenCV (LBPH) | Facial recognition algorithm |
| **Image Processing** | Pillow / PIL | Image handling & GUI icons |
| **Database** | MySQL (mysql-connector) | Student & attendance records |
| **Numerical** | NumPy | Face data array operations |

---

## Project Structure

```text
Attendance-Management-System/
│
├── main.py                 # Main dashboard (8-button control panel)
├── login.py                # Login screen with auth
├── register.py             # Teacher registration
├── student.py              # Student CRUD + face capture
├── train.py                # Train LBPH face recognizer
├── face_recognition.py     # Real-time attendance marking
├── attendance.py           # Attendance records & CSV I/O
├── developer.py            # Developer profiles
├── helpsupport.py          # Help & social links
├── databaseTest.py         # MySQL connection tester
│
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── LICENSE                 # MIT License
├── .gitignore              # Git ignore rules
│
├── Images_GUI/             # UI assets (banners, icons, backgrounds)
│   ├── banner.jpg          # Header banner image
│   ├── bg3.jpg             # Main dashboard background
│   ├── log1.png            # Login icon
│   ├── std1.jpg            # Student panel icon
│   ├── det1.jpg            # Face detector icon
│   ├── att.jpg             # Attendance icon
│   ├── hlp.jpg             # Help icon
│   ├── tra1.jpg            # Train icon
│   ├── qr1.png             # QR codes icon
│   ├── dev.jpg             # Developers icon
│   ├── exi.jpg             # Exit icon
│   ├── ...and more         # Additional UI assets
│
├── data_img/               # Captured face samples (auto-generated)
│
├── haarcascade_frontalface_default.xml  # Face detection model
├── clf.xml                 # Trained recognizer model (auto-generated)
└── attendance.csv          # Attendance log file (auto-generated)
```

---

## Installation

### Prerequisites

| Requirement | Version | Download |
|-------------|---------|----------|
| Python | 3.8+ | [python.org](https://python.org) |
| MySQL Server | 8.0+ | [mysql.com](https://mysql.com) |
| Webcam | Built-in / USB | - |

### Step 1: Clone Repository

```bash
git clone https://github.com/SaiSriRam-Vanama/Attendance-Management-System.git
cd Attendance-Management-System
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

<details>
<summary><b>requirements.txt contents</b></summary>

```text
opencv-python==4.8.1.78
opencv-contrib-python==4.8.1.78
Pillow==10.1.0
mysql-connector-python==8.2.0
numpy==1.24.3
```

</details>

---

## Database Setup

### Step 1: Create Database

```sql
CREATE DATABASE face_recognition;
USE face_recognition;
```

### Step 2: Create Tables

```sql
-- Teachers table (for login/registration)
CREATE TABLE regteach (
    fname VARCHAR(50),
    lname VARCHAR(50),
    contact VARCHAR(20),
    email VARCHAR(100) PRIMARY KEY,
    ss_que VARCHAR(100),
    s_ans VARCHAR(100),
    pwd VARCHAR(50)
);

-- Students table
CREATE TABLE student (
    Student_ID VARCHAR(20) PRIMARY KEY,
    Name VARCHAR(50),
    Department VARCHAR(50),
    Course VARCHAR(50),
    Year VARCHAR(20),
    Semester VARCHAR(20),
    Division VARCHAR(20),
    Gender VARCHAR(10),
    DOB VARCHAR(20),
    Mobile_No VARCHAR(20),
    Address VARCHAR(100),
    Roll_No VARCHAR(20),
    Email VARCHAR(100),
    Teacher_Name VARCHAR(50),
    PhotoSample VARCHAR(10)
);

-- Attendance table
CREATE TABLE stdattendance (
    std_id VARCHAR(20),
    std_roll_no VARCHAR(20),
    std_name VARCHAR(50),
    std_time VARCHAR(20),
    std_date VARCHAR(20),
    std_attendance VARCHAR(20)
);
```

### Step 3: Configure Connection

Update credentials in all `.py` files if your setup differs:

| Parameter | Default Value |
|-----------|--------------|
| **Host** | `localhost` |
| **Port** | `3307` |
| **User** | `root` |
| **Password** | `root` |
| **Database** | `face_recognition` |

---

## Usage Guide

### First Time Setup

```bash
python login.py
```

| Step | Action | Description |
|------|--------|-------------|
| 1 | **Register** | Create a teacher account (or use `admin`/`admin`) |
| 2 | **Login** | Enter credentials to access the dashboard |

### Adding Students

```mermaid
graph LR
    A[Dashboard] --> B[Student Panel]
    B --> C[Fill Details]
    C --> D[Save to DB]
    D --> E[Take Pic]
    E --> F[100 Samples Captured]
```

1. Click **Student Panel** from dashboard
2. Fill all fields (ID, Name, Department, Course, etc.)
3. Click **Save** to store in database
4. Click **Take Pic** - webcam captures 100 face samples automatically

### Training the Model

1. Click **Data Train** from dashboard
2. Click **Train Dataset** button
3. LBPH model trains on all captured face samples
4. Generates `clf.xml` classifier file

### Marking Attendance

1. Click **Face Detector** from dashboard  
2. Webcam activates with real-time face detection
3. **Confidence > 77%** - Student identified
4. **Confidence <= 77%** - "Unknown Face"
5. Attendance auto-saved to `attendance.csv`

### Viewing Reports

1. Click **Attendance** from dashboard
2. **Left Panel:** Import/Export CSV attendance
3. **Right Panel:** MySQL attendance records
4. Use **Import CSV** to load external attendance
5. Use **Export CSV** to download records

---

## UI Theme

```text
Color Palette
- Primary:   #1a1a2e  (Dark Navy)
- Accent:    #e94560  (Crimson Red)
- Secondary: #16213e  (Deep Blue)
- Light:     #FFFFFF  (White)
- Font:      Segoe UI (Modern Sans-Serif)
```

- **Flat design** buttons with hover effects
- **Consistent padding** and spacing across all panels
- **Treeview tables** with scrollable content
- **Responsive layouts** for 1366x768 resolution

---

## Troubleshooting

| # | Error | Cause | Solution |
|---|-------|-------|----------|
| 1 | `ModuleNotFoundError` | Missing packages | Run `pip install -r requirements.txt` |
| 2 | `Can't open camera` | Webcam not detected | Check camera connection & permissions |
| 3 | `MySQL connection failed` | Database not running | Start MySQL service & verify credentials |
| 4 | `Face not detected` | Poor lighting | Ensure face is well-lit & directly facing camera |
| 5 | `Unknown Face` | Low confidence | Re-train model with more face samples |
| 6 | `Port 3307 refused` | Wrong MySQL port | Update port in all files to match your MySQL config |
| 7 | `No module named cv2` | OpenCV not installed | Run `pip install opencv-python opencv-contrib-python` |

---

## License

```text
MIT License

Copyright (c) 2026 Sai SriRam Vanama

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Contact

**Developer:** Sai SriRam Vanama  
**Email:** [saisriram2796@gmail.com](mailto:saisriram2796@gmail.com)  
**LinkedIn:** [linkedin.com/in/saisriramv](https://linkedin.com/in/saisriramv)  
**GitHub:** [github.com/SaiSriRam-Vanama](https://github.com/SaiSriRam-Vanama)  

---

<div align="center">

**Made for smarter attendance management**

If you found this project useful, please consider giving it a star!

</div>
