import random

def computer_guesses():
    print("Think of a number between 1 and 100, and I'll try to guess it!")
    low, high = 1, 100
    attempts = 0
    
    while low <= high:
        guess = random.randint(low, high)
        attempts += 1
        
        response = input(f"Is your number {guess}? (h/l/c): ").lower()
        
        if response == 'c':
            print(f"Yay! I guessed your number {guess} in {attempts} attempts.")
            break
        elif response == 'h':
            high = guess - 1
        elif response == 'l':
            low = guess + 1
        else:
            print("Invalid input. Please enter 'h' for too high, 'l' for too low, or 'c' for correct.")

if __name__ == "__main__":
    computer_guesses()
