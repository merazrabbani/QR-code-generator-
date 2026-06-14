# 🌟 Advanced QR Code Generator (Python CLI Project)

A powerful command-line QR Code Generator built using Python.  
This project allows users to generate **custom QR codes with colors, sizes, and history tracking**, making it a practical real-world automation tool.

---

# 🚀 Features

## 🎯 Core Features
- Generate QR codes from text or URLs
- Save QR codes as PNG images
- Auto-create storage folder for QR images
- Timestamp tracking for every QR generated

## 🎨 Customization Features
- QR foreground color selection (Blue, Red, Green, Black)
- Background color customization (White, Black, Grey)
- Size control (Small / Medium / Large)
- Simple menu-driven interface

## 📁 History System
- View all generated QR codes
- Search QR by keyword or filename
- Delete full history
- Stores generation time for each QR

## 🧠 Smart Features
- Prevents duplicate file names
- Handles empty input safely
- Error handling for file operations
- Clean CLI-based workflow

---

# 🛠️ Tech Stack

- Python 3.x  
- qrcode (Python library)  
- os module (file management)  
- datetime module (timestamps)

---

# 📦 Installation

Install required dependency:
pip install qrcode[pil]

---

# ▶️ How to Run

Run the program using:
python main.py

---

# 📂 Project Structure

QR-Generator/
│
├── main.py
├── history.txt
├── QR codes/
│   ├── sample.png
│   ├── example.png
│
└── README.md

---

# 🎮 Menu System

Main Menu:
1. Generate QR
2. History
3. Exit

History Menu:
1. View History
2. Search QR
3. Delete History
4. Exit

---

# 🎨 QR Customization

Foreground Colors:
- Blue
- Red
- Green
- Black

Background Colors:
- White
- Black
- Grey

Size Options:
Small  → 5
Medium → 10
Large  → 15

---

# 🧠 Working Process

1. User enters text or URL  
2. System asks for QR customization  
3. QR is generated using qrcode.QRCode()  
4. Image is saved in /QR codes folder  
5. Entry is stored in history.txt with timestamp  
6. User can view/search/delete history anytime  

---

# 📊 Example History Format

https://google.com | google.png | 14/06/2026 12:30:45  
https://youtube.com | youtube.png | 14/06/2026 12:35:10  

---

# 🔥 Future Improvements

- Add logo inside QR code (Pillow integration)
- Gradient QR codes
- Statistics dashboard (QR count, daily usage)
- Export history to CSV/Excel
- QR scanner using OpenCV
- GUI version using Tkinter
- Cloud-based QR storage

---

# 🧑‍💻 Author

Meraz  
Student | Python Learner | Future Developer

---

# ⭐ Project Goal

This project is built to practice:
- File handling
- Functions and logic building
- Real-world Python automation
- CLI application design
- Modular thinking in programming

---

# 🚀 Status

✔ Stable CLI Version  
✔ Custom QR Generator  
✔ History System Working  
🔜 Next: Logo + GUI + Scanner Upgrade
