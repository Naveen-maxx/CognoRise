import random

def roll(sides, rolls):
    result = []
    for _ in range(rolls):
        outcome = random.randint(1, sides)
        result.append(outcome)
    return result

def main():
    print("Hello There!")
    print("Welcome to the Dice Rolling Simulator!")
    
    while True:
        try:
            sides = int(input("Enter the number of sides on the dice: "))
            rolls = int(input("Enter the number of rolls: "))
            
            if sides <= 0 or rolls <= 0:
                print("Both numbers must be positive integers. Please try again.")
                continue
            
            result = roll(sides, rolls)
            
            print(f"\nRolling a {sides}-sided dice {rolls} times:")
            for i, outcome in enumerate(result, start=1):
                print(f"Roll {i}: {outcome}")
            
            choice = input("\nDo you want to roll again? (yes/no): ").lower()
            if choice != 'yes':
                print("Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter positive integers only.")
            continue

if __name__ == "__main__":
    main()
