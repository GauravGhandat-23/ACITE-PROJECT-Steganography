<h1 align="center"> 📷 SECURE DATA HIDING IN IMAGES USING STEGANOGRAPHY 📷 </h1>

![image](https://github.com/user-attachments/assets/0cf47d73-05cb-4395-bdc8-651e96b7d403)

## 📝 Description
The Image-Based Steganography Tool is a Python-powered application that enables users to securely hide messages within images using AES encryption and LSB (Least Significant Bit) steganography. The tool provides both encoding and decoding functionality through an intuitive Streamlit-based UI.

## ⭐ Features

- 🔐 **AES Encryption**: Encrypts messages using AES-CBC mode before embedding them in images.
- 🖼️ **LSB Steganography**: Hides encrypted messages in images at the pixel level.
- 📤 **Image Upload & Download**: Allows users to upload images, encode/decode messages, and download encrypted images.
- 🛠 **User-Friendly Interface**: Built with Streamlit for a seamless experience.


## 📥 Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/ACITE-PROJECT-Steganography.git
   cd ACITE-PROJECT-Steganography.git
   ```
2. Install required dependencies:
   ```sh
   pip install streamlit opencv-python numpy pycryptodome
   ```
3. Run the Application
   ```sh
   streamlit run stego.py
   ```
   
## 🛠 Usage
## 🔵 Encoding a Message

1. Upload a PNG image.
2. Enter your secret message.
3. Provide a passcode (used for encryption & decryption).
4. Click Encode & Save Image.
5. Download the newly encrypted image.

### 🟢 Decoding a Message

1. Upload an encrypted image.
2. Enter the correct passcode.
3. Click Decode Message.
4. View the decrypted message.

## 📸 Screenshots

## Encode Message

![encoded example](https://github.com/user-attachments/assets/36eacc75-acf5-4d70-b5f1-24f70589dc59)

## Decode Message

![image](https://github.com/user-attachments/assets/e54e22aa-afcb-41b5-a1f0-e6116f33a867)


### 🛡️ Security Considerations

- AES encryption ensures strong message protection.
- Messages are not retrievable without the correct passcode.
- Ensure images are stored securely to prevent unauthorized access.

### 👨‍💻 Technologies Used

- Python 🐍

- Streamlit 📊

- penCV 📷

- PyCryptodome 🔐

### 🤝 Contributing

- Contributions are welcome! Feel free to fork this repository and submit a pull request.

## 🌐 Connect with Me 

- 📧 [Email](mailto:gauravghandat12@gmail.com)
- 💼 [LinkedIn](www.linkedin.com/in/gaurav-ghandat-68a5a22b4)


