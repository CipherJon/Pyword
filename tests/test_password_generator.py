# generator/password_generator.py
import random
import string

def generate_password(length, include_numbers=False, include_symbols=False, include_uppercase=False):
    if length < 1:
        raise ValueError("Length must be at least 1")
    
    # Start with lowercase letters as the base character set
    characters = string.ascii_lowercase
    
    # Add additional character sets based on flags
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    if include_uppercase:
        characters += string.ascii_uppercase
    
    # Generate initial password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Ensure at least one character of each requested type
    if include_numbers and not any(char.isdigit() for char in password):
        # Replace a random character with a digit
        position = random.randint(0, length - 1)
        password = password[:position] + random.choice(string.digits) + password[position + 1:]
    
    # Similar checks could be added for symbols and uppercase if needed
    if include_symbols and not any(char in string.punctuation for char in password):
        position = random.randint(0, length - 1)
        password = password[:position] + random.choice(string.punctuation) + password[position + 1:]
    
    if include_uppercase and not any(char.isupper() for char in password):
        position = random.randint(0, length - 1)
        password = password[:position] + random.choice(string.ascii_uppercase) + password[position + 1:]
    
    return password