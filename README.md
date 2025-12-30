# Image Encryption & Decryption Tool

A simple web-based tool aimed at demonstrating basic image encryption and decryption principles using pixel manipulation. Built with Python, Flask, and OpenCV.

## 🔒 Features

- **Encrypt Image**: Upload any image to encrypt it into unreadable noise using a secure XOR operation.
- **Decrypt Image**: Restore encrypted images back to their original form using the correct key.
- **Visual Feedback**: Simple and clean user interface to manage your uploads.S
- **Reset Option**: Quickly clear your selections with a dedicated Reset button.
- **Educational**: Includes a section explaining how the encryption process works.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Image Processing**: OpenCV, NumPy
- **Frontend**: HTML5, CSS3

## 🚀 Installation & Setup

1.  **Clone the repository** (if applicable) or navigate to the project folder.

2.  **Run the Application**:
    ```bash
    python app.py
    ```



## 📖 How It Works

This tool utilizes **XOR Encryption**.
- **Encryption**: Each pixel's RGB value is XOR-ed with a secret key (default: `123`). This scrambles the visual data.
- **Decryption**: Applying the XOR operation again with the same key reverses the change, restoring the original pixel values.

## User Interface

![alt text](<Screenshot 2025-12-30 131608.png>)