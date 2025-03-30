import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special = string.punctuation if use_special else ''
    
    all_chars = lower + upper + digits + special
    if not all_chars:
        raise ValueError("At least one character set must be enabled.")
    
    password = ''.join(random.sample(all_chars, length))
    return password

def get_user_preferences():
    try:
        length = int(input("Enter password length (default 12): ") or 12)
        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
        
        return length, use_uppercase, use_digits, use_special
    except ValueError:
        print("Invalid input. Using default settings.")
        return 12, True, True, True

if __name__ == "__main__":
    length, use_uppercase, use_digits, use_special = get_user_preferences()
    password = generate_password(length, use_uppercase, use_digits, use_special)
    print(f"Generated Password: {password}")
