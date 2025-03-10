import random
import string
from .utils import shuffle_string

def generate_password(length, include_symbols=True, include_numbers=True, include_uppercase=True, **kwargs):
    """
    Generates a random password with the specified length and character options.
    Accepts:
    - length (int): Length of the password.
    - include_symbols (bool): Whether to include special characters.
    - include_numbers (bool): Whether to include digits.
    - include_uppercase (bool): Whether to include uppercase letters.
    
    Extra keyword arguments (kwargs) are ignored to prevent errors.
    """
    # Support 'use_upper' for backward compatibility
    if 'use_upper' in kwargs:
        include_uppercase = kwargs['use_upper']

    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if length < 1:
        raise ValueError("Password length must be at least 1")

    password = ''.join(random.choice(characters) for _ in range(length))
    return shuffle_string(password)

def evaluate_strength(password):
    """
    Evaluates the strength of a password based on its length and character variety.
    Returns a string: 'Weak', 'Moderate', or 'Strong'.
    """
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    # Count the types of characters used
    variety_score = sum([has_upper, has_lower, has_digit, has_special])

    # Strength rules
    if length <= 8:
        return "Weak"
    elif length >= 12 and variety_score >= 3:
        return "Strong"
    elif length >= 8 and variety_score >= 2:
        return "Moderate"
    else:
        return "Weak"
