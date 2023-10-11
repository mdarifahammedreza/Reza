import os
from cryptography.fernet import Fernet

# Generate a random encryption key
key = Fernet.generate_key()

# Save the key to a file (you should keep this key secret)
with open("encryption_key.key", "wb") as key_file:
    key_file.write(key)

# Load the encryption key from the file
with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()

# Create a Fernet cipher with the key
cipher_suite = Fernet(key)

# Specify the directory containing the files you want to encrypt
input_directory = input(f'Enter the directory path: ')

# Loop through each file in the input directory
for filename in os.listdir(input_directory):
    input_file_path = os.path.join(input_directory, filename)

    # Check if the file is a regular file (not a directory)
    if os.path.isfile(input_file_path):
        # Read the contents of the file to encrypt
        with open(input_file_path, "rb") as file:
            file_data = file.read()

        # Encrypt the file data
        encrypted_data = cipher_suite.encrypt(file_data)

        # Replace the original file with the encrypted one
        with open(input_file_path, "wb") as file:
            file.write(encrypted_data)

        print(f"File '{input_file_path}' encrypted and replaced with the encrypted version.")

print("Encryption complete.")

