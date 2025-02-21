from generator.password_generator import generate_password

if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    include_symbols = input("Include symbols (y/n)? ").strip().lower() == 'y'
    include_numbers = input("Include numbers (y/n)? ").strip().lower() == 'y'
    include_uppercase = input("Include uppercase letters (y/n)? ").strip().lower() == 'y'
    
    password = generate_password(length, include_symbols, include_numbers, include_uppercase)
    print(f"Generated password: {password}")