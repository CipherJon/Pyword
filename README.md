# Pyword

Python password generator utilities for secure password creation.

## Features
- Generate secure random passwords with customizable length
- Password strength evaluation
- Support for different character sets (letters, numbers, symbols)
- CLI/GUI programmatic interfaces

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```python
from generator.password_generator import generate_password

# Generate a 12-character password with letters, numbers, and symbols
password = generate_password(length=12, use_letters=True, use_numbers=True, use_symbols=True)
print(password)
```

## CLI Usage
```bash
python main.py --length 15 --numbers --symbols
```

## GUI Usage
```bash
python app.py
```

## Contributing
Pull requests are welcome. Please open an issue first to discuss changes.
