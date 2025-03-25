# Import necessary modules
from random import randint

# Define Hacker class
class Hacker:
    def __init__(self, alias):
        self.alias = alias
        self.hack_attempts = 0
        self.suspicion_level = 0
        self.max_failures = 5
    
    def hack(self):
        code = randint(1000, 9999)  # Generate random 4-digit security code
        attempts_left = 3

        print(f"\nHacker {self.alias}, you are attempting to hack the system!")
        
        while attempts_left > 0:
            guess = input(f"Enter 4-digit code (Attempts left: {attempts_left}): ")
            
            # Check if the guess is valid (4 digits and numeric)
            if not guess.isdigit() or len(guess) != 4:
                print("❌Invalid code! Must be 4 digits.")
                continue
            
            if int(guess) == code:
                print("Access granted! You have breached the system!")
                self.suspicion_level = 0  # Reset suspicion after success
                print("Suspicion Level Reset. You’re in the clear!")
                return True
            
            else:
                print("❌Incorrect code. Try again.")
                attempts_left -= 1
        
        # If all attempts fail, increase suspicion level
        print(f"Intrusion detected! {self.alias}, the system is getting suspicious!")
        self.suspicion_level += 1

        if self.suspicion_level == 3:
            print("Warning! High suspicion level. One more mistake and the system may lock you out!")
        
        if self.suspicion_level >= self.max_failures:
            print("Maximum failed attempts detected! You are locked out forever!")
            return False
        
        return True

# Main hacker simulation function
def main():
    alias = input("Enter your hacker alias: ")
    hacker = Hacker(alias)

    # Loop until the user chooses to exit or gets locked out
    while True:
        print("\n1. Attempt to Hack\n2. Check Suspicion Level\n3. Exit Game")
        choice = input("Choose an action (1-3): ")
        
        if choice == "1":
            success = hacker.hack()
            if not success:
                print("You've triggered maximum security. Game over!")
                break
        elif choice == "2":
            print(f"Suspicion Level: {hacker.suspicion_level}/{hacker.max_failures}")
        elif choice == "3":
            print(f"Goodbye, {hacker.alias}. Stay in the shadows...")
            break
        else:
            print("Invalid choice! Try again.")

    # Ask if the user wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        main()
    else:
        print("Exiting... Until next time, hacker!")
        return


if __name__ == "__main__":
    main()
