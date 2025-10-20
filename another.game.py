# rock_paper_scissors_interface.py
import random
def print_header():
    print("=" * 40)
    print("🎮 Welcome to Rock-Paper-Scissors 🎮".center(40))
    print("=" * 40)

def print_round_header(round_num, total_rounds):
    print("\n" , "-" * 40)
    print(f"🕹️ Round {round_num} of {total_rounds}".center(40))
    print("-" * 40)

def get_user_choice():
    print("\nChoose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Enter 1, 2, or 3: ")
    if choice == "1":
        return "rock"
    elif choice == "2":
        return "paper"
    elif choice == "3":
        return "scissors"
    else:
        print("❌ Invalid input. Try again.")
        return get_user_choice()

def get_computer_choice(round_number=None):
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def decide_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def play_game():
    print_header() 
    rounds = int(input("How many rounds would you like to play? (3 or 5 or 7): "))
    if rounds < 3:
        print("Minimum is 3 rounds. Setting to 3.")
        rounds = 3
    elif rounds % 2 == 0:
        rounds += 1  # Make it odd for fair win possibility

    user_score = 0
    computer_score = 0

    for round_number in range(1, rounds + 1):
        print_round_header(round_number, rounds)
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\n🧑 You chose: {user_choice}")
        print(f"💻 Computer chose: {computer_choice}")

        winner = decide_winner(user_choice, computer_choice)
        if winner == "user":
            print("✅ You win this round!")
            user_score += 1
        elif winner == "computer":
            print("❌ Computer wins this round!")
            computer_score += 1
        else:
            print("🤝 It's a draw.")

        print(f"\n📊 Scoreboard: You {user_score} - {computer_score} Computer")

    print("\n" + "=" * 40)
    print("🏁 Game Over".center(40))
    print("=" * 40)
    if user_score > computer_score:
        print("🎉 Congratulations! You won the game!")
    elif computer_score > user_score:
        print("😞 Computer won the game. Better luck next time!")
    else:
        print("🤝 It's a tie!")

# Start the game
play_game()