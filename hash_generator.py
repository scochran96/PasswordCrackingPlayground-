import hashlib
import bcrypt

# Ask the user for a password
plain_text = input("Enter a password to hash: ")

# === SHA-256 ===
sha256_hash = hashlib.sha256(plain_text.encode()).hexdigest()
print(f"\n🔒 SHA-256 Hash:\n{sha256_hash}")

# === bcrypt ===
bcrypt_hash = bcrypt.hashpw(plain_text.encode(), bcrypt.gensalt())
print(f"\n🔒 bcrypt Hash:\n{bcrypt_hash.decode()}")
