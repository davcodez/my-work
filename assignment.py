import random
import string

def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation

    
    password = set()
    while len(password) < length:
        password.add(random.choice(characters))

    return ''.join(password)


password = generate_password(15)
print("Generated Password:", password)
# The End