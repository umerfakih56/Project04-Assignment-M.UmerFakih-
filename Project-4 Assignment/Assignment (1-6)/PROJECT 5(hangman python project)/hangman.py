import random

def display_hangman(attempts):
    hangman_stages = [
        """
           ------
           |    |
           |    O
           |   /|\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |
           |
           |
           |
        """
    ]
    return hangman_stages[attempts]

def get_word():
    categories = {
        "Animals": ["elephant", "giraffe", "kangaroo", "tiger", "dolphin"],
        "Fruits": ["apple", "banana", "cherry", "mango", "strawberry"],
        "Countries": ["canada", "brazil", "germany", "japan", "australia"],
        "Sports": ["football", "cricket", "tennis", "hockey", "badminton"]
    }
    
    print("Choose a category: ")
    for i, category in enumerate(categories.keys(), 1):
        print(f"{i}. {category}")
    
    while True:
        try:
            choice = int(input("Enter the number of your category choice: "))
            if 1 <= choice <= len(categories):
                selected_category = list(categories.keys())[choice - 1]
                return random.choice(categories[selected_category]).upper()
            else:
                print("Invalid choice. Please select a valid category number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def hangman():
    word = get_word()
    word_completion = "_" * len(word)
    guessed_letters = set()
    guessed_words = set()
    attempts = 6
    
    print("Welcome to Hangman!")
    print(display_hangman(attempts))
    print(word_completion)
    
    while attempts > 0 and "_" in word_completion:
        guess = input("\nEnter a letter or word: ").upper()
        
        if not guess.isalpha():
            print("Invalid input. Please enter only letters.")
            continue

        if len(guess) == 1:  # Single letter guess
            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue
            guessed_letters.add(guess)
            
            if guess in word:
                word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])
                print("Correct!")
            else:
                attempts -= 1
                print("Wrong guess!")
        
        elif len(guess) == len(word):  # Full word guess
            if guess in guessed_words:
                print("You already guessed that word.")
                continue
            guessed_words.add(guess)
            
            if guess == word:
                word_completion = word
                break
            else:
                attempts -= 1
                print("Wrong guess!")
                
        else:
            print("Invalid guess length.")
        
        print(display_hangman(attempts))
        print(word_completion)
    
    if "_" not in word_completion:
        print("Congratulations! You guessed the word!")
    else:
        print(f"Game Over! The word was {word}.")

if __name__ == "__main__":
    hangman()