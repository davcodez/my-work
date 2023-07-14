def encrypt(message):
    encrypted_message = ""
    for word in message:
        encrypted_message += chr(ord(word) + 1)  
    return encrypted_message

def decrypt(encrypted_message):
    decrypted_message = ""
    for word in encrypted_message:
        decrypted_message += chr(ord(word) - 1)  
    return decrypted_message

try:
    message = input("Enter a message to encrypt: ")
    encrypted_message = encrypt(message)
    print("Encrypted Message:", encrypted_message)

    decrypted_message = decrypt(encrypted_message)
    print("Decrypted Message:", decrypted_message)

except:
    print("An error occurred in the program.")