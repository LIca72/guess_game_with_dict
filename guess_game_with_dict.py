import random

# Dictionary to hold the game state
game = {
    "secret_number": random.randint(1, 10),
    "attempts": 0,
    "max_attempts": 3,
    "status": "playing"
}

# Main game loop
while game["attempts"] < game["max_attempts"]:
    guess = int(input("🎯 Guess a number between 1 and 10: "))
    game["attempts"] += 1

    if guess == game["secret_number"]:
        print("🎉 Congratulations! You guessed the number!")
        game["status"] = "won"
        break
    else:
        print("❌ Wrong guess. Try again.")

# Game over message
if game["status"] != "won":
    print(f"😢 No more attempts. The correct number was {game['secret_number']}.")
