# Author : @valuthringer
# Rock Paper Scissors Lizard Spock
# A simple Rock Paper Scissors Lizard Spock game in Python
# Rules: https://bigbangtheory.fandom.com/wiki/Rock,_Paper,_Scissors,_Lizard,_Spock

import random

def get_choice_name(choice):
    choices = {1: "✊", 2: "✋", 3: "✌", 4: "🦎", 5: "🖖"}
    return choices.get(choice, "Invalid")

def determine_winner(player, computer):
    winning_cases = {
        1: [3, 4], #Rock crushes scissors & crushes lizard
        2: [1, 5], #Paper covers Rock & disproves Spock
        3: [2, 4], #Scissors cut Paper & beat Lizard
        4: [2, 5], #Lizard eats Paper & poisons Spock
        5: [1, 3] #Spock vaporizes Rock & smashes Scissors
    }
    
    if player == computer:
        return "It's a tie!"
    elif computer in winning_cases[player]:
        return "The player won!"
    else:
        return "The computer won!"

def main():
    while True:
        print("================================")
        print("Rock Paper Scissors Lizard Spock")
        print("================================")
        print("1) ✊\n2) ✋\n3) ✌\n4) 🦎\n5) 🖖")
        
        try:
            player = int(input("Pick a number: "))
            if player not in [1, 2, 3, 4, 5]:
                print("Invalid choice! Please choose a number between 1 and 5.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        computer = random.randint(1, 5)
        
        print(f"\nYou chose: {get_choice_name(player)}")
        print(f"CPU chose: {get_choice_name(computer)}")
        print(determine_winner(player, computer))
        
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != "y" and play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()