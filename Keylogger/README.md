# 🖥️ Keylogger — Keyboard Activity Monitor

A Python-based keystroke logging tool with a simple GUI interface, built for **educational and cybersecurity research purposes only**.

---

## 📌 Project Overview

This project is a lightweight keylogger application that captures and logs all keyboard activity in real time. It features a minimal Tkinter GUI and saves keystroke data to both JSON and plain text formats.

---

## ✨ Features

- Simple one-click GUI to start the keylogger
- Captures three keyboard event states — **Pressed**, **Held**, and **Released**
- Saves structured logs to `log.json`
- Saves plain text keystroke history to `logs.txt`
- Real-time logging — files update with every keystroke

---

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| Python 3.14 | Core programming language |
| pynput | OS-level keyboard event listener |
| Tkinter | GUI window and button interface |
| JSON | Structured log storage |
| File I/O | Plain text log writing |

---

## 📁 Project Structure

```
keylogger/
│
├── keylogger.py       # Main application file
└── README.md          # Project documentation
```

---

## ⚙️ Installation

### Prerequisites
- Python 3.14 installed on your system
- pip package manager

### Step 1 — Clone the Repository
```bash
git clone https://github.com/prinsonjose/DIY-Project/tree/39860f748f9d2b136d34f00ac653ffa34dde8b63/Keylogger
cd keylogger
```

### Step 2 — Install Dependencies
```bash
pip install pynput
```

> Tkinter comes pre-installed with Python. If missing, install it via:
> ```bash
> sudo apt-get install python3-tk   # Linux
> ```

---

## ▶️ Usage

Run the application using:

```bash
python keylogger.py
```

1. A small GUI window (250×200) will open
2. Click the **"Start Keylogger"** button
3. Begin typing anywhere — all keystrokes are captured
4. Check `log.json` and `logs.txt` for recorded output

---

## 📄 Output Format

### log.json
```json
[
  {"Pressed": "Key.shift"},
  {"Held": "Key.shift"},
  {"Released": "Key.shift"},
  {"Pressed": "'h'"},
  {"Released": "'h'"}
]
```

### logs.txt
```
Key.shift'h''e''l''l''o'
```

---

## ⚠️ Known Issues

| Issue | Description |
|-------|-------------|
| File overwrite mode | `+wb` mode rewrites the entire JSON file on every keystroke instead of appending |
| Press/Hold flag bug | Every keypress logs both "Pressed" and "Held" due to flag logic error |
| GUI freezes | `listener.join()` blocks the main thread after clicking Start, freezing the window |

---

## 🔧 Possible Improvements

- Fix the press/hold boolean flag logic
- Run the keyboard listener in a separate thread to keep GUI responsive
- Add a **Stop** button to end logging gracefully
- Add a live keystroke display inside the GUI window
- Encrypt log files for secure storage
- Add timestamp to each keystroke event

---

## ⚖️ Legal & Ethical Disclaimer

> ⚠️ **This project is strictly for educational and authorized use only.**

- **Do NOT** deploy this software on any system without the **explicit consent** of the owner
- Unauthorized use of keyloggers is **illegal** and violates computer fraud laws including:
  - CFAA (Computer Fraud and Abuse Act) — USA
  - IT Act 2000 — India
  - Computer Misuse Act — UK
- The author holds **no responsibility** for any misuse of this software

---

## 📚 Educational Use Cases

- Learning how keyloggers work in cybersecurity courses
- Ethical hacking and penetration testing (authorized environments only)
- Understanding input event handling in Python
- Demonstrating the importance of endpoint security

---

*Built with Python 🐍 | For Educational Purposes Only*
