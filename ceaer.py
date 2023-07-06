def caesar_cipher(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_text += char
    
    return encrypted_text

# Example usage
plaintext = input("enter plaintext: ")
shift_value = 3
encrypted_text = caesar_cipher(plaintext, shift_value)

print("Plaintext:", plaintext)
print("Shift:", shift_value)
print("Encrypted text:", encrypted_text)
