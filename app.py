from flask import Flask, request, render_template, send_file
import numpy as np
import cv2
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ENCRYPTED_FOLDER = 'encrypted'
DECRYPTED_FOLDER = 'decrypted'
SECRET_KEY = 123  # Simple XOR key

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ENCRYPTED_FOLDER, exist_ok=True)
os.makedirs(DECRYPTED_FOLDER, exist_ok=True)

def xor_encrypt_decrypt(image_path, output_path, key):
    img = cv2.imread(image_path)
    encrypted_img = np.bitwise_xor(img, key)
    cv2.imwrite(output_path, encrypted_img)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = os.path.join(UPLOAD_FOLDER, file.filename)
        encrypted_filename = os.path.join(ENCRYPTED_FOLDER, f"enc_{file.filename}")
        file.save(filename)

        # Encrypt Image
        xor_encrypt_decrypt(filename, encrypted_filename, SECRET_KEY)

        return send_file(encrypted_filename, as_attachment=True)

@app.route('/decrypt', methods=['POST'])
def decrypt_file():
    file = request.files['file']
    if file:
        filename = os.path.join(ENCRYPTED_FOLDER, file.filename)
        decrypted_filename = os.path.join(DECRYPTED_FOLDER, f"dec_{file.filename}")
        file.save(filename)

        # Decrypt Image
        xor_encrypt_decrypt(filename, decrypted_filename, SECRET_KEY)

        return send_file(decrypted_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
