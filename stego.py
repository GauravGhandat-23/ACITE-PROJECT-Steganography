import cv2
import os
import hashlib

def hash_password(password):
    """Hashes the password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def encode_message(img_path, msg, password):
    """Encodes a secret message into an image"""
    img = cv2.imread(img_path)

    if img is None:
        print("Error: Image not found!")
        return

    hashed_password = hash_password(password)  # Hash password
    msg = hashed_password + "::" + msg + "%%"  # Store hash with message

    rows, cols, _ = img.shape
    max_chars = rows * cols * 3  # Each RGB channel stores 1 character

    if len(msg) > max_chars:
        print("Message is too long for this image!")
        return

    d = {chr(i): i for i in range(256)}  # Character to integer mapping
    n, m, z = 0, 0, 0  # Pixel position tracking

    for char in msg:
        img[n, m, z] = d[char]
        z += 1
        if z == 3:
            z = 0
            m += 1
            if m == cols:
                m = 0
                n += 1

    output_image = "encryptedImage.png"  # Use PNG for lossless storage
    cv2.imwrite(output_image, img)
    print("Message encrypted successfully in 'encryptedImage.png'!")

def decode_message(img_path, password):
    """Extracts the secret message from the image"""
    img = cv2.imread(img_path)

    if img is None:
        print("Error: Image not found!")
        return

    rows, cols, _ = img.shape
    c = {i: chr(i) for i in range(256)}  # Integer to character mapping

    n, m, z = 0, 0, 0
    extracted_message = ""

    while True:
        extracted_message += c[img[n, m, z]]
        z += 1
        if z == 3:
            z = 0
            m += 1
            if m == cols:
                m = 0
                n += 1
        if "%%" in extracted_message:  # Stop extracting at delimiter
            break

    try:
        stored_hash, secret_msg = extracted_message.split("::", 1)
        secret_msg = secret_msg.replace("%%", "")  # Remove end delimiter
    except ValueError:
        print("Error in decryption: Corrupted message data.")
        return

    if hash_password(password) == stored_hash.strip():
        print("Decrypted message:", secret_msg.strip())
    else:
        print("Authentication failed! Incorrect passcode.")

# Main Execution
image_path = "image.png"  # Ensure this image exists and is in PNG format

# Encryption
msg = input("Enter secret message: ")
password = input("Enter passcode: ")
encode_message(image_path, msg, password)

# Decryption
pas = input("Enter passcode for Decryption: ")
decode_message("encryptedImage.png", pas)

