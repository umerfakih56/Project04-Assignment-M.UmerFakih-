import random

def rock_paper_scissors():
    """Rock Paper Scissors Game"""
    choices = ["rock", "paper", "scissors"]
    score = {"user": 0, "computer": 0}
    
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        
        if user_choice == "quit":
            print(f"Final Score - You: {score['user']}, Computer: {score['computer']}")
            print("Thanks for playing!")
            break
        
        if user_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            score["user"] += 1
        else:
            print("You lose!")
            score["computer"] += 1
        
        print(f"Current Score - You: {score['user']}, Computer: {score['computer']}")
        print("\nLet's play again!")

if __name__ == "__main__":
    rock_paper_scissors()
