import random
import string

def generate_password(length=22, uppercase=True, lowercase=True, digits=True, special_chars=True):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not any([uppercase, lowercase, digits, special_chars]):
        raise ValueError("At least one character type must be enabled.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password