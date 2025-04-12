# 🛡️ Password Cracking Playground

A web-based cybersecurity tool that simulates real-world password cracking techniques in a safe, ethical, and educational environment. Built using Python and Flask, this interactive app allows users to hash passwords, perform brute-force and dictionary attacks, and view logs of all cracking attempts.

---

## 🔍 Features

| Feature                  | Description                                                       |
|--------------------------|-------------------------------------------------------------------|
| 🔐 Hash Passwords        | Hash any password with SHA-256 and bcrypt                        |
| 🧪 Dictionary Attack     | Crack SHA-256 hashes using a common password wordlist            |
| 💣 Brute Force Cracking  | Try every lowercase combination up to 4 characters               |
| 🔢 Guess Counter         | Shows how many guesses brute force took                          |
| ⏱️ Time Tracker          | Displays how long the brute-force attack took                    |
| 📜 Log Viewer            | Shows last 10 cracking attempts in-browser                       |
| 🧹 Clear Log Button      | One-click button to erase log history from the UI                |
| 🖥️ Web Interface         | Built with Flask and styled with clean HTML/CSS                 |

---

## 🧠 Technologies Used

- **Python 3**
- **Flask**
- **hashlib** (SHA-256 hashing)
- **bcrypt** (secure salted password hashing)
- **itertools** (brute-force generator)
- **HTML + CSS** (for UI)

---


## 🚀 How to Run Locally

1. **Clone this repo**

```bash
git clone https://github.com/scochran96/PasswordCrackingPlayground.git
cd PasswordCrackingPlayground

2. pip install -r requirements.txt

3. python app.py