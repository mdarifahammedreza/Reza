import os
from cryptography.fernet import Fernet

# Load the encryption key from the key file
with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()

# Create a Fernet cipher with the key
cipher_suite = Fernet(key)

# Specify the directory containing the encrypted files
input_directory = input("Enter the directory path with encrypted files: ")

# Loop through each file in the input directory
for filename in os.listdir(input_directory):
    input_file_path = os.path.join(input_directory, filename)

    # Check if the file is a regular file (not a directory)
    if os.path.isfile(input_file_path):
        # Read the contents of the encrypted file
        with open(input_file_path, "rb") as file:
            encrypted_data = file.read()

        try:
            # Decrypt the encrypted data
            decrypted_data = cipher_suite.decrypt(encrypted_data)

            # Replace the encrypted file with the decrypted one
            with open(input_file_path, "wb") as file:
                file.write(decrypted_data)

            print(f"File '{input_file_path}' decrypted and replaced with the decrypted version.")
        except Exception as e:
            print(f"Failed to decrypt '{input_file_path}': {str(e)}")

print("Decryption complete.")

