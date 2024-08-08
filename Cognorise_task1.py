import random

def user_ch():
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice. Please try again.")

def comp_ch():
    return random.choice(['rock', 'paper', 'scissors'])

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "win"
    else:
        return "lose"

def display(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == "win":
        print("You win!")
    elif result == "lose":
        print("You lose!")
    else:
        print("It's a tie!")

def main():
    user_score = 0
    computer_score = 0
    play_again = 'yes'

    while play_again == 'yes':
        user_choice = user_ch()
        computer_choice = comp_ch()
        result = winner(user_choice, computer_choice)
        
        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1

        display(user_choice, computer_choice, result)
        print(f"Score: You {user_score} - {computer_score} Computer\n")

        play_again = input("Do you want to play again? (yes/no): ").lower()

    print("Thanks for playing! Final score:")
    print(f"You: {user_score} - Computer: {computer_score}")

if __name__ == "__main__":
    main()
