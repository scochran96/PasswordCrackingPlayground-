import hashlib

# Ask for the SHA-256 hash to crack
target_hash = input("Enter the SHA-256 hash to crack: ")

# Load wordlist
with open("common_passwords.txt", "r") as file:
    passwords = file.readlines()

# Try each password
for pwd in passwords:
    pwd = pwd.strip()
    hashed = hashlib.sha256(pwd.encode()).hexdigest()

    if hashed == target_hash:
        print(f"\n✅ Password found: {pwd}")
        break
else:
    print("\n❌ Password not found in wordlist.")