if __name__ == "__main__":
    choice = input("Enter 'E' to encrypt or 'D' to decrypt: ")

    if choice.upper() == "E":
        text = input("Enter the text to encrypt: ")
        shift = int(input("Enter the shift value: "))

        encrypted_text = ""
        for char in text:
            if char.isalpha():
                start = ord('a') if char.islower() else ord('A')
                offset = (ord(char) - start + shift) % 26
                encrypted_text += chr(start + offset)
            else:
                encrypted_text += char

        print("Encrypted text :", encrypted_text)

    elif choice.upper() == "D":
        text = input("Enter the text to decrypt: ")
        shift = int(input("Enter the shift value: "))

        decrypted_text = ""
        for char in text:
            if char.isalpha():
                start = ord('a') if char.islower() else ord('A')
                offset = (ord(char) - start - shift) % 26
                decrypted_text += chr(start + offset)
            else:
                decrypted_text += char

        print("Decrypted text:", decrypted_text)

    else:
        print("Invalid choice.")
RecursionError