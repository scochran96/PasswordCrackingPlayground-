from flask import Flask, render_template, request
import hashlib
import bcrypt
import itertools
import string
import time
from datetime import datetime

app = Flask(__name__)

# === Logging Function ===
def log_crack_attempt(method, target_hash, result, guess_count=None, elapsed=None):
    with open("crack_attempts.log", "a") as log_file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        line = f"[{timestamp}] Method: {method} | Hash: {target_hash} | Result: {result}"
        if guess_count is not None:
            line += f" | Guesses: {guess_count}"
        if elapsed is not None:
            line += f" | Time: {elapsed}s"
        log_file.write(line + "\n")

@app.route('/')
def home():
    logs = read_logs()
    return render_template('index.html', logs=logs)

@app.route('/hash', methods=['POST'])
def hash_password():
    password = request.form['password']
    sha256 = hashlib.sha256(password.encode()).hexdigest()
    bcrypt_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    logs = read_logs()
    return render_template('index.html', sha256=sha256, bcrypt_hash=bcrypt_hash, password=password, logs=logs)

@app.route('/crack', methods=['POST'])
def crack_hash():
    target_hash = request.form['sha256_hash']
    cracked_password = None

    with open("common_passwords.txt", "r") as file:
        for pwd in file:
            pwd = pwd.strip()
            hashed = hashlib.sha256(pwd.encode()).hexdigest()
            if hashed == target_hash:
                cracked_password = pwd
                break

    log_crack_attempt("dictionary", target_hash, cracked_password if cracked_password else "not found")
    logs = read_logs()
    return render_template('index.html', cracked_password=cracked_password, input_hash=target_hash, logs=logs)

@app.route('/brute', methods=['POST'])
def brute_force():
    target_hash = request.form['brute_hash']
    charset = string.ascii_lowercase
    max_length = 4

    guess_count = 0
    start_time = time.time()

    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            attempt = ''.join(guess)
            guess_count += 1
            hashed = hashlib.sha256(attempt.encode()).hexdigest()

            if hashed == target_hash:
                elapsed = round(time.time() - start_time, 2)
                log_crack_attempt("brute", target_hash, attempt, guess_count, elapsed)
                logs = read_logs()
                return render_template('index.html',
                                       brute_result=attempt,
                                       brute_input=target_hash,
                                       brute_guesses=guess_count,
                                       brute_time=elapsed,
                                       logs=logs)

    elapsed = round(time.time() - start_time, 2)
    log_crack_attempt("brute", target_hash, "not found", guess_count, elapsed)
    logs = read_logs()
    return render_template('index.html',
                           brute_result=None,
                           brute_input=target_hash,
                           brute_guesses=guess_count,
                           brute_time=elapsed,
                           logs=logs)

@app.route('/clear_log', methods=['POST'])
def clear_log():
    with open("crack_attempts.log", "w") as file:
        file.write("")
    logs = ["✅ Log cleared successfully."]
    return render_template('index.html', logs=logs)

def read_logs():
    try:
        with open("crack_attempts.log", "r") as file:
            return file.readlines()[-10:]
    except FileNotFoundError:
        return ["No log file found yet."]

if __name__ == '__main__':
    app.run(debug=True)