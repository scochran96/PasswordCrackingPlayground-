import hashlib
import itertools
import string
import time

# Input hash from user
target_hash = input("Enter the SHA-256 hash to crack: ")

# Settings
charset = string.ascii_lowercase
max_length = 4  # increase with caution

guess_count = 0
start_time = time.time()

# Try all combos
for length in range(1, max_length + 1):
    for guess in itertools.product(charset, repeat=length):
        attempt = ''.join(guess)
        guess_count += 1
        hashed = hashlib.sha256(attempt.encode()).hexdigest()

        if hashed == target_hash:
            elapsed = round(time.time() - start_time, 2)
            print(f"\n✅ Password found: {attempt}")
            print(f"🔢 Total guesses: {guess_count}")
            print(f"⏱️ Time taken: {elapsed} seconds")
            exit()

# Not found
elapsed = round(time.time() - start_time, 2)
print("\n❌ Password not found")
print(f"🔢 Total guesses: {guess_count}")
print(f"⏱️ Time taken: {elapsed} seconds")