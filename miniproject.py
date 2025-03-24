import random

def start_game():
    print("\n🎯 WELCOME TO THE NUMBER GUESSING GAME 🎯")
    
    while True:
        # Choose difficulty level
        print("\nSelect Difficulty Level:")
        print("1️⃣ Easy (1-50, 10 chances)")
        print("2️⃣ Medium (1-100, 7 chances)")
        print("3️⃣ Hard (1-200, 5 chances)")
        
        level = input("Enter 1, 2, or 3: ")
        
        if level == "1":
            max_num, chances = 50, 10
        elif level == "2":
            max_num, chances = 100, 7
        elif level == "3":
            max_num, chances = 200, 5
        else:
            print("❌ Invalid choice! Please select again.")
            continue

        target = random.randint(1, max_num)
        print(f"\n🎲 A random number between 1 and {max_num} has been chosen!")
        print(f"🔥 You have {chances} attempts to guess correctly. Good luck!\n")

        # Game loop
        attempts = 0
        while chances > 0:
            user_input = input(f"🔢 Enter your guess (or type 'Q' to quit): ").strip()
            
            if user_input.upper() == "Q":
                print("🚪 You quit the game. Thanks for playing!")
                return
            
            if not user_input.isdigit():
                print("❌ Invalid input! Please enter a number.")
                continue

            user_guess = int(user_input)
            attempts += 1

            if user_guess == target:
                print(f"🎉 SUCCESS: YOU GUESSED IT IN {attempts} ATTEMPTS! 🎯")
                break
            elif user_guess < target:
                print("📉 Your number is too low! Try a higher guess.")
            else:
                print("📈 Your number is too high! Try a lower guess.")
            
            chances -= 1
            print(f"🔁 Chances left: {chances}\n")

        if chances == 0:
            print(f"💀 GAME OVER! The correct number was {target}.")

        # Ask for replay
        replay = input("\n🔄 Do you want to play again? (Y/N): ").strip().upper()
        if replay != "Y":
            print("👋 Thanks for playing! See you next time.")
            break

# Start the game
start_game()
