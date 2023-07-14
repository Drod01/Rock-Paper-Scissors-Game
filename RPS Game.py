import random

print("Let's play Rock, Paper, Scissors!")

options = ["rock", "paper", "scissors"]

computer_score = 0
player_score = 0

while True:
    
    player_choice = input("Rock, paper or scissors? ").lower()
    
    if player_choice not in options:
        print("Invalid choice. Try again.")
        continue
    
    computer_choice = random.choice(options)
    print("Computer chose", computer_choice + ".")
    
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock":
        if computer_choice == "scissors":
            print("Rock crushes scissors. You win!")
            player_score += 1
        else:
            print("Paper covers rock. You lose.")
            computer_score += 1
    elif player_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock. You win!")
            player_score += 1
        else:
            print("Scissors cut paper. You lose.")
            computer_score += 1
    elif player_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cut paper. You win!")
            player_score += 1
        else:
            print("Rock crushes scissors. You lose.")
            computer_score += 1
            
    print("Player score:", player_score) 
    print("Computer score:", computer_score)
    
    play_again = input("Play again (y/n)? ")
    if play_again.lower() != "y":
        print("Final scores:")
        print("Player score:", player_score)
        print("Computer score:", computer_score)
        break