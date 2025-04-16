from cryptography.fernet import Fernet

def genrate_key():
    key = Fernet.generate_key()

    with open('key.key', 'wb') as Key_file:
        Key_file.write(key)
    print("Encryption key generated successfully.")

if __name__ == "__main__":
    genrate_key()
    