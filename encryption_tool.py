import os
import sys
import hashlib
from cryptography.fernet import Fernet, InvalidToken


KEY_FILE = "secret.key"
ENCRYPTED_FILE = "student_record.enc"
DECRYPTED_FILE = "student_record_decrypted.txt"
HASH_FILE = "student_record.sha256"


def generate_key():
    """Generate an encryption key if one does not already exist."""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()

        with open(KEY_FILE, "wb") as file:
            file.write(key)

        print(f"New encryption key created: {KEY_FILE}")


def load_key():
    """Load the encryption key."""
    if not os.path.exists(KEY_FILE):
        print(f"Error: Encryption key '{KEY_FILE}' was not found.")
        print("Generate or restore the key before continuing.")
        return None

    try:
        with open(KEY_FILE, "rb") as file:
            key = file.read()

        # Validate the key
        Fernet(key)

        return key

    except Exception:
        print("Error: Invalid encryption key.")
        return None


def calculate_sha256(filename):
    """Calculate the SHA-256 hash of a file."""
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


def encrypt_file(filename, key):
    """Encrypt the supplied file."""
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' was not found.")
        return False

    try:
        with open(filename, "rb") as file:
            original_data = file.read()

        cipher = Fernet(key)
        encrypted_data = cipher.encrypt(original_data)

        with open(ENCRYPTED_FILE, "wb") as file:
            file.write(encrypted_data)

        print(f"File encrypted successfully: {ENCRYPTED_FILE}")

        return True

    except Exception as error:
        print(f"Encryption error: {error}")
        return False


def decrypt_file(key):
    """Decrypt the encrypted file."""
    if not os.path.exists(ENCRYPTED_FILE):
        print(f"Error: Encrypted file '{ENCRYPTED_FILE}' was not found.")
        return False

    try:
        with open(ENCRYPTED_FILE, "rb") as file:
            encrypted_data = file.read()

        cipher = Fernet(key)
        decrypted_data = cipher.decrypt(encrypted_data)

        with open(DECRYPTED_FILE, "wb") as file:
            file.write(decrypted_data)

        print(f"File decrypted successfully: {DECRYPTED_FILE}")

        return True

    except InvalidToken:
        print("Error: Decryption failed. The file may have been modified or the key is incorrect.")
        return False

    except Exception as error:
        print(f"Decryption error: {error}")
        return False


def verify_original(original_file):
    """Verify that the decrypted file matches the original."""
    if not os.path.exists(original_file):
        print(f"Error: Original file '{original_file}' was not found.")
        return False

    if not os.path.exists(DECRYPTED_FILE):
        print("Error: Decrypted file was not found.")
        return False

    try:
        with open(original_file, "rb") as original:
            original_data = original.read()

        with open(DECRYPTED_FILE, "rb") as decrypted:
            decrypted_data = decrypted.read()

        if original_data == decrypted_data:
            print("Verification successful: Decrypted file matches the original.")
            return True

        print("Verification failed: Decrypted file does not match the original.")
        return False

    except Exception as error:
        print(f"Verification error: {error}")
        return False


def save_hash(filename):
    """Calculate and save the SHA-256 hash of a file."""
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' was not found.")
        return False

    try:
        file_hash = calculate_sha256(filename)

        with open(HASH_FILE, "w") as file:
            file.write(file_hash)

        print(f"SHA-256 hash: {file_hash}")
        print(f"Hash saved to: {HASH_FILE}")

        return True

    except Exception as error:
        print(f"Hashing error: {error}")
        return False


def detect_change(filename):
    """Compare the current file hash with the stored hash."""
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' was not found.")
        return False

    if not os.path.exists(HASH_FILE):
        print(f"Error: Hash file '{HASH_FILE}' was not found.")
        return False

    try:
        current_hash = calculate_sha256(filename)

        with open(HASH_FILE, "r") as file:
            original_hash = file.read().strip()

        print(f"Stored SHA-256:  {original_hash}")
        print(f"Current SHA-256: {current_hash}")

        if current_hash == original_hash:
            print("Integrity check: File has NOT changed.")
            return True

        print("Integrity check: WARNING - File has been changed!")
        return False

    except Exception as error:
        print(f"Integrity check error: {error}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python encryption_tool.py <student_record_file>")
        return

    original_file = sys.argv[1]

    # Generate key if necessary
    generate_key()

    # Load key
    key = load_key()

    if key is None:
        return

    # Encrypt
    if not encrypt_file(original_file, key):
        return

    # Decrypt
    if not decrypt_file(key):
        return

    # Verify decrypted content
    verify_original(original_file)

    # Calculate and save SHA-256 hash
    save_hash(original_file)

    # Check whether the original file has changed
    detect_change(original_file)


if __name__ == "__main__":
    main()
