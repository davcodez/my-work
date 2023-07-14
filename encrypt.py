try:
    message = input("Enter a message to encrypt: ")
    encrypted_message = ""
    
    for word in message:
        encrypted_message += chr(ord(word) + 1) 
    
    print("Encrypted Message:", encrypted_message)

    decrypted_message = ""
    
    for word in encrypted_message:
        decrypted_message += chr(ord(word) - 1)  
    
    print("Decrypted Message:", decrypted_message)

except Exception as e:
    print("An error occurred in the program:", e)
