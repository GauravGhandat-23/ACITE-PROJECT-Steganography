# 📷 Image Steganography using OpenCV and Python 📷

## 📝 Description
This project allows users to hide a secret message inside an image using image steganography techniques. The message is encrypted within the image pixels, secured with a SHA-256 hashed password, and can only be retrieved with the correct passcode.

## ⭐ Features
- Hide secret messages inside images securely.
- Encrypt messages with a SHA-256 hashed password.
- Extract and decrypt messages using the correct passcode.
- Supports PNG image format for lossless storage.

## 📌 Requirements
- Python 3.x
- OpenCV (`cv2` module)
- `hashlib` (built-in Python module)

## 📥 Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/Steganography.git
   cd Steganography
   ```
2. Install required dependencies:
   ```sh
   pip install opencv-python
   ```

## 🛠 Usage
### 🔏 Encoding a Message
1. Place the image (`image.png`) in the same directory as the script.
2. Run the script:
   ```sh
   python stego.py
   ```
3. Enter the secret message and a password when prompted.
4. The encrypted message will be saved in `encryptedImage.png`.

### 🔓 Decoding a Message

1. Enter the password for decryption.
2. If the password matches, the hidden message will be displayed.

## 💻 Code Explanation
### `hash_password(password)`
Hashes the password using SHA-256 to enhance security.

### `encode_message(img_path, msg, password)`
- Reads the image and verifies its existence.
- Hashes the password and appends it to the message.
- Encodes the message into the image pixels.
- Saves the modified image as `encryptedImage.png`.

### `decode_message(img_path, password)`
- Reads the encrypted image.
- Extracts the hidden message from the pixels.
- Verifies the stored hash against the user-provided password.
- Displays the secret message if authentication is successful.

## 📖 Example
```sh
Enter secret message: Hello, this is a secret!
Enter passcode: mySecurePassword123
Message encrypted successfully in 'encryptedImage.png'!

Enter passcode for Decryption: mySecurePassword123
Decrypted message: Hello, this is a secret!
```

## ⚠️ Notes
- The message length is limited by the image size.
- Ensure that the image used is a PNG to prevent data loss.
- If the incorrect password is provided, authentication will fail.

## 🌐 Connect with Me 

- 📧 [Email](mailto:gauravghandat12@gmail.com)
- 💼 [LinkedIn](www.linkedin.com/in/gaurav-ghandat-68a5a22b4)


