import random

def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "It's a tie!"
    elif (player_move == "rock" and computer_move == "scissors") or \
         (player_move == "paper" and computer_move == "rock") or \
         (player_move == "scissors" and computer_move == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    moves = ["rock", "paper", "scissors"]
    
    while True:
        player_move = input("Enter your move (rock, paper, scissors) or 'quit' to stop: ").lower()
        if player_move == 'quit':
            print("Thanks for playing!")
            break
        if player_move not in moves:
            print("Invalid move. Please try again.")
            continue
        
        computer_move = random.choice(moves)
        print(f"Computer chose: {computer_move}")
        
        result = determine_winner(player_move, computer_move)
        print(result)

if __name__ == "__main__":
    main()


"""
Short Questions
1. What is the purpose of the moves list?

The moves list stores the possible choices for the game: "rock", "paper", and "scissors". It is used to:

Validate the player's input to ensure they enter a valid move.
Allow the computer to randomly select one of these moves using random.choice(moves).


2. Explain the logic used to decide if the player wins or the computer wins.

The function determine_winner implements the logic to decide the winner of each round. Here's how it works:

Tie: If the player's move is the same as the computer's move, it's a tie.
Player Wins: The player wins if:
They choose "rock" and the computer chooses "scissors".
They choose "paper" and the computer chooses "rock".
They choose "scissors" and the computer chooses "paper".
Computer Wins: In all other cases, the computer wins.
This logic is implemented using conditional statements (if, elif, and else). The winning combinations for the player are explicitly checked, and if none of these conditions are met, the computer is declared the winner.

"""